import click
import os
import time
import numpy as np
import random
import logging
import re

from submit import submit as submit_to_github
from ballet.compat import pathlib, safepath
from ballet.util.log import LevelFilter, SIMPLE_LOG_FORMAT, logger

FEATURE_REGEX = r"feature\_\d\d\.py$"
USER_REGEX = r"user\_\d\d"

MAX_SLEEP_TIME = 8 * 60 + 1
MIN_SLEEP_TIME = 3 * 60

os.chdir(os.path.dirname(os.path.abspath(__file__)))
print(os.getcwd())


def configure_logging(output_dir):
    logger.setLevel(logging.DEBUG)

    handler = logging.FileHandler(output_dir.joinpath("info.log"))
    formatter = logging.Formatter(SIMPLE_LOG_FORMAT)
    handler.setFormatter(formatter)
    handler.setLevel(logging.INFO)
    logger.addHandler(handler)

    handler = logging.FileHandler(output_dir.joinpath("debug.log"))
    handler.setFormatter(formatter)
    handler.setLevel(logging.DEBUG)
    handler.addFilter(LevelFilter(logging.DEBUG))
    logger.addHandler(handler)

    logger.info("***BEGIN NEW SIMULATION SESSION***.")
    logger.debug("***BEGIN NEW SIMULATION SESSION***.")


class SubmissionClient:
    def __init__(self, feature_path, random_seed=1, start=None, end=None):
        self.feature_path = pathlib.Path(feature_path)
        self.start = start
        self.end = end
        self.rng = np.random.RandomState(seed=random_seed)
        self._create_queue()

    def _create_queue(self):
        features = []
        for user_path in self.feature_path.iterdir():
            if not (user_path.is_dir() and re.search(USER_REGEX, str(user_path))):
                continue
            user_num = int(user_path.parts[-1].split("_")[1])
            logger.debug("COLLECTING FEATURES FROM USER {}".format(user_num))
            user_features = []
            for feature_path in user_path.iterdir():
                if not re.search(FEATURE_REGEX, str(feature_path)):
                    logger.debug(
                        "INVALID FEATURE {}".format(safepath(feature_path.parts[-1]))
                    )
                    continue
                feature_num = int(feature_path.parts[-1].split("_")[1].split(".")[0])
                if self.start and self.start > feature_num:
                    continue
                elif self.end and self.end < feature_num:
                    continue
                else:
                    user_features.append((user_num, feature_num))
            logger.debug("FOUND {} FEATURES".format(len(user_features)))
            features.append(sorted(user_features, key=lambda f: f[1]))
        self.feature_queue = self.shuffle_feature_queue(features)
        logger.debug("USING QUEUE:")
        logger.debug("\n".join(list(map(str, self.feature_queue))))

    def shuffle_feature_queue(self, features):
        feature_queue = []
        while len(features) > 0:
            randind = self.rng.randint(0, len(features))
            user_features = features[randind]
            feature = user_features.pop(0)
            feature_queue.append(feature)
            if len(user_features) == 0:
                del features[randind]
        return feature_queue

    def submit(self):
        user, feature = self.feature_queue.pop(0)
        logger.info(
            "Submitting: User {user:02d}, Feature {feature:02d}".format(
                user=user, feature=feature
            )
        )
        submit_to_github(user, feature, str(self.feature_path), False, None, True, True)

    def submit_with_delay(self):
        self.submit()
        if not self.is_completed():
            time_to_sleep = self.rng.randint(MIN_SLEEP_TIME, MAX_SLEEP_TIME)
            logger.debug("Sleeping for {} minutes".format(time_to_sleep / 60.0))
            time.sleep(time_to_sleep)
            logger.debug("Waking up...")

    def is_completed(self):
        return len(self.feature_queue) == 0


@click.command()
@click.option(
    "--from",
    "from_",
    required=True,
    type=click.Path(exists=True, file_okay=False, readable=True, resolve_path=True),
    help="root directory of existing features",
)
@click.option(
    "--start",
    "start",
    type=click.INT,
    required=False,
    default=None,
    help="where to start feature numbers [inclusive]",
)
@click.option(
    "--end",
    "end",
    type=click.INT,
    required=False,
    default=None,
    help="where to end feature numbers [inclusive]",
)
def run_simulation(from_, start, end):
    configure_logging(pathlib.Path("."))
    submitter = SubmissionClient(from_, start=start, end=end)
    while not submitter.is_completed():
        submitter.submit_with_delay()


if __name__ == "__main__":
    run_simulation()
