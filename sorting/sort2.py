import random
import sys
import time

def sorting(nums):
	length = len(nums) - 1
	if length != 1:
		for i in range(100000):
			for i in range(length):
				if nums[i] > nums[i+1]:
					nums[i], nums[i+1] = nums[i+1], nums[i]
	return nums

def sortedcheck(nums):
	length = len(nums) - 1
	if length != 1:
		for i in range(length):
			if nums[i] > nums[i+1]:
				return False
				break	
		return True
#python command line arguments, how to pass num of lists and len of each list on command line
#function for generating lists
#print num of list generated
#length of each list
#how many lists sorted correctly, fraction correct
#get length of list and num of lists from command line
#find out how long sorting takes,take time before sorting after sorting
#python time module, python numpy module 

args = sys.argv[1:]
num = int(args[0])
length = int(args[1])
correct = []
start = time.time()
for i in range(num):
        list = []
        for i in range(length):
                x = random.randint(1,10000)
                list.append(x)
        result = sorting(list)
        check = sortedcheck(result)
        if check == False:
                print("sorting failed")
        if check == True:
                correct.append('x')
final_num = str(num)
end = time.time()
num_correct = len(correct)
fraction_correct = (num_correct/num)
final_fraction_correct = str(fraction_correct)
print("total number of lists sorted:" + final_num)
print("fraction of lists sorted correctly:" + final_fraction_correct)
print(f"Time to run program is [secs]{end - start}")


