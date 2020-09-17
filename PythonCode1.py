import time
import sys
import ibmiotf.application #to install pip install ibmiotf
import ibmiotf.device

#Provide your IBM Watson Device Credentials
organization = "uo20tn"
deviceType = "raspberrypi"
deviceId = "345678"
authMethod = "token"
authToken = "123456789"


def myCommandCallback(cmd):
        print("Command received: %s" % cmd.data)
        if cmd.data('command')=='lighton':
                print("LIGHT ON IS RECIEVED")
             
        elif cmd.data('command')=='lightoff':
                print("LIGHT OFF IS RECIEVED")

        if cmd.command == "set interval":

                if 'interval' not in cmd.data:
                        print("Error - command is missing required information: %s" % cmd.data)
                else:
                        interval = cmd.data['interval']
        elif cmd.command == "print":
                if 'message' not in cmd.data:
                        print("Error - command is missing required information: %s" % cmd.data)
                else:
                        output=cmd.data['message']
                        print(output)
                        

try:
        deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
        deviceCli = ibmiotf.device.Client(deviceOptions)#.............................................
	
except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()
	# Connect and send a datapoint "hello" with value "world" into the cloud as an event of type "greeting" 10 times
deviceCli.connect()

while True:
        
        deviceCli.commandCallback = myCommandCallback

# Disconnect the device and application from the cloud
deviceCli.disconnect()
