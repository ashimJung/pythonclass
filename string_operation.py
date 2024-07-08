String_name = "this is String it's"
print(String_name)
print(len(String_name))

a='kushal gede'
 

for i in a:
  print(i)

email=input('Enter you email:')
if '@' not in email:
  print('Invalid Email')
else:
  print('Email Validated succesfully!')

  #slicing string

  example = 'favourite food is mango'
  print(example[2:8])

  b='hello world!'
  print(b[-5:-2])

  #modifying string
sentence='The world is beautiful so lets be HAPPY'
print(sentence.lower())

#to remove whitespace
new_sentence=' texas college of management '
print(new_sentence.strip())

#to replace anything character add a word from a string we use replace
print(new_sentence.strip().replace('management','science'))

#splitting string
split_name='rajesh!hamal'
print(split_name.split('!'))
print(type(split_name.split('!')))

#string concatination
first_name="ashim jung"
last_name="karki"

concate_name=first_name+" "+last_name
print(concate_name)

def sum(a,b):
  sum =a+b
  return sum
sum_amt=sum(20,40)
print(sum_amt)


#sets in python
set_items={'ram','shyam','hari','gopal'}
print(set_items)



