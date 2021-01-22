import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mathematics-package",
    version="0.0.0a3",
    author="Ashwin Naren",
    author_email="arihant2math@gmail.com",
    description="A mathematics package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/arihant2math/mathemathics",
    packages=["number_theory", "counting_and_probability", "algebra"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=["statistics==1.0.3.5"],
    py_modules=["number_theory", "counting_and_probability", "algebra"]
)
