from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="gmailagent",
    version="1.0.0",
    author="Product Team",
    author_email="team@example.com",
    description="Gmail automation tool that retrieves emails and exports them to Excel with URL extraction",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/gmailagent",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Communications :: Email",
        "Topic :: Office/Business",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "gmailagent=gmailagent.cli:cli",
        ],
    },
    include_package_data=True,
    keywords="gmail email api automation excel export url-extraction",
)
