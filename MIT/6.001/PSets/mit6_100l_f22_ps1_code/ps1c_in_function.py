def part_c(initial_deposit):
	#########################################################################
	cost_of_dream_home = 800000
	portion_down_payment = 0.25
	down_payment = cost_of_dream_home * portion_down_payment
	months = 36
	epsilon = 100
	high = 1
	low = 0
	steps = 0
	r = 1
	
	while(True):
			amount_saved = initial_deposit * (1 + r / 12) ** months
			if (amount_saved >= down_payment + epsilon):
				high = r
			elif (r >= 1):
				r = None
				break
			elif (amount_saved < down_payment - epsilon):
				low = r
			else:
				break
			r = (high + low) / 2
			steps += 1
	##################################################################################################
	## Determine the lowest rate of return needed to get the down payment for your dream home below ##
	##################################################################################################
	return r, steps