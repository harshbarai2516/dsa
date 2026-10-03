class Solution:

    def pattern1(self, n):
        for i in range(n):
            print("*" *  n)

    def pattern2(self, n):
        for i in range(1, n + 1):
            print("*" * i)

    def pattern3(self, n):
        for i in range(1,n+1):
            for j in range(1,i+1):
                print(j, end="")
            print()

    def pattern4(self, n):
        for i in range(1, n +1):
            for j in range(1, i + 1):
                print(i, end="")
            print()

    def pattern5(self, n):
        for i in range(n, 0, -1):
            print("*" * i)


    def pattern6(self, n):
        for i in range(n , 0, -1):
            for j in range(1,i+1):
                print(j, end="")
            print()

    def pattern7(self, n):
        for i in range(n):
            for j in range(n ,i,-1):
                print(" ",end="")

            for j in range(i+1):
                print("*",end="")

            for j in range(i):
                print("*",end="")
            print()

    def pattern8(self, n):
        for i in range(n):

            for j in range(i):
                print(" " , end="")

            for j in range(n, i,-1):
                print("*", end="")

            for j in range(n-1, i,-1):
                print("*", end="")

            print()


    def pattern9(self, n):
        for i in range(n):

            for j in range(n, i, -1):
                print( " ", end="")

            for j in range(i+1):
                print("*", end="")

            for j in range(i):
                print("*", end="")

            print()

        for i in range(n):

            for j in range(i+1):
                print(" ", end="")

            for j in range(n , i,-1):
                print("*", end="")

            for j in range(n-1, i,-1):
                print("*", end="")

            print()

    def pattern10(self,n):

        for i in range(n):
            for j in range(i+1):
                print("*",end="")
            print()

        for i in range(n-1, 0,-1):
            for j in range(i):
                print("*",end="")
            print()



sol = Solution()

sol.pattern11(4);