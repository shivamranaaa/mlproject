from setuptools import find_packages,setup
from typing import List

HYPER_E_DOT = '-e .'
def get_requirments(file_path:str)->List[str]:
    """
    This funtion will retunr th elist pf requirments
    """

    requirments = []
    with open(file_path) as file_obj:
        requirments = file_obj.readlines()
        requirments = [req.replace("\n","") for req in requirments]

        if HYPER_E_DOT in requirments:
            requirments.remove(HYPER_E_DOT)
    
    return requirments

setup(
    name="mlproject",
    version='0.0.1',
    author="shivam",
    author_email='krishnaik06@gmail.com',
    packages=find_packages(),
    install_requires=get_requirments('C:/Users/shiva/Desktop/mlproject/requirements.txt'),

)