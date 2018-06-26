#What will be the output of the following code:
# Program to depict Raising Exception

try:
    raise NameError("Hi there")  # Raise Error
except NameError:
    print("An exception")
    raise  # To determine whether the exception was raised or not



#following will the output of the given program :-

# raise NameError("Hi there")  # Raise Error
# NameError: Hi there