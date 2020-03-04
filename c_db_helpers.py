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

        return sql

    def insertIntoDB(self, connection, tableName, columnNames, listOfListOfValues):
        names = "("
        for n in columnNames:
            names += n + ','
        names = names[:-1] + ') '
        sql = "INSERT INTO " + tableName + names

        for list in listOfListOfValues:
            vals = "("
            for v in list:
                vals += str(v) + ','
            vals[:-1] + '),'
        sql = sql[:-1] + ';'
        print(sql)
        self.executeSQL(connection, sql, self.debug)

    def executeSQL(self, sql):
        if self.debug:
            print(sql)
        else:
            self.con.cursor().execute(sql)
            self.con.commit()
