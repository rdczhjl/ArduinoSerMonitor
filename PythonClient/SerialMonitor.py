'''
Created on Apr 1, 2015

@author: rdczhjl
It is the Client towards Arduino
'''
import sys
import serial

global running
global monitor




# ==============class definition ======================== 
class SerialMonitor(object):
    '''
    classdocs
    '''



#Constructor
    def __init__(self, param):
        #setup the serial connection
        '''
        classdocs
        '''
        
    def func1(self):
        print ("here is func1 in SerialMonitor")
        
    def func2(self):
        print ("here is func2 in SerialMonitor")
        

# ==============define the func ==================
def byebye():
        print ("byebye , leaving ")
        running=False
        exit(0)


def extfunc1():
        print ("here is extfunc1")

# ==============define the dictionary ==================
theCmdDict={'bye':byebye,'extfunc1':extfunc1,'func1':SerialMonitor.func1}


# ==============main ======================== 

welcomeStr= "==========Hello, Welcome to the Arduino Serial Monitor=========="
print (welcomeStr)


running=True
monitor=SerialMonitor("dummy")

#lookup dictionary to understand the cmd
while running:
        #get the intension 
        theIntension=raw_input("Please input your command:")
        print ("Your Command is "+theIntension)
        #translate the intension to the command
       
        func=theCmdDict[theIntension]
        func();

          
exit (0)    
