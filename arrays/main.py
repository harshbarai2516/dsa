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

class mediumArrays:

    def reverseArray(self, arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -=1

    def rotateLeftk(self, arr, k):
        n = len(arr)
        k %= n

        self.reverseArray(arr, 0 , k - 1)
        self.reverseArray(arr, k , n - 1)
        self.reverseArray(arr, 0 , n-1)

    def merge2sortedarr(self, arr1, arr2):
        union = []
        i, j = 0, 0

        while i < len(arr1) and j < len(arr2):

            if arr1[i] < arr2[j]:
                val = arr1[i]
                i += 1

            elif arr[i] > arr2[j]:
                val = arr2[j]
                j += 1

            else:
                val = arr[i]
                i += 1
                j+= 1

            if not  union or union[-1] != val:
                union.append(val)

        while i < len(arr1):
            if not union or union[-1] != arr1[i]:
                union.append(arr1[i])
                i += 1


        while j < len(arr2):
            if  not union or union[-1] != arr2[j]:
                union.append(arr2[j])
                j += 1

        return union

    def intersectionArr(self, arr1, arr2):

        i , j = 0, 0
        intersection = []

        while i < len(arr1) and j < len(arr2):

            if arr1[i] < arr2[j]:
                i += 1

            elif arr1[i] > arr2[j]:
                j += 1

            else:

                if not intersection or intersection[-1] != arr1[i]:
                    intersection.append(arr1[i])
                i += 1
                j += 1

        return intersection

    def majorityElement(self, arr):
        candidate = None
        count = 0

        for val in arr:
            if count == 0:
                candidate = val

            if val == candidate:
                count += 1

            else:
                count -= 1




arr = [1,5,7,3,5,9,8]

arr1 = [1,5,7,3,5,9,8]
arr2 = [1,9,17,13]

k = 2
sol = learnArrays()
sol.linersearch(arr, k)
#print(sol.linersearch(arr, k))

solut= mediumArrays()

print(solut.intersectionArr(arr1, arr2))
