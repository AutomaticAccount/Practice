# NOT PRACTICAL TASK #
#This is a self-started exercise to automate the guessing game in the example. The program will make a guess starting from 25 and work its way to the correct answer with step displayed.
#It usually takes 6 step max to reach the correct answer.

import random # import the random library to enable the use of its built-in functions

num = random.randint(1,50) # use the randint (i.e. random integer) function from the random library to get a random integer between 1 and 50
num_guess = 25 #1st guess
num_limits = [0,50] #Set limits
num_history = [] #Record all the attempts

while int(num_guess) != num:

    #Show guess, number of attempts and update list for limits /records
    print(f"{num_guess}")
    num_limits.append(int(num_guess))
    num_history.append(int(num_guess))
    print(f"{len(num_history)}")

    #Record previous guess for later checks on guessing the same number
    num_previous_guess = num_guess
    
    #If the guess is smaller than the answer 
    if num_guess < num:
        
        print(f"Too small! Guess another number from 1 to 50: ")

        #Take previous guess and add the upper limit then divide by two to obtain new guess
        num_guess  = int(num_previous_guess + max(num_limits))/2

        #Remove lower limits to allow the small guess become the new lower limit to accelerate calculation
        num_limits.remove(min(num_limits))

        #To avoid duplicate guesses
        if num_guess == num_previous_guess:
            num_guess += 1
        
    #If the guess is bigger than the answer 
    else:  
        print(f"Too big! Guess another number from 1 to 50: ")

        #Take previous guess and add the lower limit then divide by two to obtain new guess
        num_guess  = int(num_previous_guess + min(num_limits))/2

        #Remove upper limits to allow the guess become the new upper limit to accelerate calculation
        num_limits.remove(max(num_limits))

        #To avoid duplicate guesses
        if num_guess == num_previous_guess:
            num_guess -= 1


    #Stopper in case it runs into infinite loop
    if len(num_history) >=10:
        print(f"You have used all your attempts")

        break
    
#Display result    
num_history.append(int(num_guess))
print(f"Your final guess is:\n {int(num_guess)}")
print(f"The number of guesses:\n {len(num_history)}")
print(f"The number you have gussed\n {num_history}")
print(f"It took you {len(num_history)} attempts to get the correct answer {int(num)}.")