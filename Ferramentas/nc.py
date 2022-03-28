import sys
import getopt
import threading
import _thread
import subprocess

listener = False
cmd= False
send = False
run = ""
target = ""
up_dst = ""
port = ""

def uso ():
    print("Ferramenta NC :")
    print ("Uso : nck.py -t target ")
    print ("-l --listen")
    print ("-e --execute = file_to_run")
    print ("-c --command")
    print ("-u --upload = destino")
    