import random
import math
import karmarkar

# write to file

MAX_ITER = 25000
ARR_LEN = 100
RAND_MAX = ARR_LEN - 1

#calculate residue
def residue(A, S):
	u = 0
	for i in range(0, ARR_LEN):
		u += S[i]*A[i]
	return math.fabs(u)


#"cooling schedule"
def T(iterator):
	return pow(10,10)*pow(0.8, (iterator/300))

#######################


#finds neighbor_standard of s
def neighbor_standard(input):
	#pick a random place to switch the sign in S
	S = list(input)
	index = random.randint(0, RAND_MAX)
	S[index] = (-1)*S[index]
	assert (input[index] != S[index])
	
	#with probability 1/2 switch a different index too.
	coin = random.choice((0,1))
	
	#if coin == 0 then don't switch sign, if coin == 1 switch sign
	#of another index, ensure new_index != index
	if(coin == 0):
		return S
	if(coin == 1):
		#maybe should use dowhile loop
		new_index = random.randint(0, RAND_MAX)
		while (new_index == index):
			new_index = random.randint(0, RAND_MAX)
		S[new_index] = (-1) * S[new_index]
		assert (S[index] != input[index])
		assert (S[new_index] != input[new_index])
		return S
			
#######################			
			
			
#generates a random solution
def generate_random():
	solution = []
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
	sol = []
	for i in range(0, ARR_LEN):
		num = random.randint(0, RAND_MAX)
		p.append(num)
		a_prime.append(0)
		sol.append(0)

	#now update A' so that it is a sum
	for j in range (0, ARR_LEN):
		a_prime[p[j]] += A[j]

	sol_part = generate_random()
	for k in range (0, ARR_LEN):
		sol[k] = sol_part[p[k]]
	
	return (a_prime, sol)

#######################

#for all of these what is max_iter to be set to?
#Repeated Random Algorithm for Standard Representation.
def rep_rand_standard(A, starting_sol):
	sol = starting_sol
	for iter in range (1, MAX_ITER):
		s_prime = generate_random()
		if (residue(A, s_prime) < residue(A, sol)):
			sol = list(s_prime)
	return sol


#######################

#Hill Climb Algorithm for Standard Representation
def hill_climb(A, starting_sol):
	sol = list(starting_sol)
	for i in range (1, MAX_ITER):
		s_prime = neighbor_standard(sol)
		if(residue(A, s_prime) < residue(A, sol)):
			sol = list(s_prime)
	return sol

#######################


#Simulated Annealing for Standard Representation
def sim_anneal(A, starting_sol):
	#annealcount = 0
	sol = list(starting_sol)
	s_dprime = list(sol)
	for i in range(1, MAX_ITER):
		s_prime = neighbor_standard(sol)
		if(residue(A, s_prime) < residue(A, sol)):
			sol = list(s_prime)
		elif random.random() <= math.exp(-(residue(A, s_prime) - residue(A, sol))/T(i)):
			# with probability exp(-res(s_prime) - res(sol)/T(iter)
			#annealcount += 1
			sol = list(s_prime)
		if(residue(A, sol) < residue(A, s_dprime)):
			s_dprime = list(sol)
	#print "annealing: ", annealcount
	return s_dprime
			

#######################

for count in range (1,51):
	f = open("test_files/test"+str(count)+".txt", "r")
	num_arr = [int(line.strip()) for line in f]

	kk = str(karmarkar.run(list(num_arr)))

	r1 = str(residue(num_arr, rep_rand_standard(num_arr, generate_random())))
	r2 = str(residue(num_arr, hill_climb(num_arr, generate_random())))
	r3 = str(residue(num_arr, sim_anneal(num_arr, generate_random())))

	p_num_arr, p_sol = prepartition(num_arr)
	p1 = str(residue(p_num_arr, rep_rand_standard(p_num_arr, p_sol)))
	p2 = str(residue(p_num_arr, hill_climb(p_num_arr, p_sol)))
	p3 = str(residue(p_num_arr, sim_anneal(p_num_arr, p_sol)))

	print str(count) + "," + kk + "," + r1 + "," + r2 + "," + r3 + "," + p1 + "," + p2 +"," + p3
