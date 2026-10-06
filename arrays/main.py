class learnArrays:
    def linersearch(self, arr, k):
        for i in range(len(arr)):
            if arr[i] == k:
                return i

        return -1

    def largestElement(self, arr):

        largest = arr[0]
        for i, val in enumerate(arr):
            if val > largest:
                largest = val

        return largest

    def secondlargestElement(self, arr):
        slargest = float('-inf')
        largest = 0
        for i , val in enumerate(arr):
            if val > largest:
                slargest = largest
                largest = val

            elif val > slargest and val != largest:
                slargest = val
                

        return slargest

    def maximum1(self, arr):
        count = 0
        maxCount  = 0

        for val in arr:
            if val == 1:
                count += 1
                maxCount = max(maxCount, count)
            else:
                count = 0

        return maxCount

    def rotatearrleft(self, arr):
            temp = arr[0]

            for i in range(1, len(arr)):
                arr[i-1] = arr[i]

            arr[len(arr) - 1] = temp

            return arr            

    def moveZeros(self, arr):
        j = 0
        for i in range(len(arr)):
            if  arr[i] != 0:
                arr[j], arr[i] = arr[i], arr[j]
                j+= 1

        return arr

    def removeDuplicates(self, arr):
        i = 0
        for j in range(1, len(arr)):
            if arr[j] != arr[i]:
                i+= 1
                arr[i] = arr[j]

        return i + 1

    def missingNumber(self, arr, n):

        expectedSum = n * (n+1) // 2
        actualSum = sum(arr)  

        return expectedSum - actualSum

    def twoSum( self, arr, target):

        mp = {}

        for i , val in enumerate(arr):

            needed = target - val

            if needed in mp:
                return [mp[needed], i]

            mp[arr] = i




arr = [1,5,7,3,5,9,8]
k = 7
sol = learnArrays()
sol.linersearch(arr, k)
print(sol.linersearch(arr, k))

