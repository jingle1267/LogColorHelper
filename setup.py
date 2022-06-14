import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="LogColorHelper",
    version="0.0.4",
    author="jingle1267",
    author_email="jingle1267@163.com",
    description="Log with color for python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jingle1267/LogColorHelper",
    project_urls={
        "Bug Tracker": "https://github.com/jingle1267/LogColorHelper/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)