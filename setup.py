from setuptools import setup

setup(
    name="ECEformer",
    version="0.1",
    description="Learning Evolutionary Chain of Events for Temporal Knowledge Graph Reasoning",
    url="https://github.com/seeyourmind/ECEformer",
    author="USTB",
    author_email="xs.b12345@ustb.edu",
    packages=["kge"],
    install_requires=[
        "torch==1.4.0",
        "pyyaml",
        "pandas",
        "argparse",
        "path",
        "sqlalchemy",
        "torchviz",
        "dataclasses",
        # LibKGE uses numba typed-dicts which is part of the experimental numba API
        # in version 0.48
        # see http://numba.pydata.org/numba-doc/0.48.0/reference/pysupported.html
        "numba==0.48.0",
        "pytorch-pretrained-bert==0.6.0",
        "networkx==2.4",
        "regex==2020.5.14",
        "pytorch_lightning==1.3.1"
    ],
    zip_safe=False,
    entry_points={"console_scripts": ["kge = kge.cli:main",],},
)
