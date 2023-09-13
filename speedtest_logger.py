import speedtest
import time
import argparse
import sys

def measure_speed(logfile, timediff, measurements):
    with open(logfile, 'w') as log_file:
        log_file.write("timestamp\tdownload_speed\tupload_speed\tping\n")

        for _ in range(measurements):
            st = speedtest.Speedtest(secure = True)
            st.get_best_server()

            download_speed = st.download() / 1_000_000  # Convert to Mbps
            upload_speed = st.upload() / 1_000_000  # Convert to Mbps
            ping = st.results.ping

            timestamp = time.strftime("%Y-%m-%d_%H:%M:%S")
            
            log_line = f"{timestamp}\t{download_speed:.2f}\t{upload_speed:.2f}\t{ping}\n"
            log_file.write(log_line)

            print(f"Measurement at {timestamp}: Download: {download_speed:.2f} Mbps, Upload: {upload_speed:.2f} Mbps, Ping: {ping} ms")

            time.sleep(timediff)

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

