from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json
import random
app = Flask(__name__)

@app.route("/")
def render_main(): 
  with open('county_demographics.json') as demographics_data:
    counties = json.load(demographics_data)
  return render_template('home.html', options = get_state_options(counties), reply = "", options2 = get_county_options(counties), reply2 = "")

@app.route("/reply")
def render_main2(): 
  with open('county_demographics.json') as demographics_data:
    counties = json.load(demographics_data)
  randomVal = int(random.random()*3)
  if randomVal == 0:
    return render_template('home.html', options = get_state_options(counties), reply = get_state_fact1(counties, request.args['state']), options2 = get_county_options(counties), reply2 = get_county_fact1(counties, request.args['county']))
  elif randomVal == 1:
    return render_template('home.html', options = get_state_options(counties), reply = get_state_fact2(counties, request.args['state']), options2 = get_county_options(counties), reply2 = get_county_fact1(counties, request.args['county']))
  else:
    return render_template('home.html', options = get_state_options(counties), reply = get_state_fact3(counties, request.args['state']), options2 = get_county_options(counties), reply2 = get_county_fact1(counties, request.args['county']))

def get_state_options(counties):
  listOfStates = []
  for county in counties:
    if county['State'] not in listOfStates:
      listOfStates.append(county['State'])
  options=""
  for state in listOfStates:
    options = options + Markup("<option value=\"" + state + "\">" + state + "</option>")
  return options

def get_county_options(counties):
  listOfCounties = []
  for county in counties:
    listOfCounties.append(county['County'])
  options=""
  for county in listOfCounties:
    options = options + Markup("<option value=\"" + county + "\">" + county + "</option>")
  return options

def get_state_fact1(counties, state):
  count =0
  for county in counties:
    if county['State'] == state:
      count+= 1
  fact = "Fun Fact: Your state, " + str(state) + ", has "+ str(count) + " counties in it."
  return fact

def get_state_fact2(counties, state):
  personCount =0
  for county in counties:
    if county['State'] == state:
      personCount = personCount + county['Population']['2010 Population']
  fact = "Fun Fact: Your state, " + str(state) + ", has "+ str(personCount) + " people in it."
  return fact

def get_state_fact3(counties, state):
  vetCount =0
  for county in counties:
    if county['State'] == state:
      vetCount = vetCount + county['Miscellaneous']['Veterans']
  fact = "Fun Fact: Your state, " + str(state) + ", has "+ str(vetCount) + " vetrans in it."
  return fact

def get_county_fact1(counties, county):
  print( str(county['Miscellaneous']['Language Other than English at Home']) + "percent of people in " + county + " speak a foreign language at home.")
  return "o"
  

if __name__=="__main__":
    app.run(debug=False)
    
