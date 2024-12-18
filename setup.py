from setuptools import setup, find_packages

setup(
    name="coe",  # Replace with your package name
    version="0.1.0",
    author="Ruquiya Anjum",
    author_email="anjumruquiya999@example.com",
    description="A simple package for addition",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="",  # Replace with your repo URL
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
