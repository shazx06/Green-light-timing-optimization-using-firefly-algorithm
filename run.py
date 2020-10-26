from FireflyAlgorithm import *


def Fun(D, sol):
    val = 0.0
    for i in range(D):
        val = val + sol[i] * sol[i]
    return val


Algorithm = FireflyAlgorithm(10, 7, 100, 0.5, 0.2, 1.0, 120, 180, Fun)
Best = Algorithm.Run()

print (Best)
