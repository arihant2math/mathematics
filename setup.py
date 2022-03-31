import setuptools

with open("README.md", "r", encoding="utf-8") as readme:
    long_description = readme.read()

setuptools.setup(
    name="mathematics-package",
    version="0.0.0a1",
    author="Ashwin Naren",
    author_email="arihant2math@gmail.com",
    description="A mathematics package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/arihant2math/mathemathics",
    packages=["mathematics"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6"
)
