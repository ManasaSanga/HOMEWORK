#Task-1-1-Question 1
Create a program that tells you whether or not you need an umbrella when you leave the house.
The program should:
1. Ask you if it is raining using input()
2. If the input is 'y', it should output 'Take an umbrella'
3. If the input is 'n', it should output 'You don't need an umbrella'

i = input("Please enter your input: ")
if( i.lower() == 'y'):
    print("Take an umbrella")
elif(i.lower() == 'n'):
    print("You don't need an umbrella")
else:
    print("Please enter y or n")


#Task-1-2-I'm on holiday and want to hire a boat. The boat hire costs £20 + a refundable £5 deposit. I've written a program to check that I can afford the cost, but something doesn't seem right. Have a look at my program and work out what I've done wrong

my_money = int(input('How much money do you have? '))
boat_cost = 20 + 5
if my_money > boat_cost:
	print('You can afford the boat hire')
else :
	print('You cannot afford the board hire')


#Task-1-3-Your friend works for an antique book shop that sells books between 1800 and 1950 and wants to quickly categorise books by the century and decade that they were written. Write a program that takes a year (e.g. 1872) and outputs the century and decade (e.g. "Eighteenth Century, Seventies")

from num2words import num2words
i = input("please enter your input: ")
j = (num2words(int(i[0:2]), to = 'ordinal'))
k = (num2words(int(i[2:])//10, to = 'ordinal'))
if(int(i[2:])== 00):
    print(j+' Century')
else:
    print(j+' Century',k+'ties')



#Task-2-1-I have a list of things I need to buy from my supermarket of choice.I want to know what the first thing I need to buy is. However, when I run the program it shows me a different answer to what I was expecting? What is the mistake? How do I fix it.

shopping_list = [
	"oranges",
	"cat food",
	"sponge cake",
	"long-grain rice",
	"cheese board",
]
print(shopping_list[0])




#Task-2-2- I'm setting up my own market stall to sell chocolates. I need a basic till to check the prices of different chocolates that I sell. I've started the program and included the chocolates and their prices. Finish the program by asking the user to input an item and then output its price.

chocolates = {
	'white': 1.50,
 	'milk': 1.20,
	'dark': 1.80,
	'vegan': 2.00,
}

ch = input("Chocolates list:\nWhite, milk, dark, vegan\nchoose one: ")
print(chocolates[ch])



#Task-2-3
import random


def ran_number():
    number = []
    for i in range(0, 7):
        number.append(random.randint(1, 50))
        return number


def lot_num(num):

    lot_list = [1, 2, 4, 18, 40, 32, 50]
    message = ''
    matches = 0
    for no in num:
        if no in lot_list:
            matches += 1
        else:
            continue
    if matches < 3:
        message = 'You have less than 4 numbers matched, please try your luck next time'
    elif matches == 3:
        message = '£20 for three matching numbers'
    elif matches == 4:
        message = '£40 for four matching numbers'
    elif matches == 5:
        message = '£100 for five matching numbers'
    elif matches == 6:
        message = '£10000 for six matching numbers'
    elif matches == 7:
        message = '£1000000 for seven matching numbers'
    return message

def lot_simulator():
        num = ran_number()
        print('The random numbers for lottery are:', num, '\n')
        counter = 'Your prize - ' + lot_num(num)
        return counter

print(lot_simulator())





#Task-3-1- You're having coffee/tea/beverage of your choice with a friend that is learning to program in Python. They're curious about why they would use pip. Explain what pip is and one benefit of using pip.
 
print("Explanation for PIP")
print("-- Pip is the technology that manages the packages in python. The main benefit of pip is that it allows users to install python packages in any environment or platform")




#Task-3-2- This program should save my data to a file, but it doesn't work when I run it. What is the problem and how do I fix it?

poem = 'I like Python and I am not very good at poems'
with open('poem.txt', 'w') as poem_file:
	poem_file.write(poem)



#Task-3-3- Here is a snippet of Elton John’s song “I’m Still Standing”

with open ('song.txt', 'r') as song:
    line = song.readline()
    cnt = 1
    while line:
        if(line.find('still')!=-1):
            print("Line {}: {}".format(cnt, line.strip()))
        line = song.readline()
        cnt = cnt + 1



#Task-4-1- Question 1
In this session you used the Pokémon API to retrieve a single Pokémon.
I want a program that can retrieve multiple Pokémon and save their names and moves to a file.
Use a list to store about 6 Pokémon IDs. Then in a for loop call the API to retrieve the data for each Pokémon. Save their names and moves into a file called 'pokemon.txt'

import requests as rq
import json 
j = 0
for i in range(1126//20):
    url = 'https://pokeapi.co/api/v2/pokemon/?offset='+str(j)+'&limit=20'
    j+=20
    k = rq.get(url)
    raw = k.json()
    for i in range(len(raw['results'])):
        #print(raw['results'][i]['name'])
        with open('pokemon_names.txt','a') as f:
            f.writelines("%s\n"%raw['results'][i]['name'])

#Testing file for API
k = {
"count": 1126,
"next": "https://pokeapi.co/api/v2/pokemon/?offset=30&limit=10",
"previous": "https://pokeapi.co/api/v2/pokemon/?offset=10&limit=10",
"results": [
{
"name": "spearow",
"url": "https://pokeapi.co/api/v2/pokemon/21/"
},
{
"name": "fearow",
"url": "https://pokeapi.co/api/v2/pokemon/22/"
},
{
"name": "ekans",
"url": "https://pokeapi.co/api/v2/pokemon/23/"
},
{
"name": "arbok",
"url": "https://pokeapi.co/api/v2/pokemon/24/"
},
{
"name": "pikachu",
"url": "https://pokeapi.co/api/v2/pokemon/25/"
},
{
"name": "raichu",
"url": "https://pokeapi.co/api/v2/pokemon/26/"
},
{
"name": "sandshrew",
"url": "https://pokeapi.co/api/v2/pokemon/27/"
},
{
"name": "sandslash",
"url": "https://pokeapi.co/api/v2/pokemon/28/"
},
{
"name": "nidoran-f",
"url": "https://pokeapi.co/api/v2/pokemon/29/"
},
{
"name": "nidorina",
"url": "https://pokeapi.co/api/v2/pokemon/30/"
}
]
}

print(k['results'][0]['name'])

