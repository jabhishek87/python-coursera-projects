"""
Program Rock - Spock - Paper - Lizard - Scissors
@author :- Abhishek Jaiswal <ia.malhotra@gmail.com>
@submitted :-  in courseera mini projects
@Written :- October 2013
@codeskulptor link :- http://www.codeskulptor.org/#user20_msJ2BemcCN_1.py

Summary of program

The key idea of this program is to equate the strings "rock", "paper", "scissors", "lizard", "Spock" to numbers as follows:
0 - rock
1 - spock
2 - paper
3 - lizard
4 - scissors
"""
import random
import sys
#
# Function :- Converts Number to Name
# @param :- number[integer]
# @return :- name [string]
#
def number_to_name(number):
    if number == 0:
        return 'rock'
    elif number == 1:
	    return 'spock'
    elif number == 2:
	    return 'paper'
    elif number == 3:
	    return 'lizard'
    elif number == 4:
	    return 'scissors'
    else:
	    return 'undefined'

#
# Function :- Converts Name to Number
# @param :- name [string]
# @return :- number[integer]
#
def name_to_number(name):
    name = name.lower()
    if name == 'rock':
        return 0
    elif name == 'spock':
	    return 1
    elif name == 'paper':
	    return 2
    elif name == 'lizard':
	    return 3
    elif name == 'scissors':
	    return 4
    else:
	    return 'undefined'
#
# Function :- Main function 
# @param :- name [string]
# @return :- none
# @Prints :- 
#
def rpsls(name):
    # convert name to player_number using name_to_number
    player_number = name_to_number(name)

    # genrate a random number for computer between 0 to 4
    comp_number = random.randint(0, 4)

    # convert computer_number to name
    comp_name = number_to_name(comp_number)

    #halting if any wrong inputs is given
    if(player_number == 'undefined'):
        print "wrong input given :- " + name
        sys.exit("Halting Execution")

    # compute difference of player_number and comp_number modulo five
    difference = (player_number - comp_number) % 5
    # use if/elif/else to determine winner
    if difference in [1, 2]:
        winmsg = "Player wins!"
    elif difference == 0:
        winmsg = "Player and computer tie!"
    else:
        winmsg = "Computer wins!"
    # print results
    print " "
    print "Player chooses " + str(name).title()
    print "Computer chooses " + str(comp_name).title()
    print winmsg
    

 
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric