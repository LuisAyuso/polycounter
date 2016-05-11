from distutils.core import setup

setup(
    # Application name:
    name="polycounter",

    # Version number (initial):
    version="0.1.0",

    # Application author details:
    author="Luis Ayuso",
    author_email="luis.f.ayuso@gmail.com",

    # Packages
    packages=["py_micro"],

    # Include additional files into the package
    include_package_data=True,

    # Details
    url="",

    #
    license="LICENSE.txt",
    description="Useful towel-related stuff.",

    # long_description=open("README.txt").read(),

    # Dependent packages (distributions)
    install_requires=[
        "PyQt5",
    ],

	# app entry points
	entry_points={'PYMICRO': [ 'py_micro = py_micro.__main__:main' ] },
)

