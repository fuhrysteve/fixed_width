from setuptools import setup, find_packages


with open("README.rst") as f:
    readme = f.read()

setup(
    name="fixed_width",
    version="0.2.0",
    description="Parse fixed-width files in python",
    long_description=readme,
    author="Stephen J. Fuhry",
    author_email="fuhrysteve@gmail.com",
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    url="https://github.com/fuhrysteve/fixed_width",
    license="MIT License",
    packages=find_packages(exclude=("tests", "docs")),
    python_requires=">=3.6",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    test_suite="tests",
)
