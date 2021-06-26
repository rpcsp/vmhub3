import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vmhub3",
    version="1.0",
    author="rpcsp",
    author_email="pcunha@hotmail.com",
    description="python module to send instructions to VM Hub 3 routers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    project_urls={
        "Project page": "https://github.com/rpcsp/vmhub3",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    entry_points="""\
    [console_scripts]
    vmhub3 = vmhub3.vmhub3:main
    """
)
