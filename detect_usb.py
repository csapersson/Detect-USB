import pyudev

context = pyudev.Context()
monitor = pyudev.Monitor.from_netlink(context)
monitor.filter_by(subsystem="usb")

for action, device in monitor:
    if action == "add":
        print("Device connected.")
        
    elif action == "remove":
        print("Device disconnected.")
