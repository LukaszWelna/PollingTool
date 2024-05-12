# Polling tool
> The app is a polling tool. It allows to send answers to a question and store them in the database. 

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Setup](#setup)
* [Docker](#docker)
* [Unit tests](#unit-tests)
* [Project Status](#project-status)
* [Contact](#contact)

## General Information
- The user is able to receive question from database.
- Application allows to send answer and save this into database.
- User can check what is the average of good answers to that question.
- Application is using python and MongoDB.
- The password to database is placed in .env file. Connection with database is using "testUser" which is added to database. 

## Technologies Used
- Python 3.10.8
- MongoDB 5.0.14

## Setup
The required dependencies to run the project are listed in requirements.txt file.

Steps to run project locally:
- Install python 3.10.8 from https://www.python.org/downloads/release/python-3108/.
- Clone repository to selected folder.
- Install required dependecies by running command `pip install -r requirements.txt`
- If you wish to run unit tests run command `pip install -r requirements_dev.txt`
- Run application by command `python -m uvicorn main:app`
- You can view available endpoints at `localhost:8000/docs`

Steps to run project with Docker:
- Install docker in your system.
- Download docker image via command `docker pull lukaszwelna/coding_challenge:v1.1`
- Run application by command `docker run -p 80:80 lukaszwelna/coding_challenge:v1.1`
- Application is accessible in localhost port 80
- You can view available endpoints at `localhost:80/docs`

## Docker
Building docker image:
- Run command `docker build -t <name_of_docker_image> .`

## Unit tests
- Run command `pip install -r requirements_dev.txt`
- Run command `python -m pytest`

## Project Status
The assumed functionality is done. 
It is possible to improve the project in future. 

Improvements:
- Adding frontend.
- Extending the survey by adding more questions. 

## Contact
Created by Lukasz Welna. For inquiries, please reach out on [LinkedIn](https://www.linkedin.com/in/lukasz-welna) or [Website](https://lukasz-welna.profesjonalnyprogramista.pl/).
