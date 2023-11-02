import speedtest
import time
import argparse
import sys

def execute_speedtest():
    try:
        st = speedtest.Speedtest(secure = True)
        st.get_best_server()

        download_speed = st.download() / 1_000_000  # Convert to Mbps
        upload_speed = st.upload() / 1_000_000  # Convert to Mbps
        ping = st.results.ping
        return (download_speed, upload_speed, ping)
    except Exception as e:
        print(f"An exception occurred during speedtest: {e}")
        return (0, 0, None) # Default values, in case of exception

def execute_log_test(log_file):
    download_speed, upload_speed, ping = execute_speedtest()
    timestamp = time.strftime("%Y-%m-%d_%H:%M:%S")
    log_line = f"{timestamp}\t{download_speed:.2f}\t{upload_speed:.2f}\t{ping}\n"
    log_file.write(log_line)
    print(f"Measurement at {timestamp}: Download: {download_speed:.2f} Mbps, Upload: {upload_speed:.2f} Mbps, Ping: {ping} ms")

def measure_speed(logfile, timediff, measurements):
    if timediff <= 0:
        print("Error: 'timediff' must be a positive number.")
        return

    if measurements <= 0:
        print("Error: 'measurements' must be a positive integer.")
        return

    with open(logfile, 'w') as log_file:
        log_file.write("timestamp\tdownload_speed\tupload_speed\tping\n")

        for i in range(measurements):
            start_time = time.time()

            execute_log_test(log_file)

            if i < measurements - 1:
                end_time = time.time()
                # Difference % timediff is used to guarantee \
                # whole steps of timediff
                sleep_time = timediff - ( (end_time - start_time) % timediff )
                time.sleep(sleep_time)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Measure and log internet speed.")
    parser.add_argument("--logfile", default="default.log", help="File to log internet speed measurements (default: default.log)")
    parser.add_argument("--timediff", type=int, default=60, help="Minimum time difference between measurements in seconds (default: 60)")
    parser.add_argument("--measurements", type=int, default=5, help="Number of measurements to take")
    
    args = parser.parse_args()

    try:
        measure_speed(args.logfile, args.timediff, args.measurements)
    except KeyboardInterrupt:
        print("\nSpeed measurement terminated by user.")
        sys.exit(0)

