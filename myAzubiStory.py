"""
Azubi Academy Lab session
Week 2, Python intro
NB: All Contributions gladly welcomed!
Task: Take imputs and put together an azubi experinece story
extra: error handling and saving text generated
"""


# Get name and salutation
name = input("enter your name: ")
message = """! Welcome to Azubi experience storyteller\n 
We would help you put together your Azubi story by giving us
some inputs"""
print("Hello", name, message)


# Get inputs for story
program = input("what program are you enrolled in? ")
excitement_grade = input("how excited are you about the program? ")
while True:
    try:
        exp_years = int(input("How many years of experience in tech do you have? "))
        break
    except ValueError:
        print("Enter a number. 0 for no years of experience")

match exp_years:
    case 0:
        exp_years = "no working experience"
    case 1:
        exp_years = "a 1 year experience"
    case _:
        exp_years = "about " + str(exp_years) + " years of experience"
        
topics = input ("what have you learnt so far? to ...(seperate with commas) ")
learning_exp = input("in one word, how is the learning experience: ")

# The azubi story 

story = f"""Hello, my name is {name} and I am {excitement_grade} \
excited to be part of {program} summer cohort. I have {exp_years} \
in tech and hoping to learn more with Azubi Africa. So far,\
 I have learn about {topics} and it has been {learning_exp}"""
print("\nHere's your story\n")

# Output story
print(story)

# Save story to txt
while True:
    try:
        response = input("Do you wanna save story as txt file?(y or n) ")
        if response.lower() == 'y':
            # Hardcoded path, could use os.path.join()
            with open("D:/azubi/test/myAzubiStory.txt", 'w') as f:
                f.write(story)
            break
        elif response.lower() == 'n':
            print("\nThanks for using Story teller")
            break
        
        print("Enter Valid Response")
    except:
        print("Watch your keys")
