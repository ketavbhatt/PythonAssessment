# Given array element
array = [ 15, 25, 35, 45 ] 

# Number to find
num = 45




def binarySearch (array, i, j, num): 

      if j >= i: 

            m = int(i + (j - i)/2)

            # Found element in the middle itself 
            if array[m] == num: 
                  print("Element Found At Index", m)

            # If element is smaller than middle element, find left subarray
            elif array[m] > num: 
                  return binarySearch(array, i, m-1, num) 

            # Since element is greater than middle element, find right subarray
            else: 
                  return binarySearch(array, m + 1, j, num)

      else:
            raise Exception("Element Not Found")





binarySearch(array, 0, len(array)-1, num)
