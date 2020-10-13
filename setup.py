import setuptools

setuptools.setup(
        name="Little Man Computer",
        author="Olav Aga",
        version="0.3",
        author_email="olavnlaga@gmail.com",
        description="A python interpreter for the Little Man Computer language developed by Peter Higginson",
        packages=setuptools.find_packages(),
        entry_points={
            'console_scripts': [
                'lmc=lmc.__main__:main'
                ],
            },
        )
