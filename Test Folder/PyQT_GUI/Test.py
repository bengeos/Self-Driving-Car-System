import serial.tools.list_ports
Ports = list(serial.tools.list_ports.comports())
for x in Ports:
    print x[0]