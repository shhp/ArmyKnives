import commands
import sys

if (len(sys.argv) < 2):
	print("Missing argument: need a directory or file name!")
else:
	directory = sys.argv[1]
	files = commands.getstatusoutput("find "+directory)[1].split("\n")
	lineCounts = 0
	for file in files:
		output = commands.getstatusoutput("wc -l " + file)[1]
		if "Is a directory" not in output \
		    and "No such file or directory" not in output:
			try:
				lineNumber = int(output.strip().split(" ")[0]) + 1
				lineCounts += lineNumber		    
			except Exception as e:
				print(output)

	print("total line:"+str(lineCounts))
