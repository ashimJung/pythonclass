 
 

name=[]
print("\n\n\t\t\t Top 10 Highest scoring students")

limit=10
while True:
  print('\n\t\t\t Add and remove students according to their score')
  print('\t\t To add students type "add" and to remove type "remove"')
  print('you can add maximum 10 students')
  choose=str(input('\n Choose add or remove:')).lower()

  if limit>10:
    print('limit reached')
  elif limit<0:
    print('No value,Enter a value')
    break
  if choose=='add':
    student_name=input('Enter student name:')
    name.append(student_name)
    print('Students list after insertion')
    print(name)
    limit=limit-1
    print('You have', limit,'limits\n')

  elif choose=='remove':
    student_name=input('Enter student name:')
    name.remove(student_name)
    print('Students List after deletion')
    print(name)
    limit=limit+1
    print('You have', limit,'limits\n')

  elif choose!='add' or 'remove':
    print('Invalid Choice Please enter add or remove')

