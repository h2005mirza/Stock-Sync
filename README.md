# Stock-Sync
An automated stock tracking application. 

Stock Sync is an automated stock tracking application built using Python and SQLite. 
This program uses three main ideas: Automation, Data Extraction and Data Visualisation. 
The tools and Libraries used in this program are as follows:
1. Python
2. SQLite
3. Databases
4. Pycharm
5. Polygon.io API
6. Libraries: urllib, time, json, sqlite3, schedule, tabulate, datetime, pytz.

1. API_HANDLER:
   In this file, I used the Polygon.io API key to extract data from the web which is in JSON form and parse it.

2. DATABASE:
   In this file, I used the SQLite3 library to create the database and insert into it by importing the Api_handler file and its functions.

3. DISPLAY:
   In this file, I used the Tabulate library to display the inserted data in the database by fetching it and then displaying it in a neat grid format.

4. SCHEDULER:
   In this file, I have used the pytz and schedule libraries. The pytz is used to define the different time zones. First, the NYSE opening and closing hours, and then
   Pakistan's time zone so that both time zones work correctly.
   Opening and Closing Hours: (09:30 AM - 04:00 PM)
   Pakistan Time: (06:30 PM - 01:00 AM)
   Using the schedule library, I created a schedule of fetching data every ten minutes and updating the data in the database. This runs until the market closes and final
   Fetched data can be used for visualisation purposes.

   This is a simple and exciting program. Please feel free to use it. 

   

