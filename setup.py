from setuptools import setup, find_packages

requirements = [
    "ballet @ git+https://git@github.com/HDI-Project/ballet@master",
    "Click>=6.0",
]

setup(
    author="Kelvin Lu",
    author_email="kelvinlu@mit.edu",
    entry_points={
        "console_scripts": [
            "ballet_project_simulation-engineer-features=ballet_project_simulation.features:main"
        ]
    },
    install_requires=requirements,
    name="ballet project simulation",
    packages=find_packages(
        include=["ballet_project_simulation", "ballet_project_simulation.*"]
    ),
    url="https://github.com/kelvin-lu/ballet_project_simulation",
)
