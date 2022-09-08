# To create a dictionary we need key and value pairs.
# First we need a variable and leater on curly braces{} inside these braces need to write key and values of pairs with the separation of (:) after this at the end have to write a quma(,) and all the key and value pairs should inside the double quotes or string
# following is one example of dictonary

python_dictionary = {
    "Bug" : "An error in a program that prevents the program from running as expected.",
    "Function":"A piece of code that you can easily call over and over again.",

}

#Retrieving items from dictionary.
# print(python_dictionary["Bug"])

# Adding new items to dictionary.
python_dictionary["Loop"] = "The action of doing something over and over again."

# Checking items in dictionary
# print(python_dictionary)

# Create an empty dictonary
empty_dictionary = {}

# Wipe an existing dictionary
# python_dictionary = {}
# print(python_dictionary)

# Edit an item in a dictionary
python_dictionary["Bug"] = "A moth in your computer."

# print(python_dictionary)

# Loop through a dictionary

for key in python_dictionary:
    print(key)
    print(python_dictionary[key])


