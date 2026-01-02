from setuptools import find_packages, setup
from typing import list

def get_requirements(file_path:str)->list[str]:
    '''
    This function will return the list of requirements
    '''
    requirements=[]
    with open(requirements.txt) as f:
        requirements=f.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        
        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements

setup(
    name="ml_project",
    version="0.1",
    author="Apana Rajawat",
    author_email="appy_ms@outlook.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
    )