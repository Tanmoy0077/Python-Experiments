def avr(*score):
    val = sum(*score)
    val /= 3
    return val

if __name__ == '__main__':
    # n = int(input())
    # student_marks = {}
    # for _ in range(n):
    #     name, *line = input().split()
    #     scores = list(map(float, line))
    #     student_marks[name] = scores
    # query_name = input()
    print(avr([10,20,30]))