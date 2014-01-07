from sys import exit

def dead(reason):
  print "%s. You're a sucker!" % reason
  
def start():
  print """It was a cold day of January. The year 2014 had just begun.
  At the time, my milkshakes used to bring all the boys to the yard. Damn right it was better than yours.
  You're now in my past. What do you want to do?"""
  
  next = raw_input("NotZork> ")
  if "house" in next or "go in" in next:
    enter_house()
  elif "look around" in next or "explore" in next:
    explore()
  else
    dead("Your head was chopped off by the illusion of your indecision")
    
def enter_house()
  print "You've entered my house. Watch out for the giant pink elephant in the corner"
  next = raw_input("Quick what do you do?> ")
  if "kill" in next or "shoot" in next or "throw" in next:
    win()
  else:
    dead("You're no good at all.")

def explore()
  print "You found a notebook on the ground near the swingset. Must be full of answers don't you think?"
  next = raw_input("your answer is?> ")
  if "yes" in next:
    dead("You just learnt that you are your own grandfather and your cousin is your sister but also your wife.")
  else
    print "You win because I'm bored to death so I'm gonna do something else"
    exit(0)
