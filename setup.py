from setuptools import find_packages, setup


with open("README.md", "r", encoding="utf-8") as file:
    LONG_DESCRIPTION = file.read()


extras = {
    "quality": ["black", "flake8", "isort"],
    "testing": ["pytest"],
}

extras["dev"] = extras["quality"]

setup(
    name="cocktail-opt",
    version="1.0.0.dev0",
    author="Ben Cunningham",
    author_email="benjamescunningham@gmail.com",
    description="Just-for-fun liquor cabinet optimizer",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/benjcunningham/cocktail-opt",
    package_dir={"": "src"},
    packages=find_packages("src"),
    install_requires=[
        "numpy>=1.21.4",
        "pandas>=1.3.4",
    ],
    extras_require=extras,
    python_requires=">=3.9.0",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
    ],
)
