![python_bootcamp](https://socialify.git.ci/PRADIP9193/python_bootcamp/image?description=1&descriptionEditable=100%20Days%20Challenge%20to%20Self%20&font=Source%20Code%20Pro&language=1&owner=1&pattern=Floating%20Cogs&theme=Dark)

# Python Bootcamp by PRADIP SABLE

![python](https://img.shields.io/badge/python-%23ED8B00.svg?style=for-the-badge&logo=java&logoColor=white)

<hr>

### [Day_01](https://github.com/PRADIP9193/python_bootcamp/tree/main/100_days_python/Day%201)

#### <center> Introduction to the python</center>

<br>

- ##### First install python in your system using this [Link](https://www.python.org/downloads/)

- Then create a file with extension of .py like `namaste.py`, then write inside the file write following line and run the file and see the magic.

```
print("Namaste Python Developer 🥳")
```

In python string looks like inside the double quotes`""` or single quotes `''` like above.

In python the new line can generate by `\n`.

```
print("Namste Python Developer \n Kya kar rahe ho!")
```

we can do string concatination with `+` operator like below,

```
print('Namaste' + "India😍")
```

first we have know about in python there are some common errors that can be `indentation error` or `syntax error` they are generated by user it slef becase it generated by mistakenly.

indentation error makes when we give a more spaces at the begining of the line of code.

And syntaxt error makes when we do wrong program or type invalid statements.

- `input()` fuction we can use these in program for taking input from user like below,

```
input("What is you learning?")
```

- The `print()` function prints the given thing inside it just like above.

- For create a line that cannot be executed by compiler that known as `comments` and that are created by hash tag or pound sign `#` in front of our line. And writing an comment is good practice for future understanding of code or for others to understand.

- Exercise : Write a program that prints the number of characters in a user's name. You might need to Google for a function that calculates the length of a string. [Click here to get answer](https://stackoverflow.com/questions/4967580/how-to-get-the-size-of-a-string-in-python)

i have given you answer below,

```
# normal input function
input("what is your gender?")

# nested input function.
print("hello "+input("what is your name?\n")+"!")

# length function len() to measure the length of answer string.
print(len(input("what is your name?\n")))

```

- #### Variables in Pythons

variables are the entity that hold the data of item or thing that programmer defind. like below,

```
name = 'pradip' 
# names stores the stirng value

age = 22 #
# age stores the integer value

```

- There are some rules to define a variables that are 

    - A variable name must start with a `letter` or the `underscore '_'`  character
    - A variable name cannot start with a `number`
    - A variable name can only contain alpha-numeric characters and underscores `(A-z, 0-9, and _ )`
    - Variable names are `case-sensitive`(age, Age and AGE are three different variables)


- #### Project : Band 🎸 Name Generator:

```
# Create a greeting for your program.
print("Welcome to the Band Name Generator!")

# input for users city
cityName = input("In which city are you grow up?\n")

# input for users pet name
petName = input("What is your pet name?\n")

# concatitation of cityName and petName
print("your band could be " + cityName + petName)

```



### [Day_02](https://github.com/PRADIP9193/python_bootcamp/tree/main/100_days_python/Day%202)

#### <center> Data Types, Type Conversion, Numbers, Operations, f-Strings </center>

- Data Types :-

   - Primitive Data Types :
        - Stirng : it just collection of characters just like ` "Namaste 🙏🏼"` that is inside the single quotes or double quotes.

        - Integer : in integer there are numbers without a decimal `.`,like `0123456789`.

        - Float :  the flot is same like integer but it has a decimal in it. like `pi = 3.14159 # a floating point number`.

        - Boolean : it inclues only truthy or falsy values like `true or false`.

    - Type Error, Type Cheking and Type Conversion :-

        - Type Error : means it is a typing error in the code.
        ``` 
        name = "pradip"
        print(name + 123) # this will give a type error becase the sting and numbers can not concatenate
        ```

        - Type Checking : is done through the ` type()` 
         example : `print(type(name))`.

        - To type conversion of any variable we just do the following thing:
        ``` 
        number = "2343"
        print(type(number)) # it will give you string as a type. 
        # To convert this into number we just have to write
        print(int(number)) # this will give us integer value
        ```
        just like above we can do with all data type conversions

- Mathematical Operation : 
            
    - Addition`+` = 3 + 7
    - Subtraction`-` = 3 - 7
    - Multiplication` * ` = 3 * 7
    - Division`/` = 3 / 7
    - Exponents` ** ` = 3 ** 7

    - PEDMAS = PARENTHESIS `()`, EXPONENTS `**`, MULTIPLICATION `*`, DIVISION `/`, ADDITION `+`, SUBTRACTION `-`.

    ``` print( 3 * (3 + 3) / 3 - 3)
        print( 3 * 3 + 3 / 3 - 3)
        name= input("What is your name?")
        print("Hello, " + name)
        ```

- BMI (Body Mass Index calculator)
```
height = input("enter your height in meter: ")
weight = input("enter your height in kg: ")

bmi = int(weight) / float(height) ** 2
bmi_as_int = int(bmi) // converted to integer
print(bmi)
print(bmi_as_int)
```

- Number Manipulation and F String 
    - To round the number we do ` round()` funtion 
    ex: 
    ``` 
    number = (7/2)
    print(number) # it will give us 4.5 floating number
    print(round(number)) # but in this will git the the 4 as a rounded number.
    ``` 
    insted doing division we can do the flow division like 
    ```
     number = (9 // 2) # in this we will get the 4 
    ```

    - To manipulate the number in python we can do 
    ``` 
    pradipis = 21

    # if we want to add one year to it we can do 
    pradipis += 1

    print(pradipis + "year old") 
    # it will give the result as 22 year old
    ```

    - F-String: <br> What F-sting do ?
     : it simplyfy the sting manipulation let's understand with example.
     ``` 
     # Before we have to convert the any number to string, to concatinate with each other just like 
     number = 123
     Strnum = str(number)
     print("This is number"+ Strnum)
     # Now we can just use
     
     print(f"The is number {number}")
     ```

- Your life in weeks : 
    ```
    age = input("What is your current age?")
    age_as_int = int(age)

    # here number of years are 90 you can choose as you want 
    years_remaining = 90 - age_as_int
    # here we are not traying to do with leap year
    days_remaining = years_remaining * 365
    weeks_remaining = years_remaining * 52
    months_remaining = years_remaining * 12

    massage =f"You have {days_remaining} days, {weeks_remaining} weeks,{months_remaining} months left"

    print(massage)
    ```


- Mini Project : Tip Calculator
    ```
    #If the bill was $150.00, split between 5 people, with 12% tip. 

    #Each person should pay (150.00 / 5) * 1.12 = 33.6
    #Format the result to 2 decimal places = 33.60

    #Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

    #Write your code below this line 👇
    
    print("Welcome to the tip calculator.")
    bill = float(input("What was the total bill? $"))

    tip = int(input("How much tip would you like to give? 10, 12, 15(please do not write % in it just write number: " ))
    people = int (input("How many people to split the bill? "))

    bill_with_tip = (tip/100 * bill) + bill
    print(bill_with_tip)

    bill_per_person = bill_with_tip/people

    print(f"Each person should pay: ${bill_per_person}")

    ```

    

### [Day_03](https://github.com/PRADIP9193/python_bootcamp/tree/main/100_days_python/Day%203)

### [Day_04](https://github.com/PRADIP9193/python_bootcamp/tree/main/100_days_python/Day%204)

### [Day_05](https://github.com/PRADIP9193/python_bootcamp/tree/main/100_days_python/Day%205)

### [Day_06](https://github.com/PRADIP9193/python_bootcamp/tree/main/100_days_python/Day%206)

### [Day_07](https://github.com/PRADIP9193/python_bootcamp/tree/main/100_days_python/Day%207)

#### <center> Hangman Game 👨🏻‍💻</center>
<br>

- Hangman game : It is basically letter guessing game.

The step by step macking of game as follows :

```
                step 01(starting)
                    |
                   \|/
                step 02
                    |
                   \|/
                step 03
                    |
                   \|/
                step 04
                    |
                   \|/
                step 05

```

<br>

### [Day_08](https://github.com/PRADIP9193/python_bootcamp/tree/main/100_days_python/Day%208)

#### <center>Funtions</center>
<br>

- Function : The keyword 'def' introduces a function definition. It must be followed by the function name and the parenthesized() list of formal parameters. The statements that form the body of the function start at the next line, and must be indented.

- Creating a Funtion

- Paint area calculator

- Prime number checker

- Caesar cipher

### [Day_09](https://github.com/PRADIP9193/python_bootcamp/tree/main/100_days_python/Day%209)

#### <center>Dictionaries</center>
<br>

- Retrieving item

- Adding item
- Creating empty dictionary
- Nesting
  - list in dictonary
  - dictonary in dictonary
  - dictonary in list

### [Day_10](https://github.com/PRADIP9193/python_bootcamp/tree/main/100_days_python/Day%2010)

#### <center>Function with Output</center>
<br>

- Function with output means without writing print function return the variable with return statement.
- Function with multiple return statement.
- Days in Month (Exercise)
- Docstrings : Use of docstring when we gives the discription about the function or anything that you want to describe.
- Print vs Return : Printing means displaying a value in a console. To print value in Python. We just call the print() function. Retrun is used to return value from function and exit form it. To return a funciton. We just use the return keyword.
- Created a Calculator with the help of functions and dictonary.

### [Day_11](https://github.com/PRADIP9193/python_bootcamp/tree/main/100_days_python/Day%2011)

#### <center> Black Jack Game </center>

### [Day_12](https://github.com/PRADIP9193/python_bootcamp/tree/main/100_days_python/Day%2012)

#### <center> The Namespaces </center>
<br>
* The Scope
    - The Local Scope
    - The Gloval Scope

- The Number Guessing Game

### [Day_13](https://github.com/PRADIP9193/python_bootcamp/tree/main/100_days_python/Day%2013)

#### <center>Debugging</center>
<br>

- Describe the Problem
- Reproduce the Bug
- Play Computer
- Fixing Errors nad Watching for Red Underliines
- Print is Your Friend
- Using a Debugger
- Ask a Real Friend
- Run Code Often
- Ask StackOverflow
