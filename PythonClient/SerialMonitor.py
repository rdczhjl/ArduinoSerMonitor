'''
Created on Apr 1, 2015

@author: rdczhjl
It is the Client towards Arduino
'''
import os
import ConfigParser
import serial
import struct
import sys



global running
global monitor
global configureFile
global theMessageFormat

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
        self.serSession=0
        
       
        
    def getConfigAndSetup(self,filename):
        configureFile=ConfigParser.ConfigParser()
        configureFile.read(filename)
        SerialMonitor.comPort=configureFile.get("global","ComPort")
        SerialMonitor.baudRate=configureFile.get("global","BaudRate")
        
        print("Now setup ..COM:"+SerialMonitor.comPort+"Baud:"+SerialMonitor.baudRate)
        self.serSession=serial.Serial(SerialMonitor.comPort,SerialMonitor.baudRate)
        print ("Open the serial session "+str(self.serSession.isOpen()))
        self.serSession.timeout=0

    def closeAll(self):
        if isinstance(self.serSession, serial.Serial) :
            self.serSession.close()
             
    def printMessageFromPeer(self):
        theMsgList=self.serSession.readlines()
        for m in theMsgList :
            print(m) 
    
    
    def setOnInterval(self,interval):
        global theMessageFormat
        
        print ("here is setOnInterval in SerialMonitor")
        print ("Now setting on interval to "+interval[0])
        SerialMonitor.onInterval=interval[0]
        theMsg=struct.pack(theMessageFormat,"seOn",SerialMonitor.onInterval)
        numOut=self.serSession.write(theMsg)
        print ("We sent the command setOn "+interval[0]+" to Arduino and "+str(numOut)+" are sent")
        
        
    def setOffInterval(self,interval):
        print ("here is setOffInterval in SerialMonitor")
        print ("Now setting off interval to "+interval[0])
        SerialMonitor.onInterval=interval[0]
        theMsg=struct.pack(theMessageFormat,"seOf",SerialMonitor.onInterval)
        numOut=self.serSession.write(theMsg)
        print ("We sent the command setOff "+interval[0]+" to Arduino and "+str(numOut)+" are sent")
        
    def getOffInterval(self,notUsed):
        print ("here is getOffInterval in SerialMonitor")
        theMsg=struct.pack(theMessageFormat,"geOf",'0')
        numOut=self.serSession.write(theMsg)
        print ("We sent the command setOff to Arduino and "+str(numOut)+" are sent")
        return SerialMonitor.offInterval
    
    def getOnInterval(self,notUsed):
        print ("here is getOnInterval in SerialMonitor")
        theMsg=struct.pack(theMessageFormat,"geOn",'0')
        numOut=self.serSession.write(theMsg)
        print ("We sent the command setOff to Arduino and "+str(numOut)+" are sent")
        return SerialMonitor.onInterval
    
        
# ==============define the global func ==================
def byebye(notUsed):
        global running,monitor
        print ("byebye , leaving ...COM Port "+SerialMonitor.comPort+" BaudRate "+SerialMonitor.baudRate)
        monitor.closeAll()
        running=False



def extfunc1(notUsed):
        print ("here is extfunc1")

# ==============define the global dictionary ==================

monitor=SerialMonitor("dummy")
theCmdDict={'bye':byebye,'extfunc1':extfunc1,'seOn':monitor.setOnInterval,'seOf':monitor.setOffInterval,
            'geOn':monitor.getOnInterval,'geOf':monitor.getOffInterval}
theMessageFormat="4sc"

# ==============main ======================== 

welcomeStr= "==========Hello, Welcome to the Arduino Serial Monitor=========="
print (welcomeStr)
print (sys.argv)
args=sys.argv

#Read the configure file 
if args.count('-c'):
    nameOfConfigFile=args[args.index('-c')+1]
else:
    nameOfConfigFile="../SerMonitorConfig.cfg"        
print ("Reading config file "+nameOfConfigFile)

try:
    monitor.getConfigAndSetup(nameOfConfigFile)
except:
    print ("Please check whether the configure file is there or Arduino HW is connected")
    exit(-1)


running=True

#lookup dictionary to understand the cmd
while running:
        #get the intension 
        theIntension=raw_input("Please input your command:")
        print ("Your Command is "+theIntension)
        
        #translate the intension to the command
        try:
            theCmd=theIntension.split()
            func=theCmdDict[theCmd[0]]
            retVal=func(theCmd[1:]);
            monitor.printMessageFromPeer()
        except :
            print ("Wrong Format of Command ...")
          
exit (0)    
