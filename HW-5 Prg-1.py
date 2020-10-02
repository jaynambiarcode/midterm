#Example-1

def my_range(start,end): 
	x = start
	while x < end:
		yield x 
		x = x + 1
for i in my_range(0,5):
	print(i)


#Example2:
def my_range(start, end, step):
    while start <= end:
        yield start
        start += step
for i in my_range(0,5,2):
	print(i)