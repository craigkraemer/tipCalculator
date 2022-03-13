# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 17:21:09 2022

@author: craig
"""

print("Welcome to the tip calculator!\n")
total_bill = input("What was the total bill? $")
tip = input("How much tip would you like to give? ")
people = input("How many people to split the bill? ")
total_bill = float(total_bill)
tip = float(tip)
people = int(people)
each_pay = (total_bill/people) * ((tip/100) + 1)
each_pay = "${:,.2f}".format(each_pay)
print(f"\nYou will each pay: {each_pay}")