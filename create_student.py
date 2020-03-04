import c_db_helpers as d
import random as r

dbh = d.dbh()
con = dbh.con

'''
ethnicities

| 12 | NON_HISPANIC_WHITE             | 1    |
| 13 | NATIVE_HAWAIIAN                | 1    |
| 14 | HISPANIC_LATINO                | 1    |
| 15 | PACIFIC_ISLAND_AMERICANS       | 1    |

| 67 | WHITE                          | 9    |
| 68 | BLACK                          | 9    |
| 69 | HISPANIC                       | 9    |
| 70 | ASIAN                          | 9    |
| 71 | HAWAIIAN_OR_PACIFIC_ISLANDER   | 9    |
| 72 | OTHER                          | 9    |

| 16 | FEMALE                         | 2    |
| 17 | MALE                           | 2    |

'''

class Student:
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


    def apply_race_effects(self):
        pass
    def apply_family_effects(self):
        pass

    def apply_ses_effects(self):
        pass

    def take_class(self,teacher, subject):
        pass

    def getStudentValuesForInsert(s):
        values = [1, s.ethnicity, s.raceSimple, s.raceComplex, s.sex, s.motivation, s.math, s.eng, s.ath, s.SES,
                  s.family]
        return values
#    all of the above to be implemented later


def getGaussWithMin1(mean, sd):
    ret = r.gauss(mean, sd)
    if ret < 1 : ret = 1
    return int(ret)

def createInsertCommandForStudents(n = 100):
    values = []
    for i in range(n):
        s = Student()
        values.append(s.getStudentValuesForInsert())

    names = ["USER_ID", "ETHNICITY", "RACE_SIMPLE", "RACE_COMPLEX", "SEX", "MOTIVATION", "MATH_APT", "ENG_APT",
             "ATH_APT", "SES", "FAMILY"]

    return dbh.insertIntoDB(con, "STUDENT", names, values)


#takes approximately 30 seconds which is too long imho

for i in range(1):
    print(i)
    createInsertCommandForStudents()
