# ant-wars

To start the app:
- Start Ubuntu 18
- $ `cd ant-wars`
- $ `bin/flask`
- Type in mysql password (starcraft)
- $ `bin/flask run` will now run the app
- Go to `http://127.0.0.1:5000/`

To reset the database to accommodate changes:
- $ `bin/flask db drop` will reset database
- $ `bin/flask run` will now run the app and re-init database

Use 

curl "http://127.0.0.1:5000/colony/1" -X PUT -d'{"id":1}' -H "Content-Type: application/json"
to send commands to the API




Basic Game:

one world object with a size and colonies
each colony has the list of ants


How will a colony track what it knows? Land that is scouted, food it has found, enemy locations?
How will a single ant keep track of its current goal? ie. Where its target location is
How to differentiate AI from User? Is there a separate AI for each User? Or are they all controlled by same AI?