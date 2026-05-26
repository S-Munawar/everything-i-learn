def part_b(yearly_salary, portion_saved, cost_of_dream_home, semi_annual_raise):
	#########################################################################
	portion_down_payment = 0.25
	amount_saved = 0.0
	r = 0.05
	months = 0
	
	while (True):
			amount_saved += amount_saved * r / 12
			amount_saved += (yearly_salary / 12) * portion_saved
			months += 1
			if (amount_saved >= cost_of_dream_home * portion_down_payment):
				break
			if (months % 6 == 0):
				yearly_salary += yearly_salary * semi_annual_raise
		
	###############################################################################################
	## Determine how many months it would take to get the down payment for your dream home below ## 
	###############################################################################################
	
	return months