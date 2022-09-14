'''
 we have learn couple things about function frist we seen that how to create a simple function 
 def my_function():
     # Do this 
     # Then do this 
     # Finally do this 
 my_function() #calling the funtion

# function with inputs

  def my_function(something):
       # Do this with something
      # Then do this 
      # Finally do this 
 my_function(213) #calling the funtion

# Functions with Outputs

def my_function():
    result = 5 * 2
    return result

output= my_function()
print(output)

# Some other exmples are below 👇🏼
'''
def format_name(f_name,l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

print(format_name("pradip","SABLE"))