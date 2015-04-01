'''
Created on Apr 1, 2015

@author: rdczhjl
It is the Client towards Arduino
'''
import sys
import serial



''' ==============main ======================== '''

welcomeStr= "Hello, Welcome to the Arduino Serial Monitor"
print (welcomeStr)



class SerialMonitor(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        