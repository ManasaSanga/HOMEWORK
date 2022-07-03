#def two_num_sum_1(num_arr, num_target):
 #   for i in range(len(num_arr) - 1):
  #      for j in range(i + 1, len(num_arr)):
   #         if num_arr[i] + num_arr[j] == num_target:
    #            return [num_arr[i], num_arr[j]]
    #return []


#def two_num_sum_2(num_arr, num_target):
 #   seen = set()
  #  for i in num_arr:
   #     if (num_target - i) in seen:
    #        return [i, num_target - i]
    #    seen.add(i)
   # return []


#print(two_num_sum_1([3, 5, -4, 8, 11, 1, -1, 6], 10))
#print(two_num_sum_2([3, 5, -4, 8, 11, 1, -1, 6], 10))

#def sortSquare(arr, n):

 #   for i in range(n):
  #      arr[i] = arr[i] * arr[i]
   # arr.sort()

# Driver code
#arr = [1,2,3,5,6,8,9]
#n = len(arr)

#print("Before sort")
#for i in range(n):
 #   print(arr[i], end=" ")

#print("\n")

#sortSquare(arr, n)

#print("After sort")
#for i in range(n):
 #   print(arr[i], end=" ")
