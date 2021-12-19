#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 12:40:21 2019

@author: joonas
"""

#Random Team Generator

from random import choice

def two_teams():
    while len(players) > 0:
        playera = choice(players)
        Team_a.append(playera)
        players.remove(playera)
    
        playerb = choice(players)
        Team_b.append(playerb)
        players.remove(playerb)

    print(Team_nameA, " : ", Team_a)
    print(Team_nameB, " : ", Team_b)
    
def three_teams():
    while len(players) > 0:
        playera = choice(players)
        Team_a.append(playera)
        players.remove(playera)
    
        playerb = choice(players)
        Team_b.append(playerb)
        players.remove(playerb)
            
        playerc = choice(players)
        Team_c.append(playerc)
        players.remove(playerc)

    print(Team_nameA, " : ", Team_a)
    print(Team_nameB, " : ", Team_b)
    print(Team_nameC, " : ", Team_c)
    
def four_teams():
    while len(players) > 0:
        playera = choice(players)
        Team_a.append(playera)
        players.remove(playera)
    
        playerb = choice(players)
        Team_b.append(playerb)
        players.remove(playerb)
    
        playerc = choice(players)
        Team_c.append(playerc)
        players.remove(playerc)
            
        playerd = choice(players)
        Team_d.append(playerd)
        players.remove(playerd)
    
    print(Team_nameA, " : ", Team_a)
    print(Team_nameB, " : ", Team_b)
    print(Team_nameC, " : ", Team_c)
    print(Team_nameD, " : ", Team_d)

prompt = int(input("How many players are there? "))

number_teams = (input("How many teams are there? * Maximum of 4 * "))
if number_teams != "2" or number_teams != "3" or number_teams != "4":
    print("Not possible madafaka")


players= []

while prompt != len(players):
    name = input("enter a name: ") 
    players.append(name)

print(players)

Team_a = []
Team_b = []
Team_c = []
Team_d = []

if number_teams == "2":
    Team_nameA = input("What is the first team name? ")
    Team_nameB = input("What is the second team name?")
    two_teams()
    
elif number_teams == "3":
    Team_nameA = input("What is the first team name? ")
    Team_nameB = input("What is the second team name?")
    Team_nameC = input("What is the third team name?")
    three_teams()
  
elif number_teams == "4":
    Team_nameA = input("What is the first team name? ")
    Team_nameB = input("What is the second team name?")
    Team_nameC = input("What is the third team name?")
    Team_nameD = input("What is the fourth team name?")
    four_teams()
 
else:
    print("Not possibe madafaka")


    
 
  
