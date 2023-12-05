from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='pipeyaml',
    version='0.1.1',
    description='Access YAML data in the CLI.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/skovranek/yaml_pipe',
    author='Matt Skovranek',
    author_email='mattjskov@gmail.com',
    license='GPL-3.0',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
    ],
    keywords='yaml json utility extract autocomplete',
    packages=find_packages(['yaml_pipe', 'yaml_pipe.*']),
    install_requires=[
        'argcomplete==3.1.6',
        'pyparsing==3.1.1',
        'PyYAML==6.0.1',
        'ruamel.yaml==0.17.35',
        'ruamel.yaml.clib==0.2.8'
    ],
    python_requires='>=3.12.0',
    entry_points={
        'console_scripts': ['yaml_pipe=yaml_pipe.main:main']
    }
)
