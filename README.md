# ArmyKnives
Some scripts for improving work efficiency or just for fun.

## 1. line_counter.py
Count the total line number of a file or all files in a directory depends on the argument you supply when running the script. E.g.

	python line_counter.py /path/to/the/file or /path/of/a/directory

## 2. launch_perf.py
This script can calculate the time cost in launching an Android `Activity`. E.g.

	python launch_perf.py com.test/.MainActivity 20

The first argument is the component name of the `Activity` and the second argument is how many times you want to launch the `Activity`. The default value is 10 if the second argument is not supplied.

The command will print the time cost of each launch of the `Activity` and at last calculate the average time cost by eliminating the minimum and maximum value.