from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json
import random
app = Flask(__name__)

@app.route("/")
def render_main(): 
  with open('county_demographics.json') as demographics_data:
    counties = json.load(demographics_data)
  return render_template('home.html', options = get_state_options(counties), reply = "hey")

@app.route("/reply")
def render_main2(): 
  with open('county_demographics.json') as demographics_data:
    counties = json.load(demographics_data)
  randomVal = int(random.random()*2)
  print(randomVal)
  if randomVal == 0:
    return render_template('home.html', options = get_state_options(counties), reply = get_fun_fact1(counties, request.args['state']))
  else:
    return render_template('home.html', options = get_state_options(counties), reply = get_fun_fact2(counties, request.args['state']))

def get_state_options(counties):
  listOfStates = []
  for county in counties:
    if county['State'] not in listOfStates:
      listOfStates.append(county['State'])
  options=""
  for state in listOfStates:
    options = options + Markup("<option value=\"" + state + "\">" + state + "</option>")
  return options

def get_fun_fact1(counties, state):
  count =0
  for county in counties:
    if county['State'] == state:
      count+= 1
  fact = "Fun Fact: Your state, " + str(state) + ", has "+ str(count) + " counties in it."
  return fact

def get_fun_fact2(counties, state):
  personCount =0
  for county in counties:
    if county['State'] == state:
      personCount = personCount + county['Population']['2010 Population']
  fact = "Fun Fact: Your state, " + str(state) + ", has "+ str(personCount) + " people in it."
  return fact
  

if __name__=="__main__":
    app.run(debug=False)
    
