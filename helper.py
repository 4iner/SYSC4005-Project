import math
import random


# p = 1-e^(-1*lambda*x)

# 1 - p = e ^ (-1* lambda * x)
# ln(1-p) = -1 * lambda * x
# ln(1-p)/(-1 * lambda) = x

def getValXP(mean):
    lam = 1/mean
    p = random.random()
    x = math.log(1 - p) / (-1 * lam)
    return x

# p = 1 - e^(-1 * (x/alpha)^beta )
# 1 - p = e^(-1 * (x/alpha)^beta )
# -1 * ln(1 - p) = (x/alpha)^beta
# ln (-1 * ln(1 - p)) / beta = ln(x / alpha)
# -1 * ln (1 - p) / beta = x / alpha
# alpha/beta * -1 * ln(1 - p) = x

def getValWei(a, b):
    p = random.random()
    x = a/b * -1 * math.log(1-p)
    return x



