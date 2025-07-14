def main():
    x = -1
    print(isPosOrNeg(x))



def isPosOrNeg(num=0):
    if num > 0:
        return "positive"
    elif num < 0:
        return "negative"
    else:
        return "zero"


main()