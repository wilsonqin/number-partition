import sys
import karmarkar

if not sys.argv:
  print "error no arguments provided"
elif sys.argv[1]:
  f = open(sys.argv[1], "r")
  num_arr = [int(line.strip()) for line in f]
  print karmarkar.run(num_arr)