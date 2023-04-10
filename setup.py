from setuptools import find_packages, setup

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirement = []
    with open(file_path)


setup(
name = 'mlproject',
version = '0.0.1',
author = 'Shane',
author_email='shanechany0@gmail.com',
packages = find_packages(),
install_requires = get_requirements('requirements.txt')
)