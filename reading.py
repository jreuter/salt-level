import hcsr04sensor.sensor as sensor
import logging
LOG_FILENAME = 'example.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)

logging.debug('This message should go to the log file')

def water_reading():
    '''Initiate a water level reading.'''
    trig_pin = 17
    echo_pin = 27
    round_to = 1
    unit = 'imperial'
    temperature = 65
    rount_to = 1
    pit_depth = 40

    value = sensor.Measurement(trig_pin, echo_pin, temperature, unit, round_to)
    raw_distance = value.raw_distance()

    if unit == 'imperial':
        water_depth = value.depth_imperial(raw_distance, pit_depth)
    if unit == 'metric':
        water_depth = value.depth_metric(raw_distance, pit_depth)

    generate_log(water_depth)
    generate_log("Salt level is "+ repr(water_depth/pit_depth*100) + "%")

def generate_log(water_depth):
    '''Log water level reading to a file.'''
    logging.debug(water_depth)

if __name__ == "__main__":
    water_reading()

