import sys, ast

list_of_argument = sys.argv

def sum(num1, num2):
    return int(num1) + int(num2)


def substract(num1, num2):
    return int(num1) - int(num2)
    

if __name__ == "__main__":
    if list_of_argument[1] == "-sum":
        print(sum(list_of_argument[2], list_of_argument[3]))
    elif list_of_argument[1] == "-substract":
        print(substract(list_of_argument[2], list_of_argument[3]))
    else:
        print("Invalid argument!")