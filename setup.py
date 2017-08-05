from setuptools import setup

setup(
    name='ExPreSS',
    version='0.1.0',
    description='Exabyte Property Ex(ss)tractor, Sourcer, Serializer class.',
    url='https://github.com/Exabyte-io/exabyte-express',
    author='Exabyte Inc.',
    author_email='info@exabyte.io',
    packages=["express"],
    install_requires=[
        "mock==1.3.0",
        "bunch==1.0.1",
        "numpy==1.10.4",
        "xmltodict==0.9.2",
        "esse==0.1.0",
        "pymatgen==4.2.1"
    ],
    dependency_links=[
        "git+file:///stack/lib/esse@430bf20ce4a0a4002c4f05e67671077406f654c1#egg=esse-0.1.0"
    ],
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development'
    ]
)
