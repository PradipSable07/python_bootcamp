#Creating a Function 
'''
def function_name():
    Do this
    Then do this 
    Finally do this    
'''
#calling a function
# function_name() 
# below is the example of function
# def greet():
#     print("Hello")
#     print("How do you do?")
#     print("Are you free Tomorrow?")
    
# greet()

# Creating a Function with input

'''
def function_name(declear a variable or parameter):
    Do this input or decleared variable or parameter.
    Then do this 
    Finally do this
    
#  calling a function()
 function_name(input or Declare a variable value or argument)
'''

# Functions that allows for input 
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}? ")

# greet_with_name("Pradip_Sable")
    
# Functions with more than one parameter 


def greet_with(name,locations):
    print(f"Hello {name}")
    print(f"What is it like in {locations}?")
    
# greet_with("Pradip Sable","India")
# vs
# greet_with("India","Pradip Sable")

# Function with keyword arguments
greet_with(locations="India",name="vasudev")


    