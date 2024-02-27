from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="Omodem",
    version="1.5.0",
    author="Pinokaille",
    description="A tui app to manage a orange modem !",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    packages=find_packages(include=["orange", "orange.*"]),
    install_requires=[
        "bs4",
        "requests",
    ],
    entry_points={"console_scripts": ["Orange=orange:main"]},
)
