import random as r

class Teacher:
    def __init__(self):
        self.ethnicity = 0
        if r.randint(1,10) == 10:
            self.ethnicity = r.randint(13,15)
        elif r.randint(1,3) == 1:
            self.ethnicity = 12
        self.raceSimple = 72
        if self.ethnicity == 12:
            self.raceSimple = 67
        if self.ethnicity == 13:
            self.raceSimple = 71
        if self.ethnicity == 14:
            self.raceSimple = 69
        if self.ethnicity == 15:
            self.raceSimple = 71
        self.sex = 17
        if r.randint(1,2)==1:
            self.sex = 16
        self.motivation = getGaussWithMin1(6,1)
        self.math = getGaussWithMin1(6,1)
        self.eng = getGaussWithMin1(6,1)
        self.ath = getGaussWithMin1(6,1)
        self.SES = getGaussWithMin1(6,1)
        self.family = getGaussWithMin1(6,1)
        self.raceComplex = "NULL"

def getGaussWithMin1(mean, sd):
    ret = r.gauss(mean, sd)
    if ret < 1 : ret = 1
    return int(ret)

def createSQLForInsert(con, s:Student):
    names = ["USER_ID", "ETHNICITY", "RACE_SIMPLE", "RACE_COMPLEX", "SEX", "MOTIVATION", "MATH_APT", "ENG_APT",
             "ATH_APT", "SES", "FAMILY"]
    values = [1, s.ethnicity, s.raceSimple, s.raceComplex, s.sex, s.motivation, s.math, s.eng, s.ath, s.SES, s.family]
    return dbh.insertIntoDB(con, "TEACHER", names, values, False)


def createStudents(n = 1000):
    sql = ""
    for i in range(n):
        t = Teacher()
        sql += createSQLForInsert(con, s)
    dbh.executeSQL(con,sql)
#takes approximately 30 seconds which is too long imho
createStudents()
