import random
import string
import time
import sys
import inquirer
import numpy as np

# Delay printing
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

#Start of the game
print("HELLO TRIANER PLEASE ENTER YOUR NAME =>");

#Entering of the trainer name

trainer = input("DEAR TRAINER PLEASE ENTER YOUR NAME");
print("Trainer's name is: " + trainer);

#Trainer selects a starter

delay_print(f"\nChoose 1 Pokemon\n")
questions = [
  inquirer.List('pokemon1',
                message="Please Choose Your Starter Pokemon",
                choices=["Venasaur","Charizard","Blastoise"],
            ),
]
answers = inquirer.prompt(questions)
print (answers["pokemon1"])

print("Let's Get Started now your ,First Pokemon is Registered to your Pokedex ")

delay_print(f"\nChoose 1 Pokemon For your Pokedex\n")
questions = [
  inquirer.List('pokemon2',
                message="Please Choose One",
                choices=['Centiscorsh', 'Sizzlepede', 'Raichu', 'Magikarp', 'Gyarados', 'Rayquaza'],
            ),
]
answers = inquirer.prompt(questions)
print (answers["pokemon2"])

delay_print(f"\nYour Prefered Pokemon will be Registered to your Pokedex: " + answers["pokemon2"])

print("Lets have a battle")

#battle data values and opponent decider
opn_trainer = list_values=["DAINTHA","CYNTHIA","LEON","ASH"]
print("Your Opponent is: " + random.choice(list_values))

#opponent pokemon decider
opn_pokemon = delay_print(f"\nOpponent Please Choose 1 Pokemon\n")
questions = [
  inquirer.List('pokemon3',
                message="Please Choose One Pokemon For Battle",
                choices=['Duraladon', 'Snubull', 'Blaziken', 'Boltund'],
            ),
]
answers3 = inquirer.prompt(questions)
print (answers3["pokemon3"])


#Basic Battle 
#your pokemon decider
delay_print(f"\nDefending Player Choose 1 Pokemon\n")
questions = [
  inquirer.List('pokemon4',
                message="Please Choose One Pokemon For Battle",
                choices=['Machamp', 'Rayquaza', 'Gyarados', 'Corviknight'],
            ),
]
answers4 = inquirer.prompt(questions)
print (answers4["pokemon4"])

#countdown for battle
delay_print("Battle Begins in =>")
delay_print(f"\n5\n")
delay_print(f"\n4\n")
delay_print(f"\n3\n")
delay_print(f"\n2\n")
delay_print(f"\n1\n")

print(answers4["pokemon4"], 'vs ', answers3["pokemon3"])
delay_print(f"\nLet The Battle Begin\n")

atk_a = "Super-Punch", 120
opn_atk_a = "Mega-Steel Spike", 190
atk_b = "Earthquake", 80
opn_atk_b = "Headbutt", 40
atk_c = "Dragon-Dance", 130
opn_atk_c = "Fire-Spin", 110
atk_spl_d = "G-Max Hurricane", 240 
opn_atk_spl_d = "Max-Head Bolt", 210

print(f"\nDefending player choose attack\n")
questions = [
  inquirer.List('attack1',
                message="Please Choose One attack For Battle",
                choices=[ atk_a, atk_b, atk_c, atk_spl_d],
            ),
]
result1 = inquirer.prompt(questions)
print (result1["attack1"])

print(f"\nAttacking player choose attack\n")
questions = [
  inquirer.List('attack2',
                message="Please Choose One attack For Battle",
                choices=[ opn_atk_a, opn_atk_b, opn_atk_c, opn_atk_spl_d],
            ),
]
result2 = inquirer.prompt(questions)
print (result2["attack2"])

if result2["attack2"] < result1["attack1"]:
  print("OH! it seems that it was a critical hit, your opponent is unable to battle which means")
  print("----VICTORY----")

elif result2["attack2"] == result1["attack1"]:
  print("It is a Tie")

else:
  print("YOU LOST")
  print("----DEAFEAT-----")

delay_print(f"\n...\n")
time.sleep(0.2)
delay_print(f"\n..\n")
time.sleep(0.3)
delay_print(f"\n.\n")

time.sleep(3)

#outro 
print("PLEASE TYPE YOUR REWIEWS");
input();
print("THANKS FOR YOUR REWIEWS");
print("Thanks for playing: " + trainer);
print("See you Next time");


 
