"""Main module."""

from typing import Optional
import sqlalchemy
import logging
import datetime
from sqlalchemy.engine import Engine
from sqlalchemy.orm.session import Session

type_str = type('str')
type_datetime = type(datetime.datetime.now())
type_int = type(1)
type_float = type(1.0)
type_None = type(None)


def convert_to_string(record):
    res = []
    for item in record:
        itype = type(item)

        if itype == type_None:
            res.append('NULL')
        elif itype == type_str:
            res.append(f'"{item}"')
        elif itype == type_datetime:
            res.append(f'"{str(item)}"')
        else:
            res.append(str(item))

    return ','.join(res)


class TablesCopier():
    '''
    provide function to copy the specified tables from src db to dest db
    '''

    def __init__(self, engine_src: Engine, session_src: Session, engine_dest: Engine, session_dest: Session):
        self._engine_src: Engine = engine_src
        self._session_src: Session = session_src
        self._engine_dest: Engine = engine_dest
        self._session_dest: Session = session_dest

    def run(self, tables: list = None):
        '''
        if tables is none, it means coping all tables
        '''
        if not tables:
            tables = self._get_all_src_tables()

        self._drop_dest_tables(tables)

        self._setup_dest_tables(tables)

        self._copy_tables(tables)

    def _get_all_src_tables(self):
        logging.info('get all tables on src db')

        tables = self._engine_src.table_names()

        logging.info(tables)

        return tables

    def _drop_dest_tables(self, tables: list):
        logging.info('drop the specified tables on dest db')

        for one_table in tables:
            self._drop_one_dest_table(one_table)

    def _drop_one_dest_table(self, one_table: str):
        logging.info(f'dropping one table({one_table})')

        session = self._session_dest

        session.execute('SET FOREIGN_KEY_CHECKS = 0;')

        res = session.execute(f'DROP TABLE IF EXISTS {one_table} CASCADE;')
        logging.debug(res)
        session.commit()

        session.execute('SET FOREIGN_KEY_CHECKS = 1;')

    def _setup_dest_tables(self, tables: list):
        logging.info('setup tables schema on dest db')

        for one_table in tables:
            self._setup_one_dest_table(one_table)

    def _setup_one_dest_table(self, one_table: str):
        logging.info(f'setup one tablein dest db')

        engine_src = self._engine_src
        engine_dest = self._engine_dest

        md = sqlalchemy.MetaData()
        table = sqlalchemy.Table(one_table, md, autoload=True, autoload_with=engine_src)
        logging.info(table.c)

        md.create_all(bind=engine_dest)

    def _copy_tables(self, tables: list):
        logging.info('copy tables data from src db to dest db')

        for one_table in tables:
            logging.info(f'inserting data into table {one_table}')

            cnt = 0
            res = self._read_table_data_from_src(one_table)
            for one_row in res:
                cnt += 1
                self._save_table_row_into_dest(one_table, one_row)

            logging.info(f'inserted ({cnt}) data into dest table ({one_table})')

    def _read_table_data_from_src(self, one_table: str):
        session = self._session_src

        read_sql = f'select * from {one_table}'
        rp = session.execute(read_sql)
        res = rp.fetchall()

        return res

    def _save_table_row_into_dest(self, one_table: str, one_row):
        session = self._session_dest
        valstr = convert_to_string(one_row)

        try:
            insert_sql = f'insert into {one_table} values({valstr})'
            session.execute(insert_sql)
            session.commit()
            logging.debug(f'Inserted OK: {valstr}')
        except Exception:
            logging.debug(f'Inserted Failed: {valstr}')

