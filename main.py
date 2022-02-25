import math


def getIntVal(var):
    while True:
        try:
            val = int(input("Enter " + var + " : "))
            break
        except ValueError:
            print("Please type an integer only. ")
            continue
    return val


def discriminantCheck(a, b, c):
    val = (b * b) - 4 * a * c
    if val > 0:
        return 2
    elif val == 0:
        return 1
    elif val < 0:
        return 0


def isZeroDenominator(a):
    if a == 0:
        return True


def quadraticPlus(a, b, c):
    val = (-b + math.sqrt((b * b) - 4 * a * c)) / (2 * a)
    return val


def quadraticMinus(a, b, c):
    val = (-b - math.sqrt((b * b) - 4 * a * c)) / (2 * a)
    return val


def driver():
    print("This is a Quadratic Equation calculator.")
    varA = getIntVal("a")
    if isZeroDenominator(varA):
        return "Denominator is zero. Try again"

    varB = getIntVal("b")
    varC = getIntVal("c")

    if discriminantCheck(varA, varB, varC) == 2:
        resultPlus = quadraticPlus(varA, varB, varC)
        resultMinus = quadraticMinus(varA, varB, varC)
        print("There are two solutions.")
        print("First solution is : " + str(resultPlus))
        print("Second solution is: " + str(resultMinus))
    elif discriminantCheck(varA, varB, varC) == 1:
        print("There is one solution.")
        print("The solution is : " + str(quadraticMinus(varA, varB, varC)))
    elif discriminantCheck(varA, varB, varC) == 0:
        print("There are no real solutions.")


print(driver())
