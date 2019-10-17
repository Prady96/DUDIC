

```python
import cmath

def decrement(a, b, c):
  d = (b**2) - (4*a*c)
  return d
```


```python
def quadratic_formula(a, b, c):
    solX = (-b - cmath.sqrt(decrement(a, b, c))) / (2*a)
    solY = (-b + cmath.sqrt(decrement(a, b, c))) / (2*a)

    print('decrement of the function is : ', decrement(a, b, c))
    
    return solX, solY
```


```python
solx, soly = quadratic_formula(1,5,6)
```

    decrement of the function is :  1



```python
print(solx)
```

    (-3+0j)



```python
print(soly)
```

    (-2+0j)



```python
a = input("a: ")
```

    a: 



```python
a = int(input("a: "))
```

    a: 1



```python
factorial = 1
for i in range(1,2):
  factorial = factorial * i
```


```python
print(factorial)
```

    1



```python
for i in range(1, 10):
  print('Hello World {}'.format(i))
```

    Hello World 1
    Hello World 2
    Hello World 3
    Hello World 4
    Hello World 5
    Hello World 6
    Hello World 7
    Hello World 8
    Hello World 9



```python
for i in range(1,10,2):
  print(i, end=" ")
```

    1 3 5 7 9 


```python

```


```python
def recursive_function(number):
  # base case and there can be more than one base case
  if number == 1:
    return 1
  else:
    # step size
    return number * recursive_function(number - 1)
  
answer = recursive_function(5)
print(answer)
```

    120


# **LIST**


```python
my_list = [4, 7, 0, 3, 4]
my_iter = iter(my_list)

print(next(my_iter))
print(next(my_iter))

print(my_iter.__next__())
```

    4
    7
    0



```python
print(len(my_list))
```

    5



```python
mean = 1
if len(my_list) > 1:
    for element in my_list:
        print(element)
        mean = mean + element
   

print(mean)
print('total mean :', int(mean/len(my_list)))
```

    4
    7
    0
    3
    4
    19
    total mean : 3


# Trapezoidal Rule



```python
from math import sin
```


```python
from math import sin, pi
value = 0

def f(x):
  return x*sin(x)
  
a = 0 ## lower limit
b = pi/2 ## upper limit
n = 1000 ## number of division

## h value
h = (b - a) / n

## formula
S = 0.5 * (f(a) + f(b))

##
for i in range(1, n):
  S = S +  f(a + i*h)
Integral = h * S
print('Integral Value {}'.format(Integral))
```

    Integral Value 1.0000002056167847


# **Euler Method**


```python
from math import exp

def dy(x,y):
  return x*y

## Analytical Sollution
def f(x):
  return exp(x**2/2)

## starting and final value of x
x = 0
xn = 2

## Initial value of y
y = 1

## Step Size
h = 0.5

## Total number of steps
n = int((xn - x)/h)

## header
print('x  \t\t  y(Euler) \t\t  y(Analytical)')
print('{0}  \t\t {1} \t\t  {2}'.format(x, y, f(x)))
for i in range(n):
  y += dy(x,y)*h ## calculate next h
  x += h        ## x increment
  print('{} \t\t {} \t\t {}'.format(x,y,f(x)))
```

    x  		  y(Euler) 		  y(Analytical)
    0  		 1 		  1.0
    0.5 		 1.0 		 1.1331484530668263
    1.0 		 1.25 		 1.6487212707001282
    1.5 		 1.875 		 3.080216848918031
    2.0 		 3.28125 		 7.38905609893065



```python
## Tabular Format
```


```python
num = 1
num2 = 2
```


```python
print("Hello World {0} num {1}".format(num,num2))
```

    Hello World 1 num 2



```python
# Solve the quadratic equation ax**2 + bx + c = 0

# import complex math module
import cmath

a = 1
b = 5
c = 6

# To take coefficient input from the users
# a = float(input('Enter a: '))
# b = float(input('Enter b: '))
# c = float(input('Enter c: '))

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))
```

    The solution are (-3+0j) and (-2+0j)



```python
# Solve the quadratic equation ax**2 + bx + c = 0

# import complex math module
import cmath

a = 1
b = 5
c = 6
```


```python

# To take coefficient input from the users
# a = float(input('Enter a: '))
# b = float(input('Enter b: '))
# c = float(input('Enter c: '))

# calculate the discriminant
d = (b**2) - (4*a*c)

```


```python
# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))
```

    The solution are (-3+0j) and (-2+0j)



```python

```


```python
num = 7
```


```python
for i in range(1, num+1):
        factorial = factorial*i
        print('the factorial of ', factorial)
```

    the factorial of  1
    the factorial of  2
    the factorial of  6
    the factorial of  24
    the factorial of  120
    the factorial of  720
    the factorial of  5040



```python
  
```


```python
def your_name(numb):
  """
  modules print number above
  """
  print(numb)
  print('Hello WOrld')

  number = 5



  def mention_name(name):
    print('Blah')

    number = 5




number = 10
your_name(number)
# print(numb)
```

    10
    Hello WOrld



```python
help(your_name)
```

    Help on function your_name in module __main__:
    
    your_name(numb)
        modules print number above
    

if condition == value:
  print('Blah')
elif condition != value:
  print('blah blah')
else:
  print('Foo')

```python
variable = 5
```


```python
a = 10
```


```python
def expression(num):
  num = num + 1
  return num

a = 10
ans = expression(a)
```


```python
from math import pi

print(pi)
```

    3.141592653589793



```python
from math import pi

def area_of_circle(radius):
  ans = pi * radius * radius
  return ans

def check(radius):
  if radius != 0:
    area_of_circle(radius)
  elif radius < 0:
    print()

print("area of the circle is ",area_of_circle(10))
```

    area of the circle is  314.1592653589793



```python

```
