#
# Simple mock object for the GPIO module, allows to test the code
# without executing it on an actual Raspberry Pi
#

BOARD = "BOARD"
IN = "INPUT"
OUT = "OUTPUT"


def setmode(mode):
    print("Set mode {0!s}".format(mode))


def setwarnings(mode):
    print("Set warnings as {0!s}".format(mode))


def setup(pin, mode):
    print("Set pin {0!s} as {1!s}".format(pin, mode))


def output(pin, value):
    print("Output {0!s} to pin {1!s}".format(value, pin))


def input(pin):
    print("Input 0 to pin {0!s}".format(s))
    return 0


def cleanup():
    print("Cleanup done")
