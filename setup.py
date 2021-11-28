from setuptools import setup, find_packages
from aminos.__init__ import version

with open("README.md", "r") as readme:
    long_description = readme.read()

setup(
    name="Amino-Socket",
    version=version,
    url="https://github.com/hanamixp/Amino-Socket.py.git",
    download_url="https://github.com/Hanamixp/Amino-Socket/archive/refs/heads/main.zip",
    license="Apache V2",
    author="Hanami",
    author_email="hanamixp@gmail.com",
    description="Python API to Connect Amino wss",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[
        "aminoapps",
        "amino",
        "narvii",
        "api",
        "hanami",
        "amino-socket"
    ],
    install_requires=[
        "websocket-client",
        "json_minify",
        "requests",
    ],
    setup_requires=["wheel"],
    project_urls={
        'Source': 'https://github.com/Hanamixp/Amino-Socket',
    },

    packages=find_packages()
)
