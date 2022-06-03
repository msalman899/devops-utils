from setuptools import setup
import setuptools

setup(
    name="devops-utils",
    version="1.0",
    url="https://github.com/msalman899/devops-utils.git",
    description="A Python Package containing utility / helper functions",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
    install_requires=[
        "requests==2.26.0",
    ]
)
