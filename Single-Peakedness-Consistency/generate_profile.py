def generate_candidates(nb_candidate, content):
	"""
	Generates a list of candidates 
	
	:param values: 
		nb_candidate (int): number of candidates
		content (list): lines of '.soc' file
	:return: 
		list_of_candidates (list): a list of candidates
	"""
	list_of_candidates = []
	for i in range(nb_candidate):
		element = content.pop(0).split(',')
		list_of_candidates.append((element[0], element[1]))
	return list_of_candidates
		
def generate_vote_summary(content):
	"""
	Generates the summary of votes
	
	:param values: 
		content (list): lines of '.soc' file
	:return: 
		i (int): number of voters
		j (int): sum of vote count
		k (int): number of unique orders
	"""
	element = content.pop(0).split(',')
	i, j, k = int(element[0]), int(element[1]), int(element[2])
	return i, j, k
	
def generate_preferences(nb_candidate, nb_unique_orders, content):
	"""
	Generates a list which contains lists of weight and preferences
	
	:param values: 
		content (list): lines of '.soc' file
	:return: 
		list_weight_preferences (list): a list of lists of weight and preferences(list)
	"""
	list_weight_preferences = []
	for i in range(nb_unique_orders):
		element = content.pop(0).split(',')
		preference = []
		for j in range(1, nb_candidate + 1):
			preference.append(element[j])
		list_weight_preferences.append([int(element[0]), preference])
	return list_weight_preferences

def generate_profile(content):
	"""
	Generates a dictionary which contains all the information of the profile 
	
	:param values: 
		content (list): lines of '.soc' file
	:return: 
		profile (dict): a dictionary of profile
	"""
	profile = {}
	
	nb_candidate = int(content.pop(0))
	profile["nb_candidate"] = nb_candidate
	
	list_of_candidates = generate_candidates(nb_candidate, content)
	profile["list_of_candidates"] = list_of_candidates
	
	nb_voters, sum_votecount, nb_unique_orders = generate_vote_summary(content)
	profile["nb_voters"] = nb_voters
	profile["sum_votecount"] = sum_votecount
	profile["nb_unique_orders"] = nb_unique_orders
	
	list_weight_preferences = generate_preferences(nb_candidate, nb_unique_orders, content)
	profile["list_weight_preferences"] = list_weight_preferences
	
	return profile
	