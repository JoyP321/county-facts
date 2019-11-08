from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json
import random
app = Flask(__name__)

@app.route("/")
def render_first_dropdown(): 
  with open('county_demographics.json') as demographics_data:
    counties = json.load(demographics_data)
  return render_template('home.html', options = get_state_options(counties), reply = "", options2 = "", reply2 = "")

@app.route("/reply")
def render_second_dropdown():
  return render_template('home.html', options = get_state_options(counties), reply = "", options2 = get_county_options(counties, request.args['state']), reply2 = "")
           
@app.route("/reply2")
def render_facts(): 
  with open('county_demographics.json') as demographics_data:
    counties = json.load(demographics_data)
  randomStateVal = int(random.random()*3)
  randomCountyVal = int(random.random()*2)
  stateFact = ""
  countyFact = ""
  if randomStateVal == 0:
    stateFact = get_state_fact1(counties, request.args['state'])
  elif randomStateVal == 1:
    stateFact = get_state_fact2(counties, request.args['state'])
  else:
    stateFact = get_state_fact2(counties, request.args['state'])
  
  if randomCountyVal == 0:
    countyFact = get_county_fact1(counties, request.args['county'])
  elif randomCountyVal == 1:
    countyFact = get_county_fact2(counties, request.args['county'])
  
  return render_template('home.html', options = get_state_options(counties), reply = Markup("<p>" + stateFact + "</p>"), options2 = get_county_options(counties, request.args['state']), reply2 = Markup("<p>" + countyFact + "</p>"))

def get_state_options(counties):
  listOfStates = []
  for county in counties:
    if county['State'] not in listOfStates:
      listOfStates.append(county['State'])
  options=""
  for state in listOfStates:
    options = options + Markup("<option value=\"" + state + "\">" + state + "</option>")
  return options

def get_county_options(counties, state):
  listOfCounties = []
  for county in counties:
    ifcounty['State']== state:
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
  for c in counties:
    if c['County']==county:
      return "Fun Fact: " + str(c['Miscellaneous']['Language Other than English at Home'])+ " percent of people in " + county + " speak a foreign language at home."

def get_county_fact2(counties, county):
  for c in counties:
    if c['County']==county:
      return "Fun Fact: There are " + str(c['Housing']['Households'])+ " households in " + county
  

if __name__=="__main__":
    app.run(debug=False)
    
