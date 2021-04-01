#!/usr/bin/python3

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
        
def run_tests(logfile):
    print('Starting logging tests to file: ' + logfile)
    start_time = time.time()
    while True:
        print('Executing test...')
        result_dict = execute_test()
        print('Finished executing test')
        dspeed, uspeed, ping, timestamp = get_test_results(result_dict)
        save_results(logfile, dspeed, uspeed, ping, timestamp)
        time.sleep(60.0 - ((time.time() - start_time) % 60.0))

if len(sys.argv) > 2:
    print('You only need one parameter: the logfile\'s name (optional, default is default.log')
    sys.exit()
elif len(sys.argv) == 2:
    logfile = sys.argv[1]
else:
    logfile = 'default.log'

run_tests(logfile)
