student_scores = [12,53,443,45,242,23]

# function to sum the values of the array
def sum(n):
    sum_value = 0
    for score in n: 
        sum_value += score
    return sum_value

# function to find maximum number
def max(n):
    max_score = 0

    for score in n:
        if score > max_score:
            max_score = score
    
    return max_score

# fizz buzz problem

# You are going to write a program that automatically prints the solution to the FizzBuzz game. These are the rules of the FizzBuzz game:
# Your program should print each number from 1 to 100 in turn and include number 100.
# But when the number is divisible by 3 then instead of printing the number it should print "Fizz".
# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

for i in range(10, 16):
    if i % 3 == 0 and i % 5 == 0:
        i = "FizzBuzz"
    elif i % 5 == 0:
        i = "Buzz"
    elif i % 3 == 0:
        i = "Fizz"

    print(i)
print(sum(student_scores))
print(max(student_scores))