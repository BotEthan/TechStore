# Ethan's Tech Store
This script is a basic implementation of an inventory manager from my L1T30 task. It is desgined to take in an inventory from a text file and display the current info in the console.
This is a command line interface script. Everything to manage the inventory is done in the console running it.

## Table of Contents:
* [Installation](https://github.com/BotEthan/TechStore/#installation)

* [Usage](https://github.com/BotEthan/TechStore/#usage)


## Installation
To install please make sure all the libraries/modules in the requirements.txt have been downloaded and installed.

In order to retrieve all the libraries from requirements into your venv run ```pip install -r requirements.txt``` in a shell console that has your venv active.

For Docker you would need to create a Docker Image by building it first. The Dockerfile manages moving the requirements.txt over and installing from the requirements.txt

## Usage
To run the django site on your virtual environment please input ```python manage.py runserver``` in your shell with the virtual environment active. From there
follow to the url given in the terminals response to the command. From there you can navigate it like a regular browser page.

To run the django site on your Docker, after you have created the image, ```docker run -t {your_builds_name}```. From there
follow to the url given in the terminals response to the command. From there you can navigate it like a regular browser page.