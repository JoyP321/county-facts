from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json
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
  return render_template('home.html', options = get_state_options(counties), reply = request.args['state'])

def get_state_options(counties):
  listOfStates = []
  for county in counties:
    if county['State'] not in listOfStates:
      listOfStates.append(county['State'])
  options=""
  for state in listOfStates:
    options = options + Markup("<option value=\"" + state + "\">" + state + "</option>")
  return options

def get_fun_fact(counties, state):
  count =0
  for county in counties:
    if county['State'] == state:
      count+= 1
  fact = "Your state, " + state + ", has "+ count + " counties in it"
  return state
  

if __name__=="__main__":
    app.run(debug=False)
    
