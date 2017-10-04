from setuptools import setup

setup(
    name='Lego IR Blaster',
    version='0.2',
    long_description=__doc__,
    packages=['legoirblaster'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask']
)
