#!/usr/bin/python3
# COVID Analysis Tool by Cody Skinner (https://codyskinner.net)
# API Courtesy Of: Javieraviles (https://github.com/javieraviles/covidAPI)

import argparse
import sys
import requests
import json

# Intro Text:
print("COVID-19 Analysis Tool by Cody Skinner")
print("https://codyskinner.net")
print("@TheCodySkinner")

# Arg Parse
parser = argparse.ArgumentParser(description="Provide real-time COVID-19 statistics.")
parser.add_argument("location", nargs="?", default="USA", help="Location to get data for (see 'list') NOTE: if country contains spaces, enclose in quotes ('')")
parser.add_argument("-l", "--list", help="Show available locations", action="store_true")
args = parser.parse_args()

# Confirmation and Please Wait
if args.list == 1:
    print("\n\nPlease Wait... Compiling List...")
else:
    print("\n\nPlease Wait... Collecting Data for ",args.location,"...\n",sep="")

# Setup vars
api = "https://coronavirus-19-api.herokuapp.com/"
apiall = requests.get(api+"all")
apicountries = requests.get(api+"countries")
apilocal = requests.get(api+"countries/"+args.location)
local_cases = apilocal.json()['cases']
global_cases = apiall.json()['cases']
local_deaths = apilocal.json()['deaths']
global_deaths = apiall.json()['deaths']
local_recovered = apilocal.json()['recovered']
global_recovered = apiall.json()['recovered']
local_today = apilocal.json()['todayCases']
local_active = apilocal.json()['active']
local_crit = apilocal.json()['critical']

# Print list
if args.list == 1:
    for i in apicountries.json():
        if i['country'] != 'Total:':
            print(i['country'])
    sys.exit(0)

# Output
print("---------------\n- Total Cases -\n---------------")
print(args.location,"Cases:", local_cases)
print(args.location,"New Cases Today:", local_today)
local_today_percent = (local_today/local_cases)*100
print(round(local_today_percent,2), "% of ",args.location," cases are from today", sep="")
print("Global Cases: ", global_cases)
local_cases_percent = (local_cases/global_cases)*100
print(round(local_cases_percent,2), "% of global cases are in ",args.location, sep="")

print("\n-----------------\n- Active Cases  -\n-----------------")
print(args.location,"Active Cases: ",local_active)
print(args.location,"Active (critical): ",local_crit)
local_active_percent = (local_active/local_cases)*100
local_crit_percent = (local_crit/local_cases)*100
print(round(local_active_percent,2), "% of ",args.location," cases still active", sep="")
print(round(local_crit_percent,2), "% of ",args.location," cases in critical condition", sep="")

print("\n----------\n- Deaths -\n----------")
print(args.location,"Deaths:",local_deaths)
print("Global Deaths:",global_deaths)
local_death_percent = (local_deaths/global_deaths)*100
print(round(local_death_percent,2), "% of global deaths are from ", args.location, sep="")

print("\n------------\n- Recovery -\n------------")
print(args.location,"Recovered: ", local_recovered)
print("Global Recovered: ", global_recovered)
local_recovery_percent = (local_recovered/local_cases)*100
print(round(local_recovery_percent,2), "% of cases recovered in ",args.location, sep="")
global_recovery_percent = (global_recovered/global_cases)*100
print(round(global_recovery_percent,2), "% of cases recovered globally", sep="")


