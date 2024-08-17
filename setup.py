# With setup.py I can able to build an entire machine learning application package so that I can use it for another projects.
# And also we can deploy it through pipeline so that everyone can use it.

#creating function for get_requirements
from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """
    This function will return the list of requirements,
    excluding any editable installs like '-e .'
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if not req.startswith("-e")]
    return requirements

setup(
    name='ML-Project',
    version='0.0.1',
    author='Sanjay',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
