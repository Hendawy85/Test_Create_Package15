import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Arthimatic_Package-Ahafez",
    version="0.0.1",
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Hendawy85/Test_Create_Package15",
    project_urls={
        "Bug Tracker": "https://github.com/Hendawy85/Test_Create_Package15/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={ r"C:\Users\ali\PycharmProjects\Test_Create_Package\src\Arthimatic_Package" :"Arthimatic_Package" },
    packages=setuptools.find_packages(where="Arthimatic_Package"),
    python_requires=">=3.6",
)