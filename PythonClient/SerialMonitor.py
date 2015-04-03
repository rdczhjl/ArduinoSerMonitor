'''
Created on Apr 1, 2015

@author: rdczhjl
It is the Client towards Arduino
'''
import sys
import serial
import ConfigParser

global running
global monitor
global configureFile


# ==============class definition ======================== 
class SerialMonitor(object):
    '''
    classdocs
    '''
    


#Constructor
    def __init__(self, param):
        #setup the serial connection
        SerialMonitor.comPort=0
        SerialMonitor.baudRate=4800
        SerialMonitor.onInterval=10
        SerialMonitor.offInteval=1
        
        
    def setOnInterval(self,interval):
        print ("here is setOnInterval in SerialMonitor")
        print ("Now setting on interval to "+interval[0])
        SerialMonitor.onInterval=interval[0]
        
    def setOffInterval(self,interval):
        print ("here is setOffInterval in SerialMonitor")
        print ("Now setting off interval to "+interval[0])
        SerialMonitor.offInterval=interval[0]
        
    def getOffInterval(self,notUsed):
        return SerialMonitor.offInterval
    
    def getOnInterval(self,notUsed):
        return SerialMonitor.onInterval
    
    def getConfig(self,filename):
        configureFile=ConfigParser.ConfigParser()
        configureFile.read(filename)
        SerialMonitor.comPort=configureFile.get("global","ComPort")
        SerialMonitor.baudRate=configureFile.get("global","BaudRate")

# ==============define the global func ==================
def byebye(notUsed):
        print ("byebye , leaving ...")
        running=False
        exit(0)


def extfunc1(notUsed):
        print ("here is extfunc1")

# ==============define the global dictionary ==================

monitor=SerialMonitor("dummy")
theCmdDict={'bye':byebye,'extfunc1':extfunc1,'setOn':monitor.setOnInterval,'setOff':monitor.setOffInterval,
            'getOn':monitor.getOnInterval,'getOff':monitor.getOffInterval}


# ==============main ======================== 

welcomeStr= "==========Hello, Welcome to the Arduino Serial Monitor=========="
print (welcomeStr)
print (sys.argv)
args=sys.argv

#Read the configure file 
if args.count('-c'):
    nameOfConfigFile=args[args.index('-c')+1]
else:
    nameOfConfigFile="SerMonitorConfig.cfg"        
print ("Reading config file "+nameOfConfigFile)
monitor.getConfig(nameOfConfigFile)



running=True

#lookup dictionary to understand the cmd
while running:
        #get the intension 
        theIntension=raw_input("Please input your command:")
        print ("Your Command is "+theIntension)
        #translate the intension to the command
        theCmd=theIntension.split()
        func=theCmdDict[theCmd[0]]
        retVal=func(theCmd[1:]);
        print (retVal)

          
exit (0)    
