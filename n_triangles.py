
def print_triangles(height, num_of_tri):

	if height == 0 or num_of_tri == 0:
		return
    
	str_ = ""
	for i in range(height):		
		for j in range(num_of_tri):
			str_+= "*"*(i+1) + " "*(height-1-i)
		str_ += "\n"

	print(str_[:-1])


print_triangles(6, 4) 
