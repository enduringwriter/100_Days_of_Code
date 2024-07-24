
# Variable
friends_a = 1
friends_b = 1
friends_c = 1


# variables within a function are Non-Global, and are only available within that function
def increase_friends_a():
  friends_a = 2
  x = 12
  print(x)
  print(f"friends inside function A: {friends_a}")
increase_friends_a()
print(f"friends outside function A: {friends_a}")
# print(x) outside defined fuction doesn't work
# print(x) returns "NameError: name 'x' is not defined" b/c its not a global variable. Neither is "friends_a" in the defined fuction

# Global
def increase_friends_b():
    global friends_b    # without defining the variable as global, an "UnboundLocalError of local variable" error results b/c the function is trying to modify a variable outside the function. If the value remains unchanged, no error results and there is no need to declare it as global.
    friends_b += 1
    print(f"friends inside function B: {friends_b}")
increase_friends_b()
print(f"friends outside function B: {friends_b}")

# Non-Global, using return
def increase_friends_c():
  print(f"friends inside function C: {friends_c}")
  return friends_c + 1
friends_c = increase_friends_c()
print(f"friends outside function C: {friends_c}")

# Creating global constants
# naming convention in pythong is to CAPITALIZE GLOBAL CONSTANTS
PI = 3.14159
URL = "https://enduringwriter.com"
TWITTER_HANDLE = "enduringwriter"
