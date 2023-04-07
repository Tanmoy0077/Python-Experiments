def fact(num):
    temp = 1
    for i in range(1, num+1):
        temp *= i
    return temp

def dec(func):
    def greet(num):
        print("<-- The function is called -->")
        # print(func(num))
        # print("<-- The function is terminated -->")
        return func(num)
    return greet

fact = dec(fact)
print(fact(5))
print(fact(4))