from setuptools import setup, find_packages
with open("README.md", "r") as fh:
    description = fh.read()

setup(
    name='toxicTrig',
    version='0.2',
    description='full set of words that trigger toxicity',
    long_description=description,
    long_description_content_type="text/markdown",
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