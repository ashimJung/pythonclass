

import calculate
import oddeven
 



while True:
  print('\n\n\tWelcome to this mathmetaical program please select your option:')
  print('\tEnter "o_e separator" for odd even separation and "calculator" for calculation')

  chosen_opt = input("Enter your option:").strip().lower()

  if chosen_opt=='o_e separator':
    num=int(input('enter number to find odd or even:'))
    odd_even_result=oddeven.findOddEven(num)
    if odd_even_result:
      print("the number is even")
    else:
      print('the number is odd')

  elif chosen_opt=='calculator':
    print('\n\n\t\tWelcome to calculator\n\n')
    num1=input('Enter number 1:')
    num2=input('Enter number 2:')
    operator=input('Enter operator:')

  elif chosen_opt=='quit':
      break
    
  if operator=='+':
      sum_data=calculate.sum(float(num1),float(num2))
      print('The sum is',sum_data)
  elif operator=='-':
      sub_data=calculate.sub(float(num1),float(num2))
      print('The sub is',sub_data)
  elif operator=='*':
      mul_data=calculate.multiply(float(num1),float(num2))
      print('The division is',mul_data)
  elif operator=='/':
      div_data=calculate.divide(float(num1),float(num2))
      print('The multiplication is',div_data)
  elif operator=='%':
      mod_data=calculate.modulo(float(num1),float(num2))
      print('The modulo is',mod_data)

  else:
    print('option not available')

  
