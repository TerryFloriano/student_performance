from setuptools import find_packages, setup
from typing import List 
HYPHEN_E_DOT = "-e ."
def get_requirements(requirement: str) -> List[str]:
    """
    This function will return a list of requirements
    """
    requirements = []
    with open(requirement) as file_obj:
        requirements = file_obj.readlines()
        requirements= [requirement.replace("\n", "") for requirement in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name = "student_performance",
    version = "0.0.1",
    author="Terry",
    author_email="ratombosoaterryfloriano86@gmail.com",
    packages= find_packages(),
    install_requires = get_requirements('requirements.txt')
)