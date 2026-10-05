class learnsort:

    def selection_sort(self, arr):
        for i in range(len(arr)):
            minI= i
            for j in range(i+1, len(arr)):
                if arr[j] < arr[minI]:
                    minI = j

            arr[i], arr[minI] = arr[minI], arr[i]

        return arr

    def bubble_Sort(self, arr):
        for i in range(len(arr) - 1):
            for j in range(len(arr) - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j+1] = arr[j+ 1], arr[j]

        return arr

    def insertion_Sort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1

            while j>=0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1

            arr[j+1] = key 

        return arr

    def merge_sort(self, arr):

        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2

        lh = self.merge_sort(arr[:mid])
        rh = self.merge_sort(arr[mid:])

            
        return self.merge(lh , rh)

    def merge(self,l , r):
        result = []

        left = 0
        right = 0

        while left < len(l) and right < len(r):
            if l[left] < r[right]:
                result.append(l[left])
                left+= 1
            else:
                result.append(r[right])
                right+=1

        while left < len(l):
            result.append(l[left])
            left+=1

        while right < len(r):
            result.append(r[right])
            right+=1

        return result

    def quick_sort(self, arr, low, high):

        if low < high:

            pivotI = self.partition(arr, low, high)

            self.quick_sort(arr, low, pivotI - 1)
            self.quick_sort(arr, pivotI + 1, high)


    def partition(self, arr, low, high):

        pivot = arr[low]
        i = low 
        j = high

        while i < j:

            while i <= high and arr[i] <= pivot:
                i+=1

            while j >= low and arr[j] > pivot:
                j-=1

            if i < j :
                arr[i], arr[j] = arr[j], arr[i]

        arr[low], arr[j] = arr[j], arr[low]

        return j

            


             



sol = learnsort()

arr = [8, 3, 1, 7, 0, 10, 2]
#sol.selection_sort(arr)
#sol.bubble_Sort(arr)
sol.quick_sort(arr, 0, len(arr)- 1)
print(arr)