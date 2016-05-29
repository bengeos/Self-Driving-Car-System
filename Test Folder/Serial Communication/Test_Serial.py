import serial as sp

SP = sp.Serial('COM4')
while(SP.isOpen()):
    print SP.readline()
