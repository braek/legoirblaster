from setuptools import setup

setup(
    name='Lego Train Controller',
    version='0.1',
    long_description=__doc__,
    packages=['legotraincontroller'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask']
)
