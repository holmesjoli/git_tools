import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "archivePy",
    version = "0.0.1",
    author = "Joli Holmes",
    author_email = "holmesjoli@gmail.com",
    description = "Git data archiving functions",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/holmesjoli/archivePy",
    packages = setuptools.find_packages(),
    install_requires = ["GitPython",
                        "numpy",
                        "pandas",
                        "utilsPy"]
)

