import numpy as np

#creating 1D numpy array
arr1 = np.array([1,2,3,4,5])

print(arr1)

#creating a 2d array
arr2 = np.array([[1,2,3],[4,5,6]])
print(arr2)

#creating a 3d array
arr3=np.array([
  [[1,2,3],[4,5,6]],
  [[7,8,9],[10,11,12]],
  [[2,4,5],[4,5,6]]
])
print(arr3)

arr3d_2=np.array([
  [[1,2,3],[4,5,6]],
  [[7,8,9],[10,11,12]],
  [[2,4,5],[4,5,6]]
])

array_sum=arr3+arr3d_2
print('the sum of two array is:')
print(array_sum)

zero=np.zeros((3,3))
print(zero)

one_arr=np.ones((4,4))
print(one_arr)

random_matrix=np.random.random((4,4))
print(random_matrix)

#array operator
#array operator is used to calculate between arrat
arr1=np.array([1,2,3])
arr1=np.array([3,3,2])
sum_array=arr1+arr1
print(sum_array)

sub_array=arr1-arr1
print(sub_array)

mul_array=arr1*arr1
print(mul_array)

div_array=arr1/arr1
print(div_array)

#slicing array
slic =np.array([2,3,4,5,1])
"""
  to slic data up to 3rd index from 0 so it will reach upto 2nd index counting up to three data
  """
print(slic[:3])

re_array=np.array([2,3,6,19,78,27])
re_shared_array=re_array.reshape((2,3))
print(re_shared_array)

re_array=np.array([20,30,60,19,78,27,40,87])
re_shared_array=re_array.reshape((2,4))
print(re_shared_array)

#to aggrefrate data in numpy we use its function such as sum,mean,std
example_arr=np.array([30,40,50,60,70])
print(example_arr)

#mean
mean_arr=np.mean(example_arr)
print(mean_arr)

#std deviation
std_arr=np.std(example_arr)
print(std_arr)

#maximum value
 