from setuptools import setup, find_packages

setup(
    name="sweetdebug",
    version="1.0.1",
    description="Test Package",
    author="sweetcocoa",
    author_email="sweetcocoa@snu.ac.kr",
    url="https://sweetcocoa.github.io",
    license="MIT",
    py_modules=["dm"],
    python_requires=">=3",
    packages=["sweetdebug"],  # 패키지가 들어있는 폴더들
)
