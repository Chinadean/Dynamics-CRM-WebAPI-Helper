import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Py365CE",
    version="0.0.2",
    author="colathro",
    author_email="colathro@microsoft.com",
    description="Easy Interface for Dynamics CRM WebAPI for ETL + automation.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/colathro/Py365CE-Dynamics-CRM",
    packages=setuptools.find_packages(),
    install_requires=[
          'requests',
      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 1"
    ],
)