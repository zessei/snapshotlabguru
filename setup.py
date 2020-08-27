from setuptools import setup

setup(
    name='snapshotalyzer-3000',
    version='0.1',
    author="Myself",
    auhor_email="myemail@email.place",
    description="cloud guru python lesson for managing EC2 instances and snapshots",
    license="Open",
    packages=['shotty'],
    url="https://github.com/zessei/snapshotlabguru",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',
)
