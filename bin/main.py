err = ("An error occured... Now stop talking to a computer and get a life")

# input options 1 for now
def usr_input():
  print("This is called an intro \n")
  print("All options are CASE SENSITIVE! Besure to type your options in carefully. \n")
  availible_options = print(" What do you do?", "What are you good for?", "Can you do math?", "Are you an idiot?")
  posted_available_options = "What do you do?, What are you good for?"
  print(posted_available_options)
  selected = input("Type in 1 answer...")
  
  if selected == "What do you do?":
    print("\n I just take up memory. Plus, if you're talking to me, you have no life.")
  else:
    print(err)
    
usr_input()
