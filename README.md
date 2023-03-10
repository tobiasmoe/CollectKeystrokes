# Background
This is a simple webpage written in Flask. <br>
It hosts a simple webpage that allows you to collect timing information from keystrokes written into an input field. <br>
This program was created to be used by the following simulation program: https://github.com/tobiasmoe/SimulateKeystrokes <br>

# Pre installation
This is only tested on Windows Subsystem for Linux <br>
Clone this git repository then cd into it <br>

# Commands to start flask in debug mode <br>
__apt install python3-pip__ <br>
__apt install sqlite3__ <br>
__pip install Flask__ <br>
__export FLASK_APP=webpage_collect__ <br>
__export FLASK_ENV=development__ <br>
__flask init-db__ // initalize database, new folder created called "instance" inside is db file called flaskr.sqlite3. Can also be used to "wipe" database <br>
__flask run__ <br>

go to localhost:5000 in webbrowser <br>
you should now see the webpage <br>

run keystroke simulation program that will enter information into the input field <br>

# Extract timing information from database
inside instance folder <br>
__sqlite3 flaskr.sqlite3__ <br> 
__.headers on__ <br>
__.mode csv__ <br> 
__.output data.csv__ <br>
__SELECT * FROM keystrokes;__ <br>
__.quit__ <br>

Now you have timing information in csv format.
