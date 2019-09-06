import random
import time
# Magic 8 Ball

#     Simulate a magic 8-ball.
#     Allow the user to enter their question. - when the code runs prompt the user that allows them to input a string. 
#     Display an in progress message(i.e. "thinking"). - add a wait? command that shows . .. ... 
#     Create 20 responses, and show a random response. - create 20 responses and have the program return back 1 of the 20 at random.
#     Allow the user to ask another question or quit. 

#     Bonus:
#         Add a gui.
#         It must have a box for users to enter the question.

#         It must have at least 4 buttons:
#             ask
#             clear (the text box)
#             play again
#             quit (this must close the window)


random_response = ["It is certain", "Without a doubt","You may rely on it", "Yes definitely", "It is decidedly so", "As I see it, yes", "Most likely", "Yes", "Outlook good", "Signs point to yes", 
"Reply hazy try again", "Better not tell you now", "Ask again later", "Cannot predict now", "Concentrate and ask again", "Don't count on it", "Outlook not so good", "My sources say no", "Very doubtful", "My reply is no"]

def magic_ball():
    var = input("Ask the Magic 8 Ball a question: ")
    print(".")
    time.sleep(2)
    print("..")
    time.sleep(2)
    print("...")
    time.sleep(2)
    print("still thinking...")
    time.sleep(2)
    print(random.choice(random_response))
    time.sleep(2)
    var2 = input("Would you like to ask another question?")
    
    if var2 == "y" or var2 == "yes":
        return magic_ball()
    
    elif var2 == "n" or var2 == "no":
        print("Thanks for playing! Until next time.")
    elif var2 != "n" or var2 != "no" or var2 != "yes" or var2 != "y":
        print("That isn't a yes or a no. Please try agian")
        return magic_ball()

    
magic_ball()

 
#     return var
# if input == "n" or "no":
#     print("until next time")

#if user input is y or yes, allow the user to ask another question. if the input is n or no display a msg saying until next time. 