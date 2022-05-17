import itertools
from algo_singlepeaked import verify_singlepeaked

def division(m, n):
	"""return the division of m by n with 3 decimals"""
	return round(m/n, 3)

def generate_initial_axis(nb_candidates):
	"""
	Generates an initial axis based on the number of candidates 
	
	:param values: 
		nb_candidates (int): number of candidates
	:return: 
		axis (list): an initial axis
	"""
	axis = []
	for i in range(1, nb_candidates+1):
		axis.append(str(i))
	return axis
	


def calc_nearSP(nb_voters, list_weight_preferences):
	"""
	Calculates the proximity to single-peakedness of a profile and the largest
	structuring dimension 
	
	:param values: 
		nb_voters (int): number of voters
		list_weight_preferences (list) : a list of lists of weight and preferences(list)
	:return: 
		proxSP (float): proximity to single-peakedness
		max_axis_SP (tuple): the largest structuring dimension
	"""
	nb_candidates = len(list_weight_preferences[0][1])
	axis = generate_initial_axis(nb_candidates)
	perm_axis = itertools.permutations(axis)
	max_weight_SP = 0
	max_axis_SP = []
	
	for p in perm_axis:
		if p <= p[::-1]:
			m = 0
			for weight_preference in list_weight_preferences:
				isSP = verify_singlepeaked(p, [weight_preference[1]])
				if isSP:
					m += weight_preference[0]
			if max_weight_SP < m:
				max_weight_SP = m
				max_axis_SP = p
	proxSP = division(max_weight_SP, nb_voters)
	return proxSP, max_axis_SP

