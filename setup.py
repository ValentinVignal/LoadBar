import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="load-bar",
    version="0.0.7",
    author="Valentin Vignal",
    license='MIT',
    author_email="valentin.vignal.dev@outlook.fr",
    description="Python Librairy for a loading bar in the console",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ValentinVignal/LoadBar",
    packages=['loadbar'],
    install_requires=[
        'termcolor'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
