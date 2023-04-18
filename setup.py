from setuptools import setup, find_packages

setup(
    name='toxic_triggers',
    version='0.1',
    description='full set of words that trigger toxicity',
    author='Xuhui Zhou, Maarten Sap',
    author_email='xuhuiz@cs.cmu.edu',
    url='https://github.com/XuhuiZhou/toxtrig',
    packages=find_packages(),
    install_requires=[
       'setuptools',
       'pandas',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)