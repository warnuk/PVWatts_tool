from distutils.core import setup

setup(
    name='PVWatts_Tool',
    version='1.1.0',
    url='https://github.com/warnuk/PVWatts_Tool',
    packages=['PVWatts_Tool'],
    license='MIT',
    author='warnuk',
    author_email='warnuk@umich.edu',
    description='A tool that calls on NREL APIs to generate useful information for solar PV resource planning.',
    install_requires = ['pandas', 'requests', 'PyQt5'],
    python_requires = '>=3',


)
