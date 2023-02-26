========================
SQLAlchemy Tables Copier
========================


.. image:: https://img.shields.io/pypi/v/sqlalchemy_tables_copier.svg
        :target: https://pypi.python.org/pypi/sqlalchemy_tables_copier

.. image:: https://img.shields.io/travis/fanqingsong/sqlalchemy_tables_copier.svg
        :target: https://travis-ci.com/fanqingsong/sqlalchemy_tables_copier

.. image:: https://readthedocs.org/projects/sqlalchemy-tables-copier/badge/?version=latest
        :target: https://sqlalchemy-tables-copier.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status




Copy tables and their data from one db to another db.


* Free software: MIT license
* Documentation: https://sqlalchemy-tables-copier.readthedocs.io.


Usages
--------

.. code-block:: python
   :emphasize-lines: 3,5

    import logging

    from app.db.session import SessionLocal
    from app.db.session import engine

    from app.db.session import SessionLocal_dest
    from app.db.session import engine_dest

    from sqlalchemy_tables_copier import TablesCopier

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)


    def main() -> None:
        logger.info("Before copy data")

        tc = TablesCopier(engine, SessionLocal(), engine_dest, SessionLocal_dest())
        tc.run()

        logger.info("After copy data")


    if __name__ == "__main__":
        main()


Features
--------

* TODO

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
