from bluepy.btle import Scanner
import time
import csv
import sys
import signal


def signal_handler(sig, frame):
    print("{};;;;;Stop", timestamp)
    sys.exit(0)

if len(sys.argv) < 2:
    print("please add x y as command line argument like this python prog.py x y")
    exit(1)

x = sys.argv[1]
y = sys.argv[2]
timestamp = time.time_ns()
oldTimeStamp = time.time_ns()
print("{};;;;;Start".format(timestamp))
while True:
    try:
        # record for 100ms
        ble_list = Scanner().scan(0.1)
        timestamp = time.time_ns()
        for dev in ble_list:
            print("{};{};{};{};{};".format(timestamp,dev.addr,dev.rssi,x,y))

        # only record for 10 seconds
        if timestamp - oldTimeStamp > 1e+10:
            print("{};;;;;TimeStop".format(timestamp))
    except KeyboardInterrupt:
        print("{};;;;;Stop".format(timestamp))
        sys.exit(0)
    except:
        raise Exception("Error occured")

