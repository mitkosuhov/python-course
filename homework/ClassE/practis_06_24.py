numbers = [1, 2, 3, 4, 5, 6, 7]
number = 10 

def check_number(x, y):
    x_len = len(x)
    for i in range(x_len):
        for j in range(i + 1, x_len):
            if x[i] + x[j] == y:
                print(x[i], x[j])

check_number(numbers, number)
