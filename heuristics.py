import random
import math

MAX_ITER = 25000
ARR_LEN = 100
RAND_MAX = ARR_LEN - 1

#calculate residue
def residue(A, S):
	u = 0
	for i in range(0, ARR_LEN):
		u += S[i]*A[i] 
	return int(math.fabs(u))


#"cooling schedule"
def T(iterator):
	return pow(10,10)*pow(0.8, (iterator/300))

#######################


#finds neighbor_standard of s
def neighbor_standard(S):
	#pick a random place to switch the sign in S
	index = random.randint(0, RAND_MAX)
	S[index] = (-1)*S[index]
	
	#with probability 1/2 switch a different index too.
	coin = random.choice((0,1))
	
	#if coin == 0 then don't switch sign, if coin == 1 switch sign
	#of another index, as long as new_index != index
	if(coin == 0):
		return S
	if(coin == 1):
		#maybe should use dowhile loop
		new_index = random.randint(0, RAND_MAX)
		if(new_index != index):
			S[new_index] = (-1)*S[new_index]
		return S
			
#######################			
			
			
#generates a random solution
def generate_random():
	solution = [];
	for i in range (0,ARR_LEN):
		num = random.choice((-1,1))
		solution.append(num)
	return solution

#######################

#prepartitioning to find a solution s		
def prepartition(A):	
	#initialize p - partition array
	#and initialize A' with all 0's
	p = []
	a_prime = []
	for i in range(0, ARR_LEN):
		num = random.randint(0, RAND_MAX)
		p.append(num)
		a_prime.append(0)

	#now update A' so that it is a sum
	for j in range (0, ARR_LEN):
		a_prime[p[j]] += a[j]
	return

#######################

#for all of these what is max_iter to be set to?
#Repeated Random Algorithm for Standard Representation.
def rep_rand_standard(A, sol):
	for iter in range (1, MAX_ITER):
		s_prime = generate_random()
		if (residue(A, s_prime) < residue(A, sol)):
			sol = s_prime
	return sol


#######################

#Hill Climb Algorithm for Standard Representation
def hill_climb(A, sol):
	for i in range (1, MAX_ITER):
		s_prime = neighbor_standard(sol)
		if(residue(A, s_prime) < residue(A, sol)):
			sol = s_prime
	return sol

#######################


#Simulated Annealing for Standard Representation
def sim_anneal(A, sol):
	s_dprime = sol
	for i in range(1, MAX_ITER):
		s_prime = neighbor_standard(sol)
		if(residue(A, s_prime) < residue(A, sol)):
			sol = s_prime
		elif math.exp(-(residue(A, s_prime) - residue(A, sol))/T(i)):
			# with probability exp(-res(s_prime) - res(sol)/T(iter)
			sol = s_prime
		if(residue(A, sol) < residue(A, s_dprime)):
			s_dprime = sol
	return s_dprime
			

#######################

f = open("test_files/test1.txt", "r")
num_arr = [int(line.strip()) for line in f]

print residue(num_arr, rep_rand_standard(num_arr, generate_random()))
print residue(num_arr, hill_climb(num_arr, generate_random()))
print residue(num_arr, sim_anneal(num_arr, generate_random()))