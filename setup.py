from setuptools import setup,find_packages
from typing import List
HYPEN_E_DOT = "-e ."
def get_require(file_path:str)->List[str]:
    """THIS FUNCTION WILL RETURN THE LIST OF REQUIREMENTS """
    
    requirements =[]
    with open(file_path) as file_obj :
        
        requirements = file_obj.readlines()
        requirements = [ req.replace("\n","")  for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
    return requirements
        
        
          
    


setup(
   name='projectML',
   version='0.0.1',
   description='A useful module',
   author='Anuj ',
   author_email='anujdhyani2@gmail.com',
   packages=find_packages(),
   install_requires = get_require("requirements.txt"), #external packages as dependencies
) 
