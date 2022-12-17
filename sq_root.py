# This file computes the square root of a number x, with a given precision.

x=19023192.0 # Debug value
precision=0.000001 # Precision requested

if x<0:
  print("Error: x<0")
  exit()
if x==0:
  print("square root: 0")
  exit()


error=1000.0
# 1st term Taylor series truncation approximation (iterative method)
###
# Approximation of f(x) = sqrt(x) using Taylor series truncation at the 1st term:
#   given a guess g_1 such that g_1^2<x, we can approximate f(x) by a truncated Taylor series g_2 = g_1 + .5 f'(g_1^2) (x-g_1^2).
#   By a standard theorem (Taylor?) the error term is bounded by (1/6) * (1/(2 g_1)) * abs(g_1^2-x)^2
#   When g_1^2>x we can bound by (1/6) * (1/2y) * abs(g_1^2-x)^2 for any y such that y^2<x


iteration=0
sqrt_guess = 5.0
error = abs(sqrt_guess*sqrt_guess - x)
print("Error: " + str(error))
while error>precision:
  print(iteration)
  iteration+=1
  sqrt_guess = sqrt_guess + .5 * (1/(2* sqrt_guess)) * (x-sqrt_guess*sqrt_guess)
  error = abs(sqrt_guess*sqrt_guess - x)
  print("Guess: " + str(sqrt_guess))
  print("Error: " + str(error))

print("Approximation: " + str(sqrt_guess))
print("Error: " + str(error))

