import serial
import binascii
port = input("Enter port name:")	
ser = serial.Serial(port, baudrate = 9600, timeout = 1)
ser1 = serial.Serial(port, baudrate = 9600, timeout = 10)
#ser.open()

#################################

#Set Integration Time ( 10 \mus - 60 000 000 \mus ) 
c1 = b'\xc1\x00\x000\x000'
#Set Number of Frames (Scans, Readouts) Per Acquisition ( 1 - 4599 )
c2 = b'\xc2\x00\x00\x01\x01'
#Set CCD Operating Mode ( 0 - 4 ) 
c3 = b'\xc3\x00'
#Set Trig Out Before Integration Offset ( 0 \mus - 1849 \mus )
c4 = b'\xc4\x00\x00\x00\x00'
#Enable Trigger Output ( 0 = disabled, 1 = enabled )
c5 = b'\xe1\x00'
#Set Hardware Dark Correction ( 0 = disabled, 1 = enabled )
c6 = b'\xc5\x00'
#Include Dummy Pixels in Readouts  ( 0 = disabled, 1 = enabled )
c7 = b'\xc9\x00'
#Initiate Acquisition in Onboard Data Storage Mode
c8 = b'\xc6'
#Initiate Acquisition in Data Streaming Mode and Stream Data Until Manually Stopped
c9 = b'\xc7'
#Stop Acquisition and Data Streaming  
c10 = b'\xc8'

####################################
while True:
	cmd = input("Enter command name:")
	if globals()[cmd] == c1:
		ser.write(c1)
		if ser.readline() == b'\x06':
			print("ACK")
		break
	elif globals()[cmd] == c2:
		ser.write(c2)
		if ser.readline() == b'\x06':
			print("ACK")
		break
	elif globals()[cmd] == c3:
		ser.write(c3)
		if ser.readline() == b'\x06':
			print("ACK")
		break
	elif globals()[cmd] == c4:
		ser.write(c4)
		if ser.readline() == b'\x06':
			print("ACK")
		break
	elif globals()[cmd] == c5:
		ser.write(c5)
		if ser.readline() == b'\x06':
			print("ACK")
		break
	elif globals()[cmd] == c6:
		ser.write(c6)
		if ser.readline() == b'\x06':
			print("ACK")
		break
	elif globals()[cmd] == c7:
		ser.write(c7)
		if ser.readline() == b'\x06':
			print("ACK")
		break
	elif globals()[cmd] == c8:
		ser.write(c8)
		ser1.readline()
		if ser.readline() == b'\x06':
			print("ACK")
		break
	elif globals()[cmd] == c9:
		ser.write(c9)
		k = ser1.readline()
		asciispec = binascii.a2b_hex(k)
		k1 = \x01\x0f\x00\x01\x00\x00\x00\xc8\xd9
		spec = int(k1,16)
		break
	elif globals()[cmd] == c10:
		ser.write(c10)
		ser.readline()
		break
ser.close()

