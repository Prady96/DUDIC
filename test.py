def factorial(number, factorial = 1):
    for i in range(number+1):
        factorial = factorial * i
    print('factorial of ', number, 'is', factorial)

def main():
    try:
        factorials = int(input('Enter a factorial number'))
        # factorials = 1
        end_number = int(input('Enter a number'))
        # end_number = 3
        factorial(end_number, factorials)
    except:
        print('number or factorial cannot have 0')