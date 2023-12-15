n1 = int(input("Enter First Number: "))
n2 = int(input("Enter First Number: "))
n3 = int(input("Enter First Number: "))

def maths():
    print("results is : ", n1 * n3 + n2)
def maths1():
    print("Results is: ", n1 + n2* n3)


def maths2():
    print("Results is: ", n1 * n2 * n3)


def maths4():
    print("Results is: ",(n1 * n2 + n3))

def maths5():
    print("results are: ", n1 + n2 + n3)


if n1 == n2 == n3:
    maths2()
elif n1 != n2 == n3:
    maths1()
elif n1 == n2 != n3:
    maths4()
elif n1 != n2 != n3 and n1 == n3:
    maths()
elif n1 != n2 != n3:
    maths5()



