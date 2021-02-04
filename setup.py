import setuptools

with open ("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Puzzle",
    version="0.0.1",
    author="Victoria Maksymiuk",
    author_email="viktoriia.maksymyuk@ucu.edu.ua",
    description="Working with puzzle.py",
    long_description=long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/Vihtoriaaa/puzzle.git",
    packages=setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8'
)