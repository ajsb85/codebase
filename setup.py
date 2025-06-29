from setuptools import setup, find_packages
import os
print(os.path.dirname(__file__))
setup(
    name="codebase",
    version="1.0.0",
    packages=find_packages(),
    install_requires=["python-docx","gitpython"],
    entry_points={
        "console_scripts": [
            "codebase = codebase.codebase:main",
        ]
    },
    author="Alexander Salas Bastidas",
    author_email="a.salas@ieee.org",
    description="A Python package to convert codebase to text",
    license="MIT",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    download_url="https://github.com/ajsb85/codebase/archive/refs/tags/1.0.7.tar.gz",
    long_description_content_type="text/markdown",
    keywords = ["codebase, code conversion, text conversion, folder structure, file contents, text extraction, document conversion, Python package, GitHub repository, command-line tool, code analysis, file parsing, code documentation, formatting preservation, readability"],
    
    url="https://github.com/ajsb85/codebase",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
)
