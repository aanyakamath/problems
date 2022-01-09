import random
import sys
import time
import matplotlib.pyplot as plt
def sorting(nums):
	length = len(nums) - 1
	if length != 1:
		for i in range(10000):
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
x = []
y = []
for i in range(1,5):
	list_len = 2**i
	x.append(list_len)
	list = []
	for i in range(list_len):
		num = random.randint(1,10000)
		list.append(num)
	start = time.time() 
	result = sorting(list)
	end = time.time()
	time_lapse = end - start
	y.append(time_lapse)


x2 = []
y2 = []
num_items_list = 10
time_count = 0
for i in range(1,5):
	num_lists = 2**i
	x2.append(num_lists)
	list = []
	for j in range(num_lists):
		for k in range(num_items_list):
			num = random.randint(1,10000)
			list.append(num)
		start = time.time()
		result = sorting(list)
		end = time.time()
		time_lapse = end - start
		time_count = time_count + time_lapse
	y2.append(time_count)
		
print(x[0], y[0])
print(x[1], y[1])
print(x[2], y[2])
print(x[3], y[3])

plt.plot(x,y)
plt.xlabel('length of list')
plt.ylabel('time it takes to sort list')
plt.title('Length of list vs Time it takes to sort list')
plt.show()

plt.clf()

print(x2[0], y2[0])
print(x2[1], y2[1])
print(x2[2], y2[2])
print(x2[3], y2[3])
plt.plot(x2,y2)
plt.xlabel('num of lists sorted')
plt.ylabel('time it takes to sort lists')
plt.title('Num of lists sorted vs Time it takes to sort lits')
plt.show()
