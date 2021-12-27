def getNthElement(num):
    """
    Recursive function
    For n <= 0 ==> a(n) = 0
    For n > 0  ==> a(n) = 2a(n-1) + n
    """
    if num <= 1:
        return 1
    else:
        return 2 * getNthElement(num - 1) + num

def getCharByIndex(id, uppercase=False):
    """Helper Function for converting id to character"""
    if not type(id) is int:
        raise TypeError("Only integers are allowed")

    if id < 1 or id > 26:
        raise Exception("Boundary error: parameter should be between 1 to 26")

    charater = chr(id  + 96)
    if(uppercase):
        return charater.upper()
    else:
        return charater

def getIndexByChar(char):
    """Helper Function for converting character to id"""
    if not type(char) is str:
        raise TypeError("Only character is allowed")
    return ord(char.lower()) - 96

def getNumber(char):
    """Get Number to a given letter"""
    if not type(char) is str:
        raise print("Only character is allowed")

    if (len(char) is not 1):
        raise    print("Pass a character")

    value = getNthElement(getIndexByChar(char))
    print(f"The value of '{char}' is {value} \n\n")
    return value

def getWordValue(string):
    """Sum of Number from a given word"""
    if not type(string) is str:
        raise print("Only strings are allowed")

    sum = 0

    for char in string:
        sum += getNthElement(getIndexByChar(char))

    print(f"The value of '{string}' is {sum} \n\n")
    return sum

def createDict():
    """Helper function for getting the series in dictionary"""
    temp = {}

    for i in range(1,27):
        char = getCharByIndex(i, True)
        temp[getNthElement(i)] = char

    return temp

# To find Closest number in a list
def closest(lst, K):
    return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))]

def getWordFromNumber(num):
    """Get a Shorest string of letters from a given large number"""
    if not type(num) is int:
        raise TypeError("Only integers are allowed")

    hashmap = createDict()
    print(hashmap)
    seriesValues = list(hashmap)

    string = ""
    while num > 0:
        closestInSeries = closest(seriesValues, num)
        print(hashmap[closestInSeries])
        num -= closestInSeries
        string += hashmap[closestInSeries]

    print(f"The shorest string for '{num}' is {string}\n\n")
    return string

def main():
    while True:
        print("1. Get Number to a given letter")
        print("2. Sum of Number from a given word")
        print("3. Get a Shorest string of letters from a given large number")

        execute = input("Enter the corresponding number to execute the above function: ")

        if(execute == "1"):
            getNumber(input("Enter a character: "))
        elif (execute == "2"):
            getWordValue(input("Enter a string: "))
        elif(execute == "3"):
            num = int(input("Enter a large integer: "))
            getWordFromNumber(num)
        else:
            print("Please enter a valid input")

main()