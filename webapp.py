from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json
first = 2
app = Flask(__name__)

@app.route("/")
def render_main(): 
  first--
  with open('county_demographics.json') as demographics_data:
    counties = json.load(demographics_data)
  if first <= 0:
    print(request.args['state'])
  return render_template('home.html', options = get_state_options(counties), reply = "hey")

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
  return state
  

if __name__=="__main__":
    app.run(debug=False)
