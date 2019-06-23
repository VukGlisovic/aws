import psycopg2


class RedShift(object):

    def __init__(self, host, port, database_name, user, password):
        self.connection = psycopg2.connect(dbname=database_name, host=host, port=port, user=user, password=password)

    def commit(self):
        """Persist changes to database.
        """
        self.connection.commit()

    def rollback(self):
        """Rollback non-comitted changes.
        """
        self.connection.rollback()

    def close_connection(self):
        """Close connection with database.
        """
        self.connection.close()

    def execute_query(self, query):
        """Executes a query without returning anything. This can be
        used to for example create tables or insert data.

        Args:
            query (str):
        """
        try:
            with self.connection.cursor() as cur:
                cur.execute(query)
                self.commit()
        except Exception as e:
            self.rollback()
            raise e

    def get_data(self, query):
        """Executes a query and returns all data of the result of the
        query.

        Args:
            query (str):

        Returns:
            lst
        """
        try:
            with self.connection.cursor() as cur:
                cur.execute(query)
                return cur.fetchall()
        except Exception as e:
            raise e
