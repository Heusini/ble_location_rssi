from bluepy.btle import Scanner
import time
import csv
import sys
import signal


def signal_handler(sig, frame):
    print("{};;;;;Stop", timestamp)
    sys.exit(0)

#signal.signal(signal.SIGINT, signal_handler)

if len(sys.argv) < 2:
    print("please add x y as command line argument like this python prog.py x y")
    exit(1)

x = sys.argv[1]
y = sys.argv[2]
timestamp = time.time_ns()
print("{};;;;;Start".format(timestamp))
while True:
    try:
        ble_list = Scanner().scan(0.1)
        timestamp = time.time_ns()
        for dev in ble_list:
            print("{};{};{};{};{};".format(timestamp,dev.addr,dev.rssi,x,y))
    except KeyboardInterrupt:
        print("{};;;;;Stop".format(timestamp))
        sys.exit(0)
    except:
        raise Exception("Error occured")

