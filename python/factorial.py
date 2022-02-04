def factorial(num):
  output = 1
  if num == 0:
    return 1
  else:
    for i in range(1, num + 1):
      output *= i
  return output

print(factorial(8))
