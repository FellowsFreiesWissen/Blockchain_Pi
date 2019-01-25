import os
import glob
import time
import MySQLdb
import json
import time
import datetime

# connect to the Database
connection = MySQLdb.connect(host="localhost", user="root", passwd="", db="phd_patr")
inst = connection.cursor()
FMT = '%H:%M:%S'
# Setup the hour to run the script
loop_time= "19:36:10"
data_json = {}
time_fn = datetime.datetime.now()

# Create the export database to a json file.
def databse_exrtact_data():
    mytemp = read_temp()
    data_verbose = "SELECT * FROM track_data WHERE date BETWEEN DATE_SUB(NOW(), INTERVAL 1 DAY)  AND NOW()"
    inst.execute(loggit, (mytemp))
    results = inst.fetchall()
    #Setup the filename as date_sensorType.js 
    filename = time_fn.strftime("%d_%m_%y") + '_temp.json'
    data_json['temp'] = []

    #iterate through results and append them to the json
    for row in results:
        data_json['temp'].append({
            'sensor': row['sensor'],
            'value': row['value'],
            'date': row['create_at']
        })
    #Builds the export file
    with open('files/'+filename, 'w') as outfile:
        json.dump(data_json, outfile)
    os.system('ipfs add files/'+ filename);

# Define run time based on the loop_time variable set.
while True:
    time_now = datetime.datetime.now()
    if time_now.strftime("%H:%M:%S") == loop_time:
        databse_exrtact_data()
