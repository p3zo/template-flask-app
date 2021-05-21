from setuptools import find_packages, setup

__build__ = 0
__version__ = f"0.0.1.{__build__}"

dev_requires = ["black", "flake8", "ipdb", "ipython", "isort", "bumpversion"]

test_requires = ["pytest", "pytest-cov"]

setup(
    name="template",
    author="p3zo",
    version=__version__,
    packages=find_packages(exclude=["tests", "tests.*"]),
    package_data={},
    python_requires=">=3.8",
    install_requires=[
        "Flask==2.0.0",
        "Flask-Cors==3.0.10",
        "gunicorn==20.1.0",
    ],
    extras_require={
        "test": test_requires,
        "dev": test_requires + dev_requires,
    },
)
