import hcsr04sensor.sensor as sensor
import os
import subprocess
import logging

LOG_FILENAME = 'example.log'
logging.basicConfig(filename=LOG_FILENAME,
		    format='%(asctime)s %(message)s',
		    level=logging.DEBUG)

def salt_reading():
    '''Initiate a water level reading.'''
    trig_pin = 17
    echo_pin = 27
    round_to = 1
    unit = 'imperial'
    temperature = 65
    rount_to = 1
    # Tank is 35", but 7" is the constant water level.
    pit_depth = 28

    value = sensor.Measurement(trig_pin, echo_pin, temperature, unit, round_to)
    raw_distance = value.raw_distance()

    if unit == 'imperial':
        salt_depth = value.depth_imperial(raw_distance, pit_depth)
    if unit == 'metric':
        salt_depth = value.depth_metric(raw_distance, pit_depth)

    percentage = salt_depth/pit_depth*100
    if percentage < 25 :
	pwd =  os.path.dirname(os.path.realpath(__file__))
        cmd = [
	    'python',
	    os.path.join(pwd, 'send_alert.py')
	]
	subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    generate_log("{0:.1f} inches or {1:.2f} %".format(salt_depth, percentage))

def generate_log(salt_depth):
    '''Log salt level reading to a file.'''
    logging.debug(salt_depth)

if __name__ == "__main__":
    salt_reading()

