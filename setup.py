from setuptools import setup

setup(
    name='table_of_contents',
    install_requires=[
        'pyramid',
        'pyramid_chameleon'
    ],
    entry_points="""\
        [paste.app_factory]
        main = table_of_contents:main
        """,
)
