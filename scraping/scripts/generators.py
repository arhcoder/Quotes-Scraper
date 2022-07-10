def myFunction():

    a = 11
    yield a

    a = 22
    yield a

    a = 33
    yield a

    a = 44
    yield a

# myFunction() regresa un iterador...
myFunctionResult = myFunction()
print(myFunctionResult)

print(next(myFunctionResult))
print(next(myFunctionResult))
print(next(myFunctionResult))
print(next(myFunctionResult))