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

    def insertIntoDB(self, tableName, columnNames, listOfListOfValues):
        #note this function is intended for bulk entry of data. It may be worth while to create another function that
        #deals solely with single inserts or make it an argument for this function.

        names = "("
        for n in columnNames:
            names += n + ','
        names = names[:-1] + ') '
        sql = "INSERT INTO " + tableName + names + " VALUES "

        vals = ""
        for list in listOfListOfValues:
            vals += "("
            for v in list:
                vals += str(v) + ','
            vals = vals[:-1] + '),'
        sql = sql[:-1] + vals[:-1] + ';'
        self.executeSQL(sql)

    def executeSQL(self, sql):
        if self.debug:
            print(sql)
        else:
            self.con.cursor().execute(sql)
            self.con.commit()
