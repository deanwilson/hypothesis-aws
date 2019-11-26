from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="hypothesis-aws",
    version="0.1.0",
    author="Dean Wilson",
    author_email="dwilson@unixdaemon.net",
    description="A hypothesis extension that provides AWS related strategies",
    url="https://github.com/deanwilson/hypothesis-aws",
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Framework :: Hypothesis",
        "Framework :: Pytest",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Testing",
    ],
    keywords="python testing fuzzing property-based-testing aws hypothesis",
)
