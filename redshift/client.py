import psycopg2


class RedShift(object):

    def __init__(self, host, port, database_name, user, password):
        self.connection = psycopg2.connect(dbname=database_name, host=host, port=port, user=user, password=password)

    def execute_query(self):
        pass
