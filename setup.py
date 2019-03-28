from setuptools import setup, find_packages

setup(
    name='spyda',
    version='1.0',
    description='Super Python Data Aggregator',
    author="Holden Johnson",
    author_email="horoxix@gmail.com",
    include_package_data=True,
    packages=find_packages(),
    py_modules=['lib'],
    install_requires=[
        'Click',
        'pandas',
        'mysql-connector',
        'psycopg2',
        'plotly',
        'pyquibase'
    ],
    entry_points='''
    [console_scripts]
    spyda=lib.run_cli:cli
    ''',
)
