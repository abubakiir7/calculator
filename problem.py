import sys
fl = open('out.txt','w+')
sys.stdout = fl
for i in range(10):
	print('h')