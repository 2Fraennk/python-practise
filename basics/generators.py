#!/usr/bin/env python3

# let's create and use a generator

# create a generator
## your own generator could be a individual iterator
## the yield is kind of an iterator, it "remembers" the num value and continue at this point at the next generator call
def gen_range(stop, start=1, step=2):
    num = start
    while num <= stop:
        yield num
        num += step

# call the generator gives back an object, so we need to save it as a variable
generator = gen_range(10)

# to use the generator as an iterator, we need to call it from a loop
for num in gen_range(10, step=1):
    print(f"num is:  ", num)


# turn the generator's result into a  list
my_list = list(generator)
print("here is my list generated: ", my_list)


# calculate the Fibonacci Numbers with a generator
def gen_fib():
    # define the start values
    a, b = 1, 0
    # let it run forever
    while True:
        # the result 'b' is the sum of the first and the second value
        a, b = b, a + b
        print(a, b)
        yield a

fib = gen_fib()
# limit the infinite generator run with a counting for-loop
[next(fib) for i in range(20)]

# just print the last value
print("last value in sequence: ", [next(fib) for i in range(20)][-1])