import sys, ast

list_of_argument = sys.argv

def substract(l):
    return l[0] - l[1]
    
def sum(l):
    return l[0] + l[1]

if __name__ == "__main__":
    nv = ast.literal_eval(list_of_argument[2])
    print(list_of_argument)
    if list_of_argument[1] == "-sum":
        print(sum(nv))
    elif list_of_argument[1] == "-substract":
        print(substract(nv))
    else:
        print("Invalid argument!")