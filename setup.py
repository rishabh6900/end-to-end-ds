# Import necessary modules
from setuptools import find_packages, setup  # find_packages: for locating Python packages automatically.
from typing import List  # List: for type hinting to specify the function return type.

# Constant to represent a special entry in requirements file
HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    Function to read and process the requirements from a given file.

    Parameters:
    file_path (str): Path to the requirements file.

    Returns:
    List[str]: A list of package names required for the project.
    '''
    requirements = []
    # Open and read the file line by line
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()  # Read all lines in the file
        requirements = [req.replace("\n", "") for req in requirements]  # Remove newline characters

        # Remove '-e .' if present, as it's specific to editable installs and not an actual requirement
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

# Setup function to configure the package details
setup(
    name='end to end ds',  # Package name
    version='0.0.1',  # Initial version of the package
    author='Rishabh',  # Author's name
    author_email='prajapatirishabh071@gmail.com',  # Author's email
    packages=find_packages(),  # Automatically find and include all packages in the project
    install_requires=get_requirements('requirements.txt')  # List of dependencies retrieved from requirements.txt
)
