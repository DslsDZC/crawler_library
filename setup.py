from setuptools import setup, find_packages

setup(
    name="crawler_library",
    version="2.0.0",
    author="DslsDZC",
    author_email="dsls.dzc@gmail.com",
    description="Advanced Web Crawler Library",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/DslsDZC/crawler_library",
    packages=find_packages(),
    install_requires=[
        "requests>=2.28.1",
        "beautifulsoup4>=4.11.1",
        "pyyaml>=6.0"
    ],
    entry_points={
        "console_scripts": [
            "crawler_library-cli = crawler.cli:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.8',
    include_package_data=True
)
