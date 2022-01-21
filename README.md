# Application to Obtain Email Status Responses from Mandrill API

1. This application has been built using sample data in 'sample_mandrill.py' stored in the 'data' folder within the 'listener app'. 
2. The data is in a dictionary that is converted into JSON to reflect the stream expected from Mandrill. 
3. Data selection from 'sample_mandrill.py' is randomized to mimic real-time data generation as would be expected from a live API.
4. The application's Real-time functionality is built on Django Channels and Celery with Redis db as the broker. 
5. The data received is stored upon reception in the SQLite database with the schema found in models.py in the listener app. 
6. All dependencies are in the 'requirements.txt' file installable from PIP.
7. The 'env' folder contains environment files - can be activated by running '$source env/bin/activate'.
8. The web frontend displays both 'real-time' (live API data) and 'static data' (from the database) indicating when a user opens emails. If the email is unopened, the text 'Not Opened' is displayed.