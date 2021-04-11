#!/usr/bin/python

import speedtest
import sys
import time
import os

def execute_test():
    my_speedtest = speedtest.Speedtest()
    my_speedtest.get_best_server()
    my_speedtest.download()
    my_speedtest.upload()
    return my_speedtest.results.dict()

def get_test_results(result_dict):
    dspeed = round(result_dict['download'] / 2 ** 20, 1)
    uspeed = round(result_dict['upload'] / 2 ** 20, 1)
    ping = result_dict['ping']
    timestamp = result_dict['timestamp']
    timestamp = timestamp.replace('T', '_')
    timestamp = timestamp.replace('Z', '')
    timestamp = timestamp[:timestamp.find('.')]
    return (dspeed, uspeed, ping, timestamp)

def save_results(logfile, dspeed, uspeed, ping, timestamp):
    file_exists = os.path.isfile(logfile)
    with open(logfile, "a") as myfile:
        if not file_exists:
            header = 'timestamp\tdownload_speed\tupload_speed\tping\n'
            myfile.write(header)
        myfile.write(str(timestamp) + '\t' + str(dspeed) + '\t' + str(uspeed) + '\t' + str(ping) + str('\n'))
        
def run_tests(logfile, time_diff):
    print('Starting logging tests to file: ' + logfile)
    start_time = time.time()
    while True:
        print('Executing test...')
        result_dict = execute_test()
        print('Finished executing test')
        dspeed, uspeed, ping, timestamp = get_test_results(result_dict)
        save_results(logfile, dspeed, uspeed, ping, timestamp)
        time.sleep(time_diff - ((time.time() - start_time) % time_diff))

try:
    if len(sys.argv) > 3:
        print('You only need two parameter: the logfile\'s name (optional, default is default.log), and the time difference between tests in seconds (default is 60 s, must be at least 60 s)')
        sys.exit()
    if len(sys.argv) > 1:
        logfile = sys.argv[1]
    else:
        logfile = 'default.log'

    if len(sys.argv) > 2:
        time_diff = float(sys.argv[2])
        if time_diff < 60.0:
            print('The minimum time difference must be at least 60 s, setting time differece to 60 s!')
            time_diff = 60.0
    else:
        time_diff = 60.0

    run_tests(logfile, time_diff)

except KeyboardInterrupt:
    print('\nExiting now...')
    sys.exit()

