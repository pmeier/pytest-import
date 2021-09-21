from setuptools import setup, find_packages

setup(
    name="pytest-import",
    version="0.0.1",
    packages=find_packages(exclude=["tests", "tests.*"]),
    install_requires=["pytest >=6.*"],
    entry_points={
        "pytest11": [
            "pytest-import = pytest_import._plugin",
        ],
    },
)
