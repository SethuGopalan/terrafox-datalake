from setuptools import setup, find_packages

setup(
    name="terrafox-datalake", 
    version="0.1.2",
    author="Sethu Gopalan",
    description="Automated connector wrapper for streaming data securely from a private MinIO Data Lake",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "fsspec==2025.3.0",  # Matches Colab's pre-installed environment
        "s3fs==2025.3.0",
        "boto3<1.42",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
