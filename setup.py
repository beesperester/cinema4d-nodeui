import setuptools

import c4dnodeui

setuptools.setup(
    name="c4dnodeui-beesperester",
    version=c4dnodeui.__version__,
    author="Bernhard Esperester",
    author_email="bernhard@esperester.de",
    description="Cinema 4D ui utility library",
    long_description="",
    long_description_content_type="text/markdown",
    url="https://github.com/beesperester/cinema4d-nodeui",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
