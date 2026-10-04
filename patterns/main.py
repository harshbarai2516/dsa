class Solution:
    def pattern1(self, n):
        for i in range(n):
            print("*" * n)

    def pattern2(self, n):
        for i in range(1, n + 1):
            print("*" * i)

    def pattern3(self, n):
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                print(j, end="")
            print()

    def pattern4(self, n):
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                print(i, end="")
            print()

    def pattern5(self, n):
        for i in range(n, 0, -1):
            print("*" * i)

    def pattern6(self, n):
        for i in range(n, 0, -1):
            for j in range(1, i + 1):
                print(j, end="")
            print()

    def pattern7(self, n):
        for i in range(n):
            for j in range(n, i, -1):
                print(" ", end="")

            for j in range(i + 1):
                print("*", end="")

            for j in range(i):
                print("*", end="")
            print()

    def pattern8(self, n):
        for i in range(n):
            for j in range(i):
                print(" ", end="")

            for j in range(n, i, -1):
                print("*", end="")

            for j in range(n - 1, i, -1):
                print("*", end="")

            print()

    def pattern9(self, n):
        for i in range(n):
            for j in range(n, i, -1):
                print(" ", end="")

            for j in range(i + 1):
                print("*", end="")

            for j in range(i):
                print("*", end="")

            print()

        for i in range(n):
            for j in range(i + 1):
                print(" ", end="")

            for j in range(n, i, -1):
                print("*", end="")

            for j in range(n - 1, i, -1):
                print("*", end="")

            print()

    def pattern10(self, n):

        for i in range(n):
            for j in range(i + 1):
                print("*", end="")
            print()

        for i in range(n - 1, 0, -1):
            for j in range(i):
                print("*", end="")
            print()

    def pattern11(self, n):

        for i in range(1, n + 1):
            start = 1 if i % 2 != 0 else 0

            for j in range(i):
                print(start, end="")
                start = 1 - start

            print()

    def pattern12(self, n):
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                print(j, end="")

            for j in range(n + 1, i, -1):
                print(" ", end="")

            for j in range(n, i, -1):
                print(" ", end="")

            for j in range(i, 0, -1):
                print(j, end="")
            print()

    def pattern13(self, n):
        k = 1
        for i in range(n):
            for j in range(i + 1):
                print(k, end=" ")
                k += 1
            print()

    def pattern14(self, n):

        for i in range(1, n + 1):
            for j in range(i):
                print(chr(65 + j), end=" ")
            print()

    def pattern15(self, n):
        for i in range(1, n + 1):
            for j in range(n + 1, i, -1):
                print(chr(70 - j), end=" ")
            print()

    def pattern16(self, n):
        for i in range(n):
            for j in range(i + 1):
                print(chr(65 + i), end=" ")
            print()

    def pattern17(self, n):
        for i in range(n):
            for j in range(n, i, -1):
                print(" ", end="")

            for j in range(i + 1):
                print(chr(65 + j), end="")

            for j in range(i - 1, -1, -1):
                print(chr(65 + j), end="")
            print()

    def pattern18(self, n):
        for i in range(1, n + 1):
            for j in range(i - 1, -1, -1):
                print(chr(68 - j), end=" ")
            print()

    def pattern19(self, n):

        for i in range(n):
            for j in range(n, i, -1):
                print("*", end="")

            for j in range(i):
                print(" ", end="")

            for j in range(i):
                print(" ", end="")

            for j in range(n, i, -1):
                print("*", end="")
            print()

        for i in range(n):
            for j in range(i + 1):
                print("*", end="")

            for j in range(n - 1, i, -1):
                print(" ", end="")

            for j in range(n - 1, i, -1):
                print(" ", end="")

            for j in range(i + 1):
                print("*", end="")
            print()

    def pattern20(self, n):
        for i in range(n):
            for j in range(i + 1):
                print("*", end="")

            for j in range(n - 1, i, -1):
                print(" ", end="")

            for j in range(n - 1, i, -1):
                print(" ", end="")

            for j in range(i + 1):
                print("*", end="")

            print()

        for i in range(n):
            for j in range(n-1, i, -1):
                print("*", end="")

            for j in range(i+1):
                print(" ", end="")

            for j in range(i+1):
                print(" ", end="")

            for j in range(n-1, i, -1):
                print("*", end="")

            print()

    def pattern21(self, n):
        for i in range(n):
            for j in range(n):
                if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()

sol = Solution()

sol.pattern21(2)
