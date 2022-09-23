# # # # # # # # # # # # # # # # # # # # # # # # / Scope \ # # # # # # # # # # # # # # # # # # # # # # # # # 
'''
enemies = 1 
def increase_enemies():
    enemies = 3
    print(f"enemies inside function: {enemies} ")
    print("Local Scope")


increase_enemies()
print(f"enemies inside function: {enemies} ")
print("Global Scope")
'''

# # # # # # # # # # # # # # # # # # # # # # #  / Local Scope \ # # # # # # # # # # # # # # # # # # # # # # #
# local scope means you have created a variable inside a function and you can access that variable inside that only.
'''
def drink_postion():
    potion_strenght = 5
    print(potion_strenght) 
    
drink_postion()
'''

# # # # # # # # # # # # # # # # # # # # # # #  / Global Scope \ # # # # # # # # # # # # # # # # # # # # # # # Global Scope means you have created a variable outside a function and you can accesss that variable inside a function and outside a function.
'''
player_helth = 10

def drink_postion():
    potion_strenght = 5
    print(player_helth) 
    
drink_postion()

print(player_helth)
'''
# # # # # # # # # # # # # # # # # # # # # # #  / Block Scope \ # # # # # # # # # # # # # # # # # # # # # # 
# Does python have block scope?
# No python do not have Block scope concept like c++, Java 

# # # # # # # # # # # # # # # # # # #  / Moddying Global Scope \ # # # # # # # # # # # # # # # # # # # # # #
'''
enemies = "Alien"

def increase_enemies():
    global enemies # without this line of code we can not modify something that is global within a local scope
    enemies += " Zombie"
    print(f"enemies inside function: {enemies} ")
    
increase_enemies()
print(f"enemies inside function: {enemies} ")
'''

# # # # # # # # # # # # # # # # # # #  / Global Constants \ # # # # # # # # # # # # # # # # # # # # # #
# we can make global constants by using the uppercase letters and we can not change this inside a funtion
'''
PI = 3.14159
URL ="http://www.facebook.com"
GITHUB_HANDLE = "PRADIP9193"
'''