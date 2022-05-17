'''
The algo_isSP algorithm is developped based on the paper 'Single-peaked consistency
and its complexity' by Bruno Escoffier, Jérôme Lang and Meltem Oztürk (2008)
'''


import copy

def verify_singlepeaked(axis, list_of_preferences):
	"""
	Verifies whether a list of preferences is single-peaked with respect to 
	an axis
	
	:param values: 
		axis (list/tuple)): a list of candidates
		list_of_preferences (list): a list of preferences(list)
	:return: 
		isSP (bool): True if single-peaked and False if not
	"""
	isSP = True
	i = 0
	while i < len(list_of_preferences) and isSP:
		preference = list_of_preferences[i]
		index_first_candidate = axis.index(preference[0])
		pointer_left = index_first_candidate
		pointer_right = index_first_candidate
		
		j = 1
		while j < len(preference) and isSP: 
			index_candidate = axis.index(preference[j]) 
			if index_candidate < pointer_left:
				pointer_left = index_candidate
			elif index_candidate > pointer_right:
				pointer_right = index_candidate
			else:
				isSP = False 
			j += 1
		i += 1
	return isSP


def algo_isSP(list_weight_preferences):
	"""
	Verifies whether a profile is single-peaked and find a compatible axis
	if it is single-peaked
	
	:param values:
		list_weight_preferences: a list of lists of weight and preferences(list)
	:return: 
		isSP (bool): True if single-peaked and False if not
		axis (list): a list of compatible axis if single-peaked and None if not
	"""
	isSP = True
	end_flag = False
	axis = None
	right_axis, left_axis = [], []
	x_i, x_j = None, None
	
	# generates list of preferences without the weight
	list_of_preferences =[]
	for weight_preference in list_weight_preferences:
		list_of_preferences.append(weight_preference[1])
	
	# list_of_preferences_SP: list to modify
	list_of_preferences_SP = copy.deepcopy(list_of_preferences)
	
	iteration = 0
	while isSP and len(list_of_preferences_SP[0]) >= 1 and not end_flag:
		
		# make a list of last candidates
		last_candidates = []
		for preference in list_of_preferences_SP:
			last_candidate = preference.pop()
			if last_candidate not in last_candidates:
				last_candidates.append(last_candidate)
			
				
		if len(last_candidates) >= 3: # impossible to position all candidates in leftmost and rightmost axis
			isSP = False
			end_flag = True
			
		elif len(last_candidates) == 1: 
			x = last_candidates[0]
			for preference in list_of_preferences_SP:
				if x in preference:
					preference.remove(x)
			
			case = 0
			
			for i in range(len(list_of_preferences)):
			
				# find index of x, x_i, x_j in each preference
				index_x = list_of_preferences[i].index(x)
				if x_i == None:
					index_x_i = -1
				else:
					index_x_i = list_of_preferences[i].index(x_i)
				if x_j == None:
					index_x_j = -1
				else: index_x_i = list_of_preferences[i].index(x_j)
	
				# 3 possibilities for len(last_candidates) == 1
				if index_x_i > index_x > index_x_j: # Case 1
					case_i = 1
					if case == 0:
						case = case_i
					elif case == 1:
						pass
					elif case == 2:
						end_flag = True
						isSP = False # contradiction
						break
				elif index_x_j > index_x > index_x_j: # Case 2
					case_i = 2
					if case == 0:
						case = case_i
					elif case == 2:
						pass
					elif case == 1:
						end_flag = True	
						isSP = False # contradiction
						break
				elif index_x > index_x_i and index_x > index_x_j: # Case 0
					case_i = 0
			
			# add x in leftmost or rightmost axis according to case if axis is compatible 
			if not end_flag:
				if case == 0:
					left_axis.append(x)
					x_i = x
				elif case == 1:
					left_axis.append(x)
					x_i = x
				elif case == 2:
					right_axis.insert(0, x)
					x_j = x
				
		elif len(last_candidates) == 2:
			x = last_candidates[0]
			y = last_candidates[1]
			for preference in list_of_preferences_SP:
				if x in preference:
					preference.remove(x)
				if y in preference:
					preference.remove(y) 
					
			case = 0
			
			for i in range(len(list_of_preferences)):
			
				# find index of x, y, x_i, x_j in each preference
				index_x = list_of_preferences[i].index(x)
				index_y = list_of_preferences[i].index(y)
				
				if x_i == None:
					index_x_i = -1
				else:
					index_x_i = list_of_preferences[i].index(x_i)
				if x_j == None:
					index_x_j = -1
				else: index_x_j = list_of_preferences[i].index(x_j)
				
				# swap position to put x in the lower position (ranked last)
				if index_y > index_x:
					index_x, index_y = index_y, index_x
			
				# all possible cases
				if index_x_i > index_x > index_y > index_x_j or index_x_j > index_x > index_y > index_x_i: # Case 4
					case_i = 4
					
					# get index for leftover elements and append them into left axis following increasing order
					T_bar = last_candidates + list_of_preferences_SP[i]
					order = []
					for candidate in T_bar:
						index_candidate = list_of_preferences[i].index(candidate)
						order.append((index_candidate, candidate))
					order.sort(reverse = True)
					for index, candidate in order:
						left_axis.append(candidate)
					
					axis = left_axis + right_axis
					
					isSP = verify_singlepeaked(axis, list_of_preferences) # to be completed , complete right n left axis
					end_flag = True 
					break
					
				elif index_x_i > index_x > index_x_j > index_y: # Case 1
					case_i = 1
					if case == 0:
						case = case_i
					elif case == 1:
						pass
					elif case == 2:
						end_flag = True
						isSP = False # contradiction 
						break
				elif index_x_j > index_x > index_x_i > index_y: # Case 2
					case_i = 2
					if case == 0: 
						case = case_i
					elif case == 2:
						pass
					elif case == 1: 
						end_flag = True
						isSP = False # contradiction 
						break
				elif index_x > index_x_i and index_x > index_x_j: 
					case_i = 0 
					
			# add x and y  in leftmost or rightmost axis according to case if axis is compatible
			
			if not end_flag:
				if case == 0: 
					left_axis.append(x) 
					right_axis.insert(0, y)
					x_i = x 
					x_j = y
				elif case == 1:
					left_axis.append(x) 
					right_axis.insert(0, y)
					x_i = x 
					x_j = y
				elif case == 2: 
					left_axis.append(y) 
					right_axis.insert(0, x)
					x_i = y
					x_j = x
		
		iteration += 1		
	
	if isSP and axis == None: 
		axis = left_axis + right_axis
	
	return isSP, axis