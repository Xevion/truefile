import os
import io
from setuptools import find_packages, setup

DEPENDENCIES = ['Click']
EXCLUDE_FROM_PACKAGES = []
CURDIR = os.path.dirname(__file__)

setup(
    name="truefile",
    version="1.0.0",
    author="Xevion",
    author_email="xevion@xevion.dev",
    description="",
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
    include_package_data=True,
    entry_points='''
        [console_scripts]
        truefile=truefile.cli:cli
    ''',
    install_requires=DEPENDENCIES,
)