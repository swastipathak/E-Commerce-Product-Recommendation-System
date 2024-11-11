from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirments(file_path: str) -> List[str]:
    requirments = []
    with open(file_path) as file_obj:
        requirments = file_obj.readlines()
        requirments = [req.replace("\n", "") for req in requirments]

        if HYPEN_E_DOT in requirments:
            requirments.remove(HYPEN_E_DOT)
    
    return requirments

setup(
    name='ecommerce_ml_project',
    version='0.0.1',
    author='Swasti Pathak',
    author_email='swasti20pathak@gmail.com',
    packages=find_packages(),
    install_requires=get_requirments('requirments.txt')  # Ensure this matches your actual requirments file
)
