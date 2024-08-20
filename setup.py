from setuptools import setup, find_packages

setup(
    name="netatmo_data",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    entry_points={
        "console_scripts": [
            
        ],
    },
    author="Adeniran Ibrahim",
    author_email="ibademola@yahoo.com",
    description="A library to fetch Netatmo weather data",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/netatmo_data",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)