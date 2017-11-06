# Deep Style Web App

## Current Progress: Step 1 and 2.

## NOTES
Need to change tensorflow script to allow_soft_placement = TRUE to automatically
use an available gpu. Job scheduler handles gpu assignment to each command.

Django backend assumed to be sqlite3. Need to test on inputs.
How to safely exit out of job scheduling?

Start thinking about creating docker image and DL/UL for the website.

## Running the program

We need to run the script run_server.sh in order to have docker and nvidia
libraries installed in the AWS instance. This script will also automatically
start the app if it succeeds. If these dependencies have already been installed
and the docker container has already been build, then we can just run:

nvidia-docker run -p 80:80 -d -it deepstyleapp sh /app/start_app_wrapper.sh

to start the app.

## Structure

The web app consists of:

1. Django backend with a (SQLite?) database
2. Python job scheduling script
3. Input/Output in Frontend and Backend
4. Connecting tensorflow version of Neural Style Transfer
5. Docker instructions file

## Fahim
Django backend

## Kevin
Job scheduling
