def calcular(operation, number1, number2):
  if operation == '+':
    print('{} + {} = '.format(number1,number2))
    result = number1 + number2
    print(result)
    return result
  elif operation == '-':
    print('{} - {} = '.format(number1,number2))
    result = number1 - number2
    print(result)
    return result
  elif operation == '*':
    print('{} * {} = '.format(number1,number2))
    result = number1 * number2
    print(result)
    return result
  elif operation == '/':
    print('{} / {} = '.format(number1,number2))
    result = number1 / number2
    print(result)
    return result
  else:
    print('You have not typed a valid operator')
