# input options func
def usr_input():
  
  def err():
    print("An error occurred")
  
  # Introduction lines
  print("\n Just to be clear, you have no life... \n")
  print("All options are CASE SENSITIVE! Besure to type your options in carefully. \n")
  print(" What do you do?", "What are you good for?", "Can you do math?", "Are you an idiot?", "Do you play sports? \n")
  availible_options = ["What do you do?", "What are you good for?", "Can you do math?", "Are you an idiot", "Do you play sports?"]
  
# Variables... yuy
  selected = input("Type in 1 answer...")
  
  # PoC statement
  if selected == "What can you do?":
    print("\n I just take up memory. Plus, if you're talking to me, you have no life.")

  if selected == "What are you good for?":
    print("\n I'm good for taking away your diginity if you talk to me in front of your friends. Of course, this is assuming you have any friends at all.")
    
  if selected == "Can you do math?":
    print("There is no need for me to do math as the shell you're running me on can already do that.")
  
# Executing
usr_input()
