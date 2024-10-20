if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print(student_marks)
    print(student_marks[query_name])
    sum = 0
    for i in range(len(student_marks[query_name])):
        sum = sum + student_marks[query_name][i]
    avarage = sum / len(student_marks[query_name])
    print(format(avarage, ".2f"))
