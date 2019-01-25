import os
import glob
import time
import MySQLdb

# Turns on the GPIO module
os.system('modprobe w1-gpio')
# Turns on the Temp module
os.system('modprobe w1-therm')


# Search the correct device file that holds the temp data info
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'


#Setup the connection to the MySQL server needed for live preview data and for 24h statistics
conn = MySQLdb.connect(host="localhost", user="root", passwd="", db="phd_patr")

cursor = conn.cursor()


# Function that reads the sensors data
def read_temp_raw():
    # Opens the temperature device file
    f = open(device_file, 'r')
    #Read the values from sensor
    lines = f.readlines()
    f.close()
    #returne the raw value
    return lines

# Convert the value of the sensor into a temperature data
def read_temp():
    # Read the temperature
    lines = read_temp_raw()
    # While the first line does not contain 'YES', wait for 0.2s
    # and then read the device file again.
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()

    # Look for the position of the '=' in the second line of the
    # device file.
    equals_pos = lines[1].find('t=')

    # If the '=' is found, convert the rest of the line after the
    # '=' into degrees Celsius, then degrees Fahrenheit
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c


#Store data every 5 seconds until the api is stopped
while True:
    print(read_temp())
    mytemp = read_temp()
    logdata = ('INSERT INTO track_data (sensor, value) '
                '    VALUES ("temperature", %s)')
    cursor.execute(logdata, (mytemp))
    conn.commit()
    time.sleep(5) 
