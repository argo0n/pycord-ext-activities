from setuptools import setup

classifiers = [
    "Development Status :: 2 - Pre-Alpha",
    "Intended Audience :: Developers",
    "Operating System :: Microsoft :: Windows :: Windows 10",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
]
packages = [
    "discord.ext.activities",
]
setup(
    name="pycord-ext-activities",
    version="2022.08.26",
    description="An Pycord extension that helps you to launch activities on Discord.",  # noqa: E501
    long_description=open("README.md").read(),
    url="",
    author="MaskDuck",
    license="MIT",
    classifiers=classifiers,
    keywords="activities",
    packages=packages,
    long_description_content_type="text/markdown",
    install_requires=["py-cord"],
)
