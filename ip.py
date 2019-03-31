#https://stackoverflow.com/questions/52179526/host-unreachable-returning-successful
#https://linux.die.net/man/8/ping
#https://stackoverflow.com/questions/5314038/simulating-host-unreachable-how-to-achieve-implement-it
from subprocess import call

def test():
    Output_IP_Address_AN = '1.0.0.0'
    #if call(["ping", "1.0.0.3"]) == 0:

    if call(["ping", "-c", "1", "-W", "4", "1.0.0.3"]) == 0:
        print("'Ping' Sucessful")
    else:
        print("'Ping' NOT Sucessful")

test()