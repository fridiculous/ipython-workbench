import psycopg2
import pandas as pd
import pandas.io.sql as psql
import os
from configparser import SafeConfigParser

parser = SafeConfigParser()
directory = os.path.dirname(__file__)
filename = os.path.join(directory, 'db.conf')
parser.read(filename)


class ConnectToDB(object):

    def __init__(self, db='default'):
        # load config
        self._cur = None
        self._conn = None
        self._database_conn = None
        self._db = db
        self.set_db(db='default')

    def set_db(self, db='default'):
        self._db = db
        try:        
            self._database_conn = {}
            self._database_conn['host'] = parser.get(self._db, 'host')
            self._database_conn['port'] = parser.get(self._db, 'port')
            self._database_conn['dbname'] = parser.get(self._db, 'dbname')
            self._database_conn['user'] = parser.get(self._db, 'user')
            self._database_conn['password'] = parser.get(self._db, 'password')
        except: 
            raise Exception("""not a valid connection.
                please match 'db' to keys in db.conf""")

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
