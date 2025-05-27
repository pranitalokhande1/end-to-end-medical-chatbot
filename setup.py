# from setuptools import find_packages,setup

# setup(
#     name='generative ai project',
#     version='0.0.0',
#     author='pranita',
#     author_email='pranital571@gmail.com',
#     packages=find_packages(),
#     install_requires=[]
# )
from setuptools import setup, find_packages

setup(
    name='medibot',
    version='0.1.0',
    author='Pranita',
    author_email='pranital571@gmail.com',
    packages=find_packages(),  # or find_packages(where="src") if using a src folder
    include_package_data=True,
    zip_safe=False,
)
