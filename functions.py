#here we will play with functions

#Single argument function
def print_one_agr(arg):
    print(arg)

#Two argument functions
def print_two_args(arg1 , arg2):
    print(f"First argument is {arg1} and second is {arg2}")

#argument array functions
def print_all_args(*args):
    for arg in args:
        print(arg)

#argument dictionary functions
def print_all_args_1(**args):
    default = {"count" : 4 , "seat" : 6}
    default.update(args)
    print(default)

#optional parameter
def print_optional(arg = ""):
    if arg == "":
        print("argument is not passes")
    else:
        print(f"the passes argument is {arg}")


print("Calling print_one_agr")
print_one_agr("Anubrij")

print("Calling print_two_args")
print_two_args("Sudha" , "Anubrij")

print("Calling *args ")
print_all_args("first" , "second" , "third" , 4 , 5, 6 ,"seven")

print("Calling optional without param")
print_optional()

print("Calling optional with parameter")
print_optional("Anubrij Chandra")

#Let work on some return type functions
def arthmetics(num1 , num2 , ope = "+"):
    if ope == "+":
        return num1 + num2
    elif ope == "*":
        return num1 * num2
    elif ope == "/":
        return num1 / num2
    elif ope == "-":
        return num1 - num2
    elif ope == "%":
        return num1 % num2
    else:
        return "No operation defined"

def multiRetutnFunc():
    return 1 , "a" , 2.35 , True , False , [3,4,5,6,7]

print(f"Arthmentics {arthmetics(1,2,'*')}")
print(f"Arthmentics {arthmetics(1,2,'')}")

a1 , a2 , a3 , a4 , a5, a6 = multiRetutnFunc()
print(a1 , a2 , a3, a4, a5, a6)
