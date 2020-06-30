#printing welcome on screen
print("*******************************************************************")
print("                                 WELCOME                           ")
print("*******************************************************************")
#displaying options 
print("FOR EACH QUESTION YOU GAIN 1 POINT")
print("press any other number to quit")
question=int(input("press 1 to display question"))
#s_count is for counting scores
count=0
if (question==1):
    print("LEVEL 1")
    #displaying questions
    print("Q. Which animal symbolizes good luck in Europe?")
    print("1. ladybug")
    print("2. Dog")
    print("3. Giraffe")
    print("4. Cow")
    a1=int(input("ENTER YOUR ANSWER NUMBER"))
    if (a1==1):
        count+=1
        print("WOW, IT IS A CORRECT ANSWER")
    else:
        print("OPPS!! SORRY")
    print("Q. Which cartoon character lives in a pineapple under the sea?")
    print("1. Oggie")
    print("2. OSWALD")
    print("3. Noddy")
    print("4. Spongebob Squarepants")
    a2=int(input("ENTER YOUR ANSWER NUMBER"))
    if (a2==4):
        count+=1
        print("WOW, IT IS A CORRECT ANSWER")
    else:
        print("OPPS!! SORRY")
    #printing total score
    print("your total score is ",count)
    #for correct answer
    print("press any other number to exit")
    correct=int(input("press 2 for displaying correct answer"))
    
    if (correct==2):
        print("Q. Which animal symbolizes good luck in Europe?")
        print("ANSWER = LADYBUG")
        print("Q. Which cartoon character lives in a pineapple under the sea?")
        print("ANSWER = SPONGEBOB SQUAREPANTS")
    
    
            
else:
    print("THANKS FOR BEING HERE")
