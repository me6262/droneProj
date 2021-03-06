from setuptools import setup

setup(
    name='tello_adv_setup',
    version='1.0',
    packages=[''],
    url='',
    license='',
    author='patrick ryan',
    author_email='',
    description='Tello Advanced Project Development Setup ',
    install_requires = [
        # pip install https://github.com/damiafuentes/DJITelloPy/archive/master.zip
        'opencv-python==4.4.0.42',
        'opencv-contrib-python==4.4.0.42',
        'jupyter==1.0.0',
        'imutils==0.5.3',
        'scipy==1.5.2'
    ]

)
