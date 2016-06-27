#!/usr/bin/env python
# USAGE for read1: time python phred_stats.py <fastq_file> out1.qual 
# USAGE for read2: time python phred_stats.py <fastq_file> out2.qual 
from sys import argv
import itertools
import tempfile
import time
import os



def getQualLines(input_fastq):
	tmp_output = tempfile.NamedTemporaryFile(delete=True)
	with open(input_fastq) as read:
		num = len(list(itertools.islice(read,3,4))[0])-1
	with open(input_fastq) as read:
		tmp = itertools.islice(read,3,None,4)
		for line in tmp:
			tmp_output.write(line.rjust(num,' '))
		tmp_output.seek(0)
		tmp = itertools.izip(*tmp_output)
	
	return tmp

						

def transpose(tmp_file):
	count = 0
	with open(output, 'w') as out:					
		for line in tmp_file:
			count += 1	
			start = time.time()
	
			avg = getOrd(line)
			avg = sum(avg)/len(avg) - 33
			out.write(str(avg) +'\n')
		
			end = time.time()
			if count % 10 == 0:
				print count, ',' ,avg, 'Time:',(end-start)


def getOrd(lst):
	return [ord(char) for char in lst if char != ' ']
#	return map(ord,lst)

def processPhred(tmp,index):
	return [line[index] for line in tmp]





################################################################################
####                                                                        ####
################################################################################
fastq = argv[1]
output = argv[2]

#tmp_output = getQualLines(fastq)
tmp_output = getQualLines(fastq)
print 'Finished making tmp PHRED file'
transpose(tmp_output)



#time python phred_stats.py seqs.fastq out1.qual &
#time python phred_stats.py seqs.fastq out2.qual


""" Making both scripts run at the same time
time python phred_stats.py read1.fastq out1.qual & PID_R1=$!
time python phred_stats.py read2.fastq out2.qual & PID_R2=$!
wait $PID_R1
wait $PID_R2
"""

""" This is my profiling-timer function 

#Use "@do_cprofile" to time a function
import cProfile
def do_cprofile(func):
    def profiled_func(*args, **kwargs):
        profile = cProfile.Profile()
        try:
            profile.enable()
            result = func(*args, **kwargs)
            profile.disable()
            return result
        finally:
            profile.print_stats()
    return profiled_func
"""
