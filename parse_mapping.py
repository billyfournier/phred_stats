#!/usr/bin/env python
from sys import argv
import itertools

# USAGE: python parse_mapping.py <mappingfile>

mapping_file = argv[1]
def is_number(string):
	try:
		float(string)
		return True
	except ValueError:
		return False

def is_numeric(lit):
    'Return value of numeric literal string or ValueError exception'
 
    # Handle '0'
    if lit == '0': return 0
    # Hex/Binary
    litneg = lit[1:] if lit[0] == '-' else lit
    if litneg[0] == '0':
        if litneg[1] in 'xX':
            return int(lit,16)
        elif litneg[1] in 'bB':
            return int(lit,2)
        else:
            try:
                return int(lit,8)
            except ValueError:
                pass
 
    # Int/Float/Complex
    try:
        return int(lit)
    except ValueError:
        pass
    try:
		return float(lit)    
    except ValueError:
        pass
	return complex(lit)
    

def mapping(mapping_file):
	tmp = []
	tmp2 = []
	ignore = ['#SampleID','BarcodeSequence','LinkerPrimerSequence'
					,'ReversePrimer','Experiment','Description','PrimerDesc']
	with open(mapping_file) as read:
		header = itertools.islice(read,0,1)
		data = itertools.islice(read,1,None)

		for name, value in zip(header,data):
			header = name
		for index,name in enumerate(header.split()):
			if name not in ignore:
				read.seek(0)
				data = itertools.islice(read,1,None)
				for line in data:
					if line.split('\t')[index]: 
						tmp.append((line.split('\t')[index], name))
						break
						
				
		for item in tmp:
#			print item[0]
			if is_number(item[0]):
#			if item[0].isdigit():
#				print item[0]
				if isinstance(is_numeric(item[0]),int):
					tmp2.append(("Classifier",item[1]))
				if isinstance(is_numeric(item[0]),float):
					tmp2.append(("Numeric",item[1]))
			else:
				tmp2.append(("Classifier",item[1]))
		with open('header.info', 'w') as out:
			for tup in tmp2:
				out.write('\t'.join(map(str,tup)))
				out.write('\n') 
mapping(mapping_file)
