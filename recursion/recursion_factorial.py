class Fact:
    def factorial(self, num):
        if num == 1:
            return num
        else:
            return num * self.factorial(num-1)

if __name__ == "__main__":
    num = 5
    obj = Fact()
    print("Factorial of", num, "is", obj.factorial(num))
