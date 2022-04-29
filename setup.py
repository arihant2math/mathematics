import platform
from os import getlogin

import setuptools


MAJOR_VERSION = 0
MINOR_VERSION = 0
PATCH = 0
VERSION = str(MAJOR_VERSION) + "." + str(MINOR_VERSION) + "." + str(PATCH) + "a0.dev20224291"
FILE_VERSION = ""
primes = [2, 3, 5, 7, 11, 13, 17]

if platform.system() == "Windows":
    path = "C:/Users/" + str(getlogin()) + "/AppData/Local/Temp/mathematics-python/"
elif platform.system() == "Darwin":
    path = "~/Library/Application Support/mathematics-python/"
elif platform.system() == "Linux":
    path = "~/.mathematics-python/"
else:
    path = ""
# if not exists(path + "primes.list"):
# 	with open(path + "primes.list", "x") as primes_file:
# 		primes_file.write(str(primes))

with open("README.md", "r", encoding="utf-8") as readme:
    long_description = readme.read()

setuptools.setup(
    name="mathematics",
    version=VERSION,
    author="Ashwin Naren",
    author_email="arihant2math@gmail.com",
    description="A package with mathematical functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/arihant2math/mathemathics",
    packages=["mathematics"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Intended Audience :: Developers",
    ],
    python_requires=">=3.8",
    requires=["numpy", "matplotlib"],
)
