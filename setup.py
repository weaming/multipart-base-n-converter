# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))


def _read(fname):
    if path.isfile(fname):
        with open(path.join(here, fname), encoding="utf-8") as f:
            return f.read()
    else:
        print('warning: file {} does not exist'.format(fname))
        return ''


long_description = _read("README.md")
install_requires = [
    l
    for l in _read("requirements.txt").split("\n")
    if l.strip() and not l.strip().startswith("#")
]

name = "multipart-base-n-converter"
gh_repo = "https://github.com/weaming/{}".format(name)

setup(
    name=name,  # Required
    version="0.1.0",  # Required
    # This is a one-line description or tagline of what your project does.
    description="convert a number to string with multiple parts based on the given string base",  # Required
    long_description=long_description,  # Optional
    long_description_content_type="text/markdown",  # Optional
    install_requires=install_requires,
    # You can use `find_packages()` or the `py_modules` argument which expect a
    # single python file
    packages=find_packages(exclude=["contrib", "docs", "tests"]),  # Required
    entry_points={
        "console_scripts": [
            "multipart-base-n=multipart_base_n.__main__:main"
        ]
    },  # Optional
    url=gh_repo,  # Optional
    author="weaming",  # Optional
    author_email="garden.yuen@gmail.com",  # Optional
    keywords="math",  # Optional
    project_urls={"Bug Reports": gh_repo, "Source": gh_repo},  # Optional
)

