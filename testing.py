
arr=[1,2,3,4,5,6,7,8,9,10,10]

def first_dup(array):
	arr1=array
	temp_arr=list()
	#check_arr=list()

	arrl=len(array)-1

	i=0

	while i<= arrl:
		temp_arr.append(array[0])
		array.remove(array[0])

		if array[0] in temp_arr:
			print('first duplicate found :',array[0])
			break

		i=i+1




 	

first_dup(arr)
