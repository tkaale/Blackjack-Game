
import os
os.system("")

def print_red(skk): print("\033[91m{}\033[00m" .format(skk))
def print_green(skk): print("\033[92m {}\033[00m" .format(skk))
def print_yellow(skk): print("\033[93m {}\033[00m" .format(skk))
def start():
    print("""
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
                       _/ |                
                      |__/     
    """)

def print_win():
   print_green("\nYou win! Congratulations!")

def print_loose(computer_sum):
    print_red("\nYou lost this game.")
    print_red(f'Dealer have {computer_sum} points.')

def print_blackjack():
    print_red("BLACKJACK")



# hidden_card = """
#  ___  
# |###| 
# | ##| 
# |__#|
# """


# CARDS = {"ace": [""" 
#  ___  
# |A  | 
# | ♠ | 
# |__A| 
# """,
# """
#  ___  
# |A  | 
# | ♦ | 
# |__A| 
# """,
# """
#  ___  
# |A  | 
# | ♥ | 
# |__A|
# """,
# """
#  ___  
# |A  | 
# | ♣ | 
# |__A|
# """], 
# "king": [""" 
#  ___  
# |K  | 
# | ♠ | 
# |__K| 
# """,
# """
#  ___  
# |K  | 
# | ♦ | 
# |__K| 
# """,
# """
#  ___  
# |K  | 
# | ♥ | 
# |__K|
# """,
# """
#  ___  
# |K  | 
# | ♣ | 
# |__K|
# """],
# "queen": [""" 
#  ___  
# |Q  | 
# | ♠ | 
# |__Q| 
# """,
# """
#  ___  
# |Q  | 
# | ♦ | 
# |__Q| 
# """,
# """
#  ___  
# |Q  | 
# | ♥ | 
# |__Q|
# """,
# """
#  ___  
# |Q  | 
# | ♣ | 
# |__Q|
# """],
# "jack": [""" 
#  ___  
# |J  | 
# | ♠ | 
# |__J| 
# """,
# """
#  ___  
# |J  | 
# | ♦ | 
# |__J| 
# """,
# """
#  ___  
# |J  | 
# | ♥ | 
# |__J|
# """,
# """
#  ___  
# |J  | 
# | ♣ | 
# |__J|
# """],
# "ten": [""" 
#  ___  
# |10 | 
# | ♠ | 
# |_10|
# """,
# """
#  ___  
# |10 | 
# | ♦ | 
# |_10|
# """,
# """
#  ___  
# |10 | 
# | ♥ | 
# |_10|
# """,
# """
#  ___  
# |10 | 
# | ♣ | 
# |_10|
# """],
# "nine": [""" 
#  ___  
# |9  | 
# | ♠ | 
# |__9| 
# """,
# """
#  ___  
# |9  | 
# | ♦ | 
# |__9| 
# """,
# """
#  ___  
# |9  | 
# | ♥ | 
# |__9|
# """,
# """
#  ___  
# |9  | 
# | ♣ | 
# |__9|
# """],
# "eight": [""" 
#  ___  
# |8  | 
# | ♠ | 
# |__8| 
# """,
# """
#  ___  
# |8  | 
# | ♦ | 
# |__8| 
# """,
# """
#  ___  
# |8  | 
# | ♥ | 
# |__8|
# """,
# """
#  ___  
# |8  | 
# | ♣ | 
# |__8|
# """],
# "seven": [""" 
#  ___  
# |7  | 
# | ♠ | 
# |__7| 
# """,
# """
#  ___  
# |7  | 
# | ♦ | 
# |__7| 
# """,
# """
#  ___  
# |7  | 
# | ♥ | 
# |__7|
# """,
# """
#  ___  
# |7  | 
# | ♣ | 
# |__7|
# """],
# "six": [""" 
#  ___  
# |6  | 
# | ♠ | 
# |__6| 
# """,
# """
#  ___  
# |6  | 
# | ♦ | 
# |__6| 
# """,
# """
#  ___  
# |6  | 
# | ♥ | 
# |__6|
# """,
# """
#  ___  
# |6  | 
# | ♣ | 
# |__6|
# """],
# "five": [""" 
#  ___  
# |5  | 
# | ♠ | 
# |__5| 
# """,
# """
#  ___  
# |5  | 
# | ♦ | 
# |__5| 
# """,
# """
#  ___  
# |5  | 
# | ♥ | 
# |__5|
# """,
# """
#  ___  
# |5  | 
# | ♣ | 
# |__5|
# """],
# "four": [""" 
#  ___  
# |4  | 
# | ♠ | 
# |__4| 
# """,
# """
#  ___  
# |4  | 
# | ♦ | 
# |__4| 
# """,
# """
#  ___  
# |4  | 
# | ♥ | 
# |__4|
# """,
# """
#  ___  
# |4  | 
# | ♣ | 
# |__4|
# """],
# "three": [""" 
#  ___  
# |3  | 
# | ♠ | 
# |__3| 
# """,
# """
#  ___  
# |3  | 
# | ♦ | 
# |__3| 
# """,
# """
#  ___  
# |3  | 
# | ♥ | 
# |__3|
# """,
# """
#  ___  
# |3  | 
# | ♣ | 
# |__3|
# """],
# "two": [""" 
#  ___  
# |2  | 
# | ♠ | 
# |__2| 
# """,
# """
#  ___  
# |2  | 
# | ♦ | 
# |__2| 
# """,
# """
#  ___  
# |2  | 
# | ♥ | 
# |__2|
# """,
# """
#  ___  
# |2  | 
# | ♣ | 
# |__2|
# """]}
