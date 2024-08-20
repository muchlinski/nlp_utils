import setuptools

with open('README.md', 'r') as file:
    long_description = file.read()

setuptools.setup(
    name='nlp_utils',
    version='0.0.4',
    author='Maciej M',
    description='This is NLP preprocessing package with common tools',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: MIT License',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.9'
)