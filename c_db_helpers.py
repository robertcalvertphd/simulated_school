import mysql.connector as c


class dbh:
    def __init__(self):
        self.con = self.create_connection()
        self.debug = False

    def create_connection(self):
        host = 'localhost'
        database = 'SimulatedSchool'
        user = 'root'
        con = c.connect(host=host, database=database, user=user)
        return con

    def insertIntoDB(self, connection, tableName, columnNames, columnValues, execute=True):
        # for multiple inserts use execute = False, compile the full query and then run.
        #c = connection.cursor()
        names = "("
        for n in columnNames:
            names += n + ','
        names = names[:-1] + ') '
        vals = "VALUES("
        for v in columnValues:
            vals += str(v) + ','
        vals = vals[:-1] + ')'
        sql = "INSERT INTO " + tableName + names + vals + ";"
        if execute:
            self.executeSQL(connection, sql, self.debug)
        else:
            return sql

    def executeSQL(self, sql):
        if self.debug:
            print(sql)
        else:
            self.con.cursor().execute(sql)
            self.con.commit()
