import random
import math

#calculate residue
def residue(A, S):
	u = 0
	for i in range(0, 5):
		u += S[i]*A[i] 
	return math.fabs(u)

#######################


#finds neighbor_standard of s
def neighbor_standard(S):
	#pick a random place to switch the sign in S
	index = random.randint(0, 100)
	S[index] = (-1)*S[index]
	
	#with probability 1/2 switch a different index too.
	coin = random.choice((0,1))
	
	#if coin == 0 then don't switch sign, if coin == 1 switch sign
	#of another index, as long as new_index != index
	if(coin == 0):
		return S
	if(coin == 1):
		#maybe should use dowhile loop
		new_index = random.randint(0, 100)
		if(new_index != index):
			S[new_index] = (-1)*S[new_index]
			return S
			
#######################			
			
			
#generates a random solution
def generate_random():
	solution = [];
	for i in range (0,100):
		num = random.choice((-1,1))
		solution.append(num)
	return solution

#######################

#prepartitioning to find a solution s		
def prepartition():	
	p = []
	for i in range(0, 100):
		num = random.randint(1, 100)
		p.append(num)
	#A'
	a_prime = []
	for j in range (0, 100):
		#a_pj = a_pj + 
		#not sure what to do here
		#a_prime.append()

#######################

#for all of these what is max_iter to be set to?
#Repeated Random Algorithm for Standard Representation.
def rep_rand_standard(A, sol):
	for iter in range (1, max_iter):
		s_prime = generate_random()
		if (residue(A, s_prime) < residue(A, sol)):
			sol = s_prime
	return sol


#######################

#Hill Climb Algorithm for Standard Representation
def hill_climb(A, sol):
	for i in range (1, max_iter):
		s_prime = neighbor_standard(sol)
		if(residue(A, s_prime) < residue(A, sol)):
			sol = s_prime
	return sol

#######################


#Simulated Annealing for Standard Representation
def sim_anneal(A, sol):
	s_dprime = sol
	for i in range(1, max_iter):
		s_prime = neighbor_standard(sol)
		if(reside(A, s_prime) < residue(A, sol)):
			sol = s_prime
		else:
			# with probability exp(-res(s_prime) - res(sol)/T9iter)
			sol = s_prime
		if(residue(A, sol) < residue(A, s_dprime):
			s_dprime = sol
	return s_dprime
			

#######################
			