import setuptools
import codecs
import os

with open("README.rst", "r", encoding="utf-8") as fh:
    long_description = fh.read()


# Setting up
setuptools.setup(
    name="twitterpost",
    version="0.0.1",
    author="vLeeH",
    author_email="vitorlee.tech@gmail.com",
    description="A library that search and do posts in Twitter.",
    long_description_content_type="text/markdown",
    long_description=long_description,
    url="https://github.com/vLeeH/twitterpost",
    install_requires=['oauth2', 'oauthlib'] ,
    keywords=['python', 'twitter', 'posts'], 
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.8',
        "License :: OSI Approved :: MIT License",
        'Natural Language :: English',
        "Operating System :: OS Independent",
        'Topic :: Utilities',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
    , packages=setuptools.find_packages(),
    python_requires='>=3.7',
)