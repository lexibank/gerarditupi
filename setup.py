from setuptools import setup, find_packages
import json


with open("metadata.json", encoding="utf-8") as fp:
    metadata = json.load(fp)


setup(
    name="lexibank_gerarditupi",
    version="0.1",
    description=metadata["title"],
    license=metadata.get("license", ""),
    packages=find_packages(where="."),
    url=metadata.get("url", ""),
    py_modules=["lexibank_gerarditupi"],
    include_package_data=True,
    zip_safe=False,
    entry_points={"lexibank.dataset": ["gerarditupi=lexibank_gerarditupi:Dataset"]},
    install_requires=["pylexibank>=3.0"],
    extras_require={"test": ["pytest-cldf"]},
)
