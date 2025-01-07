from setuptools import find_packages,setup
HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->list[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(

name="Insurance_Price_Predition_Project",
version='2.0',
author='Ashok',
author_email='ashokadimmala987@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)