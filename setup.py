from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="sweetdebug",
    version="1.0.11",
    description="Automatic pdb invoker",
    author="sweetcocoa",
    author_email="sweetcocoa@snu.ac.kr",
    url="https://github.com/sweetcocoa/sweetdebug",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    py_modules=["dm"],
    python_requires=">=3",
    packages=["sweetdebug"],
    install_requires=["backtrace"],
    extras_require={"telegram": ["python-telegram-bot"]},
)
