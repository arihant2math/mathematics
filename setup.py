import platform
from os import getlogin

import setuptools

VERSION = "0.0.0a1.dev202241"

primes = "2, 3, 5, 7, 11, 13, 17"

if platform.system() == "Windows":
	path = "C:/Users/" + str(getlogin()) + "/AppData/Local/Temp/mathematics-python/" + VERSION + "/"
elif platform.system() == "Darwin":
	path = "~/Library/Application Support/mathematics-python/" + VERSION + "/"
elif platform.system() == "Linux":
	path = "~/.mathematics-python/" + VERSION + "/"
else:
	path = ""
# f = open(path + "primes" + ".list", "w+")
# f.write(primes)
# f.close()

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
	],
	python_requires=">=3.8",
	requires=["numpy", "matplotlib"],
)
