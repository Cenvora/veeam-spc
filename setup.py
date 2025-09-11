"""Veeam-SPC Package Setup (minimal shim; canonical metadata in pyproject.toml)"""

from pathlib import Path
from setuptools import setup

here = Path(__file__).parent

about = {}
version_file = here / "veeam_spc" / "__version__.py"
with version_file.open() as f:
    for line in f:
        if line.startswith("__version__"):
            about["__version__"] = line.split("=")[1].strip().strip("\"'")
        if line.startswith("__title__"):
            about["__title__"] = line.split("=")[1].strip().strip("\"'")

setup(
    name=about["__title__"],
    version=about["__version__"],
    packages=["veeam_spc"],
    include_package_data=True,
    python_requires=">=3.12",
)
