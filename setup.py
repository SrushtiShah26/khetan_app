from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in khetan_app/__init__.py
from khetan_app import __version__ as version

setup(
	name="khetan_app",
	version=version,
	description="khetan_app",
	author="srushti shah",
	author_email="srushti@sanskartechnolab.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
