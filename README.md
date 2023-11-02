# Internet Speed Measurement Script

This Python script allows you to measure and log your internet speed using the Speedtest.net service. It provides options to specify the logfile, the time difference between measurements, and the number of measurements to take.

## Installation

1. Clone this repository or download the script file `internet_speed_logger.py`.

2. Install the required Python packages using pip:

`pip install -r requirements.txt`

## Usage

You can run the script from the command line with the following options:

`python speedtest_logger.py [--logfile LOGFILE] [--timediff TIMEDIFF] [--measurements MEASUREMENTS]`

- `--logfile` (optional): The file in which to log internet speed measurements in tsv format (default: default.tsv).
- `--timediff` (optional): Minimum time difference between measurements in seconds (default: 60 seconds).
- `--measurements` (optional): Number of measurements to take (default: 5).

Example usage:

`python speedtest_logger.py --logfile my_speed_log.tsv --timediff 120 --measurements 10`


## Output

The script will log internet speed measurements in a tab-separated values (TSV) file with the following columns:

- `timestamp`: Timestamp in the format YYYY-MM-DD_HH:mm:ss.
- `download_speed`: Download speed in Mbps.
- `upload_speed`: Upload speed in Mbps.
- `ping`: Ping time in milliseconds.

## Termination

You can terminate the script at any time by pressing Ctrl+C in the terminal. It will handle the interruption gracefully and provide a message indicating that the speed measurement has been terminated.
