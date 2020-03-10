# Extension Activity: Days Elapsed
# You are required to write a Python program 
# which implements the following instructions for 
# calculating the days elapsed between two dates. 
# The calculations are based on a simple estimation 
# algorithm that avoids using look-up tables for 
# leap years and days in months.

import math

name = input("plese input your name: ")
today_date = input("plese input today's date: ")

xmas_day = 25
xmas_month = 12
xmas_year = 2015

born_day = int(input("plses input your bathday's day : "))
born_month = int(input("plses input your bathday's month : "))
born_year = int(input("plses input your bathday's year : "))

now_day = int(input("input they nowday: "))
now_month = int(input("input they now month: "))
now_year = int(input("input they mow year: "))

years_indays = (now_year - born_year) * 365.25
months_indays = (now_month - born_month) * 30.4 + now_day - born_day
days_born = years_indays + months_indays

years_indays = (xmas_year - now_year) * 365.25
months_indays = (xmas_month - now_month) * 30.4 + xmas_day - now_day
days_toxmas = years_indays + months_indays

print(" Approximately", days_born, "days have elapsed since your birthday!And it is only ", abs(days_toxmas), "days to Xmas!")
