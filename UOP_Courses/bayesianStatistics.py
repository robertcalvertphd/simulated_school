import random


def bayesTheorem(A, B, B_given_A):
    return (B_given_A * A) / B


def bayesTheorem_Improved(A, X_given_A, X_given_not_A):
    return (X_given_A * A) / (X_given_A * A + X_given_not_A * (1 - A))


#   scenario:
#   15% of the general population is taller than 2m
#   75% of male basketball players are taller than 2m.
#   .001% of males are professional basketball players
#   what is the probability that a male is a professional basketball player given that he is taller than 2m?

print("Basketball Example:", bayesTheorem(.00001, .15, .75))

# probability patient has disease .1
# probability patient is an addict .05
# probability of disease given being an addict .07

print("addict", bayesTheorem(.1, .05, .07))

print("Breast Cancer:", bayesTheorem_Improved(.01, .9, .08))


# Create a data set then observe A and B and B given A to calculate probability of A given B.

class BayesianScenario:
    def __init__(self, description, A, B, B_A, n=10000):
        self.description = description
        self.A = A
        self.B = B
        self.B_A = B_A
        self.not_A = 1 - self.A
        self.B_not_A = (B - B_A * A) / (1 - A)
        self.observationSet = self.createSet(int(n * .8))
        self.testSet = self.createSet(int(n * .2))
        print("reality check", self.B, " = ", str(B_A*A + self.B_not_A*(1-A)))

    def createSet(self, n):
        ret = []

        for i in range(n):
            A = 0
            B = 0
            if random.random() < self.A: A = 1
            if A:
                if random.random() < self.B_A: B = 1
            else:
                if random.random() < self.B_not_A: B = 1
            ret.append((A, B))
        return ret

    def getX_Y(self, set):
        count_A = 0
        count_B = 0
        count_B_A = 0
        count_A_B = 0
        for item in set:
            A = item[0]
            B = item[1]
            if A:
                count_A += 1
                if B:
                    count_A_B += 1
            if B:
                count_B += 1
                if A:
                    count_B_A += 1
        n = len(set)
        return count_A / n, count_B / n, count_A_B / count_B, count_B_A / count_A


scenario = BayesianScenario("addict", .05, .07, .1)
print(scenario.getX_Y(scenario.observationSet))
