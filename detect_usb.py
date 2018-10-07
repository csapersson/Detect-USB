import pyudev

print("Script is running...")

context = pyudev.Context()
monitor = pyudev.Monitor.from_netlink(context)
monitor.filter_by(subsystem="usb")

for device in iter(monitor.poll, None):
    if device.action == "add":
        print("Device connected.")

    elif device.action == "remove":
        print("Device disconnected.")
