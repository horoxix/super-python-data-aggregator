from setuptools import setup, find_packages

setup(
    name='spyda',
    version='1.2',
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
        'mysql',
        'psycopg2',
        'plotly',
        'pyquibase',
        'requests'
    ],
    entry_points='''
    [console_scripts]
    spyda=lib.run_cli:cli
    ''',
)
