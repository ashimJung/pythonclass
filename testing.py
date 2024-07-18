 
 

# name=[]
# print("\n\n\t\t\t Top 10 Highest scoring students")

# limit=10
# while True:
#   print('\n\t\t\t Add and remove students according to their score')
#   print('\t\t To add students type "add" and to remove type "remove"')
#   print('you can add maximum 10 students')
#   choose=str(input('\n Choose add or remove:')).lower()

#   if limit>10:
#     print('limit reached')
#   elif limit<0:
#     print('No value,Enter a value')
#     break
#   if choose=='add':
#     student_name=input('Enter student name:')
#     name.append(student_name)
#     print('Students list after insertion')
#     print(name)
#     limit=limit-1
#     print('You have', limit,'limits\n')

#   elif choose=='remove':
#     student_name=input('Enter student name:')
#     name.remove(student_name)
#     print('Students List after deletion')
#     print(name)
#     limit=limit+1
#     print('You have', limit,'limits\n')

#   elif choose!='add' or 'remove':
#     print('Invalid Choice Please enter add or remove')

# import speech_recognition as sr

# # Create a speech recognition object
# r = sr.Recognizer()

# # Use the microphone as the audio source
# with sr.Microphone() as source:
#     print("Say something!")
#     audio = r.listen(source, timeout=7)  # Set timeout to 7 seconds

# # Try to recognize the spoken words
# try:
#     print("You said: " + r.recognize_google(audio))
# except sr.UnknownValueError:
#     print("Google Speech Recognition could not understand your audio")
# except sr.RequestError as e:
#     print("Could not request results from Google Speech Recognition service; {0}".format(e))
import pandas as pd 

print(pd.__version__)

dist= {
  'head':{
    'name':'Ashim J. Karki',
    'address':'kathamndu',
    'number':123456
  },
  'staff1':{
    'name':'Rajesh hamal',
    'address':'lalitpur',
    'number':123999
  }
}
#to convert dictionary to data frame we can use pd.DataFrame
df=pd.DataFrame(dist)
print(df)
print(df.head())
 

#to read datav from csv
df_Csv = pd.read_csv('/Users/ashim/Desktop/Professional course/pandas/SouthAfricaCrimeStats_v2.csv')
print(df_Csv)

print(df_Csv.head())
print(df_Csv.tail())
print(df_Csv.describe())
print(df_Csv.info())
print(df_Csv.notnull())
