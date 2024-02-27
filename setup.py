from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str) -> List[str]:
    '''
    this function will return the list of requiremtns 
    '''

# here setup will have all the parameters that are required
# consider this a metadata information about the entire project 
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements        

setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'Muhammad Uzair Awna',
    author_email = 'uzairawwan@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')

)