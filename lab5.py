def cat_greeting(word):
    print(f'cat says {word}')
    cat_greeting("meow")

   # step2
def generate_superhero_power(speed):
    name = "josue"
    power = "speed"
    print(f"{name} s power is {power}")

   
   #step 3
def generate_superhero_power1():
    power = "speed"
    return power
print(generate_superhero_power1())

#step 4
def generate_superhero_power2(user_name, super_power):
    message = user_name + "has the power of " + super_power + "!"
    return message 

print(generate_superhero_power2("josue", "invisibility"))


#step 5
def cat_greeting_loop():
    for i in range(5):
        print(f'the cat says {"meow"}')

        cat_greeting_loop("meow")
        greeting = "meow"
    
    #step6
    def generate_multiple_powers(powers):
        for i in powers:
            print(i)

powers_test = ["teleport","speed","flying"]
