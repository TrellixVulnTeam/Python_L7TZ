import subprocess
import os
with open(os.devnull, "wb") as limbo:
        for n in xrange(1, 20):
                ip="192.168.2.{0}".format(n)
                result=subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", ip],
                        stdout=limbo, stderr=limbo).wait()
                if result:
                        print ip, "off"
                else:
                        print ip, "online"

