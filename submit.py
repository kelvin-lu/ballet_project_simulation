#!/usr/bin/env python

import atexit
from textwrap import dedent
from unittest.mock import Mock

import ballet
import ballet.project
import ballet.update
import click
import funcy
import github
from ballet.compat import pathlib
from ballet.exc import BalletError
from ballet.util import one_or_raise
from ballet.util.code import blacken_code
from ballet.util.git import did_git_push_succeed
from ballet.util.log import stacklog


def _get_project():
    import ballet_project_simulation

    return ballet.project.Project(ballet_project_simulation)


def _make_branch_name(user, feature):
    return "submit-feature-{user:02d}-{feature:02d}".format(user=user, feature=feature)


def _check_environment(repo):
    if repo.head.ref.name != ballet.update.DEFAULT_BRANCH:
        repo.branches[ballet.update.DEFAULT_BRANCH].checkout()
    assert not repo.is_dirty()
    origin = repo.remotes.origin
    origin.pull()


@stacklog(print, "Creating and switching to new branch")
def create_and_switch_to_new_branch(repo, user, feature):
    name = _make_branch_name(user, feature)
    if name in repo.branches:
        repo.delete_head("-D", name)
    repo.create_head(name)
    repo.branches[name].checkout()


@stacklog(print, "Creating subdirectories of contrib")
def create_dirs_if_needed(dst):
    dst = pathlib.Path(dst)
    dst.parent.mkdir(parents=True, exist_ok=True)


@stacklog(print, "Reformatting and writing feature")
def read_format_write(src, dst):
    with src.open("r") as f:
        code = f.read()
    try:
        code = blacken_code(code)
    except Exception as e:
        # let's not deal with blacken issues...
        print(e)

    with dst.open("w") as f:
        f.write(code)


@stacklog(print, "Adding init modules")
def add_init_if_needed(dst):
    for d in (dst.parent, dst.parent.parent):
        p = d.joinpath("__init__.py")
        p.touch(exist_ok=True)


@stacklog(print, "Committing changes")
def commit_changes(repo):
    repo.git.add(".")
    repo.git.commit(m="Add new feature")


@stacklog(print, "Pushing changes")
def push_changes(repo, user, feature, dry_run=False):
    branch_name = _make_branch_name(user, feature)
    origin = repo.remote("origin")
    refspec = "{branch}:{branch}".format(branch=branch_name)
    if not dry_run:
        result = origin.push(refspec)
        push_info = one_or_raise(result)
        if not did_git_push_succeed(push_info):
            raise BalletError(
                "Git push failed, " "maybe you need to delete a branch on remote?"
            )
    else:
        print(
            "[dry run] would execute 'origin.push({refspec!r})'".format(refspec=refspec)
        )


def _make_github_client(token):
    if token is None:
        # read from ~/.github/token.txt
        p = pathlib.Path.home().joinpath(".github", "token.txt")
        with p.open("r") as f:
            token = f.read().strip()

    g = github.Github(token)
    return g


@stacklog(print, "Creating pull request")
def create_pull_request(gh, project, user, feature, dry_run=False):
    branch_name = _make_branch_name(user, feature)
    owner = project.get("project", "owner")
    name = project.get("project", "name")
    ghrepo = gh.get_repo("{owner}/{name}".format(owner=owner, name=name))

    # prepare PR metadata
    title = "Propose new feature"
    body = dedent(
        """\
    Propose new feature: feature_{feature:02d}.py
    Submitted by user: user_{user:02d}
    
    Pull request automatically created by {script_name}
    """
    ).format(user=user, feature=feature, script_name="submit.py")
    base = ballet.update.DEFAULT_BRANCH
    head = branch_name
    maintainer_can_modify = True

    # create the pull
    if not dry_run:
        pr = ghrepo.create_pull(
            title=title,
            body=body,
            base=base,
            head=head,
            maintainer_can_modify=maintainer_can_modify,
        )
    else:
        pr = Mock()
        print(
            "[dry run] would execute "
            "'ghrepo.create_pull(title={title!r}, body={body!r}, "
            "base={base!r}, "
            "head={head!r}, maintainer_can_modify={maintainer_can_modify!r})'".format(
                title=title,
                body=body,
                base=base,
                head=head,
                maintainer_can_modify=maintainer_can_modify,
            )
        )

    return pr


# @click.command()
# @click.option('--user',
#               required=True,
#               type=click.INT,
#               help='the "user" that created the feature (id between 1-9)')
# @click.option('--feature',
#               required=True,
#               type=click.INT,
#               help='the "name" of the feature (id between 1-n)')
# @click.option('--from', 'from_',
#               required=True,
#               type=click.Path(exists=True,
#                               file_okay=False,
#                               readable=True,
#                               resolve_path=True),
#               help='root directory of existing features')
# @click.option('-n', '--dry-run',
#               is_flag=True,
#               default=False,
#               help='dry run (do not actually push to remote or create PR)')
# @click.option('--github-token',
#               type=click.STRING,
#               default=None,
#               help='github access token to authorize pull request')
# @click.option('--create-pull/--no-create-pull',
#               default=True,
#               help='create pull request on github')
# @click.option('--cleanup/--no-cleanup',
#               default=True,
#               help='cleanup most changes to the project on exit')
def submit(user, feature, from_, dry_run, github_token, create_pull, cleanup):
    """Submit feature within path to project"""
    project = _get_project()
    repo = project.repo
    to = project.get("contrib", "module_path")

    src = pathlib.Path(
        from_,
        "user_{user:02d}".format(user=user),
        "feature_{feature:02d}.py".format(feature=feature),
    )
    dst = pathlib.Path(
        to,
        "user_{user:02d}".format(user=user),
        "feature_{feature:02d}.py".format(feature=feature),
    )

    # register cleanup
    if cleanup:

        @atexit.register
        @funcy.silent
        def cleanup():
            # check out default branch
            repo.branches[ballet.update.DEFAULT_BRANCH].checkout()

            # delete new branch
            name = _make_branch_name(user, feature)
            repo.delete_head(name)

    _check_environment(repo)
    create_and_switch_to_new_branch(repo, user, feature)
    create_dirs_if_needed(dst)
    read_format_write(src, dst)
    add_init_if_needed(dst)
    commit_changes(repo)
    push_changes(repo, user, feature, dry_run=dry_run)
    gh = _make_github_client(github_token)

    if create_pull:
        pr = create_pull_request(gh, project, user, feature, dry_run=dry_run)
        print("Created pull request: {pr.url}".format(pr=pr))

    print("Submission successful.")


if __name__ == "__main__":
    submit()
