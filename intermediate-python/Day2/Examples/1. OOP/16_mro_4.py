class L2_1:  
	pass

class L2_2:  
	pass

class L1_1(L2_1, L2_2):
    	pass

class L1_2(L2_2, L2_1): 
    	pass

class Child(L1_1, L1_2):  
	pass