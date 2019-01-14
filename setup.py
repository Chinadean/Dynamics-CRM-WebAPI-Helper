import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Py365CE",
    version="0.0.1",
    author="colathro",
    author_email="colathro@microsoft.com",
    description="Simple interface for Dynamics CRM Online WebAPI for ETL + automating tasks.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/colathro/Py365CE-Dynamics-CRM",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 1"
    ],
)