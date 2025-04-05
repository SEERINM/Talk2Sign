import setuptools

setuptools.setup(
    name='Talk2Sign',
    version='0.1.0',
    description='Python project',
    author='SEERIN M',
    author_email='seerin3514@gmail.com',
    url='https://github.com/SEERINM/Talk2Sign.git',
    packages=setuptools.find_packages(),
    setup_requires=['nltk', 'joblib','click','regex','sqlparse','setuptools'],
)
