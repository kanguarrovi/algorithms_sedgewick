import sys


if __name__ == '__main__':
    sum = 0.0
    counter = 0
    while True:
        input_var = input()
        if input_var == "q":
            break
        sum += float(input_var)
        counter += 1
    avg = sum/counter
    print(f'Average is {avg}')
