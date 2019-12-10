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