from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__)

@app.route("/")
def render_main(): 
  return render_template('home.html')

def get_state_options(counties):
  listOfStates = []
  for county in counties:
    if county['State'] not in listOfStates:
      listOfStates.append(county['State'])
  options=""
  for state in listOfStates:
    options = options +
  return options
