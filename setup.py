from setuptools import setup

setup(
    name='wiki_page_toc',
    install_requires=[
        'pyramid',
        'pyramid_chameleon'
    ],
    entry_points="""\
        [paste.app_factory]
        main = wiki_page_toc:main
        """,
)
