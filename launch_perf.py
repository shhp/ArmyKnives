import commands
import sys
import os
import re

testTimes = 10;
component = "";
if(len(sys.argv) >= 2):
	component = sys.argv[1]
else:
	print("Missing argument: needs a component name")
	exit(0)

if(len(sys.argv) >= 3):
	try:
		testTimes = int(sys.argv[2])
	except Exception as e:
	    pass

indexOfSlash = component.find("/")
if(indexOfSlash < 0):
	print("invalid component name")
	exit(0)
else:
	package = component[:indexOfSlash]

launchCost = []
for i in range(1, testTimes+1):
	os.system("adb shell am force-stop " + package)
	output = commands.getstatusoutput("adb shell am start -W -n " + component)
	match = re.search("TotalTime:\s*(\d+)", output[1])
	print("%d:%sms"%(i, match.group(1)))
	launchCost.append(int(match.group(1)))

launchCost.sort()
totalCost = 0;
for i in range(1, len(launchCost)-1):
	totalCost += launchCost[i]

if(len(launchCost) > 2):
	print("average:%.2fms"%(totalCost * 1.0 / (len(launchCost) - 2)))