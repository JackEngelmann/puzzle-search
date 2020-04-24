from setuptools import setup, find_packages

setup(
    name="Puzzle Search",
    version="0.1",
    author="Jack Engelmann",
    packages=find_packages(),
    entry_points={"console_scripts": ["play-puzzle=puzzlesearch.bin.play:main"],},
    python_requires=">=3.6",
    tests_require=["mock"],
)
