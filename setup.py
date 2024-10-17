from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
  """
  This fuction will return a list of requirements
  """
  requirements=[]
  with open(file_path) as file_obj:
    requirements=file_obj.readlines()
    requirements=[req.replace("\n", "") for req in requirements]
    if HYPHEN_E_DOT in requirements:
      requirements.remove(HYPHEN_E_DOT)
  return requirements
  try:
    with open(file, 'r') as f:
      return f.read().splitlines()
  except FileNotFoundError:
    print(f"Error: {file} not found.")
    return []
  except Exception as e:
    print(f"An error occurred while reading {file}: {e}")
    return []

try:
    setup(
        name='mproject',
        version='0.0.1',
        author='Timothy Kimutai',
        author_email='timkilichemursoi@gmail.com',
        packages=find_packages(),
        install_requires=get_requirements('requirements.txt')
    )
except Exception as e:
    print(f"Setup failed: {e}")