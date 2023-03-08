# Commands to start flask in debug mode
git clone https://github.com/tobiasmoe/msthesis
cd msthesis/
apt install python3-pip
apt install sqlite3
pip install Flask
export FLASK_APP=webpage_collect
export FLASK_ENV=development
flask init-db // initalize database, new folder created called "instance" inside is db file called flaskr.sqlite3
flask run

go to localhost:5000 in webbrowser
you should now see the webpage

run simulation program

extract timing information from database
inside instance folder
sqlite3 flaskr.sqlite3
.headers on
.mode csv
.output data.csv
SELECT * FROM keystrokes;
.quit
