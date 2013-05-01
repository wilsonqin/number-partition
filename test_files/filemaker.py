#import uuid
import random

MAX_INT = pow(10, 12)

# Generate files
def fileMake(f_name):
  path = f_name
  file = open(path, 'w')
  for i in range(0, 100):
    #x = uuid.uuid4().int & (1<<64)-1
    x = random.randint(0, MAX_INT)
    file.write(str(x) + '\n')
  file.close()

for i in range(1, 51):
  name = 'test' + str(i) + '.txt'
  fileMake(name)
