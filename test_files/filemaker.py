import uuid


# Generate files
def fileMake(f_name):
	path = f_name
	file = open(path, 'w')
	for i in range(0, 100):
		x = uuid.uuid4().int & (1<<64)-1
		file.write(str(x) + '\n')	
		
	file.close()

for i in range(1, 51):
	name = 'test' + str(i) + '.txt'
	fileMake(name)
