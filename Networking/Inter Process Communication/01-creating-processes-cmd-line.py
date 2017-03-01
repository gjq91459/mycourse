############################################################
#
#    creating processes
#
############################################################

from subprocess import Popen

args = ("python", "childA.py", "Monday", "Tuesday", "Wednesday")
args = ("ls -l".split())
child = Popen(args)
child.wait()
print "child completed"



1