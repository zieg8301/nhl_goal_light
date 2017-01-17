#
# Simple mock object for the GPIO module, allows to test the code
# without executing it on an actual Raspberry Pi
#

BOARD = "BOARD"
IN = "INPUT"
OUT = "OUTPUT"


def setmode(mode):
    print("Set mode {0}".format(mode))


def setwarnings(mode):
    print("Set warnings as {0}".format(mode))


<<<<<<< HEAD
def setup(pin, mode, pull =""):
    print("Set pin {0} as {1} {2}".format(pin, mode, pull))
=======
def setup(pin, mode,pull=""):
    print("Set pin {0} as {1} {3}".format(pin, mode, pull))
>>>>>>> a6739ab2896836db58e44782576083f9404ddd9e


def output(pin, value):
    print("Output {0} to pin {1}".format(value, pin))


def input(pin):
    print("Input 0 to pin {0}".format(pin))
    return 0


def cleanup():
    print("Cleanup done")
