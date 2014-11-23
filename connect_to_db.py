import psycopg2
import pandas as pd
import pandas.io.sql as psql
import os
from configparser import SafeConfigParser

parser = SafeConfigParser()
directory = os.path.dirname(__file__)
filename = os.path.join(directory, 'db_profiles.config')
parser.read(filename)


class ConnectToDB(object):

    def __init__(self, dbtype='postgres'):
        # load config
        self._cur = None
        self._conn = None
        self._database_conn = None
        if dbtype=='postgres':
            self.set_to_postgres()
        elif dbtype=='redshift':
            self.set_to_redshift()
        else:
            raise Exception("not a valid connection. please set 'dbtype', to 'postgres' or 'redshift'")

    def set_to_postgres(self):
        self._database_conn = {}
        self._database_conn['host'] = parser.get('postgres', 'host')
        self._database_conn['port'] = parser.get('postgres', 'port')
        self._database_conn['dbname'] = parser.get('postgres', 'dbname')
        self._database_conn['user'] = parser.get('postgres', 'su_user')
        self._database_conn['password'] = parser.get('postgres', 'su_password')

    def set_to_redshift(self):
        self._database_conn = {}
        self._database_conn['host'] = parser.get('redshift', 'host')
        self._database_conn['port'] = parser.get('redshift', 'port')
        self._database_conn['dbname'] = parser.get('redshift', 'dbname')
        self._database_conn['user'] = parser.get('redshift', 'su_user')
        self._database_conn['password'] = parser.get('redshift', 'su_password')

    def connect(self):
        self._conn = psycopg2.connect(**self._database_conn)
        self._cur = self._conn.cursor()

    def disconnect(self):
        self._cur.close()
        self._conn.close()

    def get_query(self, query):
        self.connect()
        df = psql.read_sql(query, self._conn)
        self.disconnect()
        return df
