# 
# Simple mock object for the GPIO module, allows to test the code
# without executing it on an actual Raspberry Pi
#

BOARD = "BOARD"
IN = "INPUT"
OUT = "OUTPUT"

def setmode(mode):
    print("Set mode %s" % mode)

def setwarnings(mode):
    print("Set warnings as %s" % mode)

def setup(pin, mode):
    print("Set pin %s as %s" % (pin, mode))

def output(pin,value ):
    print("Output %s to pin %s" % (value,pin))

def input(pin):
    print("Input 0 to pin %s" % s)
    return 0

def cleanup():
    print("Cleanup done")
