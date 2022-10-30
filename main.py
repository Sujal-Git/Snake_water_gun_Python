import random

#DeclaringMethods

def cpu_input():  #Will return r or p or s as Cpu input
    inp_choice=["s","w","g"]
    return inp_choice[random.randint(0,2)]

def start():      #entry of the game
    print("Snake water Gun")
    print("There will be 5 Rounds")
    print("------------------\n")
  

def game_logic():     #Logic of the game
    user_score=0
    comp_score=0
    tie=0
    start()
    for rounds in range(1,6):
          comp_inp=cpu_input()
          user_input=input("Enter your Input (s or w or g)? : ")
          
          if(user_input=="s" and comp_inp=="w"):
            print("You win.")
            user_score=user_score+1

          elif(user_input=="w" and comp_inp=="g"):
            print("You win.")
            user_score=user_score+1

          elif(user_input=="g" and comp_inp=="s"):
            print("You win.")
            user_score=user_score+1

          elif(user_input=="s" and comp_inp=="g"):
            print("Computer win")
            comp_score=comp_score+1

          elif(user_input=="w" and comp_inp=="s"):
            print("Computer win")
            comp_score=comp_score+1

          elif(user_input=="g" and comp_inp=="w"):
            print("Computer win")
            comp_score=comp_score+1
          
          else:
            print("Tie")
            tie=tie+1
    
    if(comp_score>user_score):
      winner="Won By Computer"
    elif(user_score>comp_score):
      winner="Won By You"
    else:
      winner="Tie"
    
    #scoreboard which will show inner after completing all rounds
    print("---Scoreboard---")
    print("----------------")
    print(f"--Its= >> {winner}")
    print(f"Comp Score: {comp_score}")
    print(f"Your Score: {user_score}")
    print(f"Ties      : {tie}")
    

game_logic(); #calling our main function
   

    


        









