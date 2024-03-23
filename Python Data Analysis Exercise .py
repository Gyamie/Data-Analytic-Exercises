# Variables
message = 'hello world'
Task = 'let today be a fresh new start'

print(f'{message}, {Task}, it will be alright')

#End 


# intergers
num_1 = 100
num_2 = 300

num_3 = str(num_2)

print(len(num_3))

#End 

#Strings
User = 'learning to understand the language'
Computer = ' i am glad you want to know me more'
print(User + Computer)
#End  


# give 1.5 times hourly rate to employees above 40 hours of work
Hours_2 = 45
Rate_2 = 10
Pay_2 = 450.0 * 1.5
print(F'Work above 40 hours of work: {Pay_2}')


# try and catch error handling
User_input1 = input('Please enter your hours\n')

try:
   Hours_3 = int(User_input1)
   print(Hours_3)
except:
   print('please enter numerical value')


User_input2 = input('Please enter your Rate\n')

try:
   Rate_3 = int(User_input2)
   print(Rate_3)
except:
   print('please enter numerical value')


width = 17
height = 12.0

Ans_1 = width//2
print (f'Ans 1 = {Ans_1}')
dataT_1= type(Ans_1)
print(dataT_1)

Ans_2 = width/2.0
print (f'Ans 2 = {Ans_2}')
dataT_2 = type(Ans_2)
print(dataT_2)

Ans_3 = height/3
print (f'Ans 3 = {Ans_3}')
dataT_3 = type(Ans_3)  
print(dataT_3)

dataT_3 = type(Ans_3)
Ans_4 = 1 + 2 * 5
print (f'Ans 4 = {Ans_4}')
dataT_4 = type(Ans_4)
print(dataT_4)

# changing the temperature of a user to Fahrenheit 
Temperature = 'Please provide your  Celsius temperature\n'
Celsius_temperature = input(Temperature)
Update= int(Celsius_temperature)
fahrenheit_temperature = (Update * 9/5) + 32
print (fahrenheit_temperature)


# please change your name
Question =input('please provide your name\n')
Question_2 = input('please provide your new name\n')
name = str(Question)
New_name = str(Question_2)
print('Name has been changed')

# conditional statements

score = -1.0 <= 1.0

UserScore = float(input('Please enter the score\n'))
if score >= UserScore  :
#    print('good grades')

   if UserScore >= 0.9 :
      grade ='A'
   
   elif UserScore >= 0.8 :
       grade ='B'

   elif UserScore >= 0.7 :
       grade ='C'

   elif UserScore >= 0.6 :
       grade ='D'

   elif UserScore < 0.6 :
       grade ='F'

   print(grade)
 
else:
   print('invalid grade')

   
# functions pay
def computepay(hours, rate) :
    Pay = hours * rate * 1.5
    return Pay

working_Pay = computepay(45, 10)

print(working_Pay)

Score_1 = -1.0 <= 1.0

UserScore_1 = float(input('please enter your score and we will tell you your grade\n'))


# functions  for grading
def computegrade(UserScore_1) :
     if  UserScore_1 == Score_1 :
        
         if UserScore_1 >= 0.9 :
                 grade = 'A'

         elif UserScore_1 >= 0.8 :
                 grade = 'B'

         elif UserScore_1 >= 0.7 :
                 grade = 'C'

         elif UserScore_1 >= 0.6 :
                 grade = 'D'

         elif UserScore_1 < 0.6 :
                 grade = 'F'
     else:
          grade = 'Grade invalid'

     return grade 
     
student_grade = computegrade(UserScore_1)

print(student_grade)

# NumberSummary
def numberIdentify ():
         total = 0
         count = 0
        

         while True :
  
            UserInput = input('Please enter a number\n')
  
            if UserInput == 'done' :
             break
      
            try:
             numberSummary = float(UserInput)
             total +=  numberSummary
             count += 1
             average = total/count
            except ValueError:
             print ('Invaild input')

         return  total,count,average
      
 
  
repeat = numberIdentify()


print(repeat)

# finding the minimum and maximum number of the numbers entered

def overView ():
    minValue = float('inf')
    maxValue = float('-inf')

    while True :
               UserInput_1 = input('Please enter a number\n')
               if UserInput_1 == 'done' :
                     break
     
               try:
                   NumberSummary1 = float(UserInput_1)
                   minValue = min(minValue,NumberSummary1)
                   maxValue = max(maxValue,NumberSummary1)
               except ValueError:
                     print('invalid error')
    
    return minValue,maxValue
   
repeat1 = overView()
print(repeat1)

# Parsing string

str = 'X-DSPAM-Confidence:0.8475'
code = str.find(':')
end_code = str.find('5')
#print(end_code)
Number_code = str[code+1:end_code+1]
print (float(Number_code))

   
def count_1():
  word = 'banana'
  count = 0
  for letter in word:
    if letter == 'a': 
       count = count + 1 
  return count   
NumberOfWords = count_1()
print(NumberOfWords)
    

fname = open('Hi Sam Smith.txt')
print (fname)
content = fname.read()
Up_content = content.lower()
print (Up_content)

##change to upper
fname = open('mbox-short.txt')
content = fname.read()
upper = content.upper()
print (upper)


#reading and selecting file content

userRequest = input('please select file \n')
try:
        fname = open(userRequest)
except:
 print(f'file cannot be opened :({userRequest}) ')
 exit()


count = 0 
for line in fname:
    line = line.rstrip()
   
   #if ('X-DSPAM-Confidence:') absent continue
    if line.find('X-DSPAM-Confidence:') == -1:
        continue

   # the latter part of the line
    resulte = (float(line[-7: ]))
    print(resulte)

    count11 = count11 + 1
    Average11 = resulte/count11
print(count)
print(f'Average total:{Average11}')

# MODIFIES LIST and create new
def chop(result,result2):
 
 return result[1:3], result2[1:3]

animals = ['lion','tiger','hen']
update_animales = animals.append('duck')
result = animals 
result2 = animals + ['dockey']
Names = chop(result,result2)

print (Names)

# ////////same/////// but gives only new list and old list

def middle(mee,animals):
 
 return mee[1:3], animals

animals = ['lion','tiger','hen']
meeup = animals + ['dockey']
mee = meeup

Names = middle(mee,animals)

print (Names)


# its for pulling content from the 2 index going.

fhand = open('mbox-short.txt')
for line in fhand:
  words = line.split()
 # print(words)
  if line.find('From') == -1 or len(words) < 3:
    continue
  print(words[:2])


  #read and sort through a file
def story():

 FName = input('please enter the file name\n') 

 try:
  UserFile = open(FName)
  
 except:
  print(f'File name is invalid: {FName}')
  exit()

 Content = UserFile.read()
 Content_new = Content.split()
 Content_orig = Content.split()
 Content_orig.sort()

 
   

 return Content_new, Content_orig

content_view = story()
print(content_view)
  
# selecting and counting mailbox data
def Mail():
    userInput14 = input('please enter your file name \n')
    try:
        RightInput = open(userInput14)
    except:
        print(f'Input is invalid {userInput14}')
        exit()

    count = 0
    for line in RightInput :
        line = line.rstrip()
        line = line.split()

        if 'From' in line :
         
#print the line instead of returning it so you get a looped version of the list
         print(line[1])

        if 'From:' in line:
         continue
        count = count + 1
    print(f'There were {count} lines in the file with From as the first word')
    

Mail()

# min and max in a list
def overView ():
    Numbers = []

    while True :
               UserInput_1 = input('Please enter a number\n')
               if UserInput_1 == 'done' :
                     break
     
               try:
                   NumberSummary1 = float(UserInput_1)
                #   the use of append to store them in a list 
                   Numbers.append(NumberSummary1)
                   minValue = min(Numbers)
                   maxValue = max(Numbers)
               except ValueError:
                     print('invalid error')
    
    return minValue,maxValue
   
repeat1 = overView()
print(repeat1)


def Mail():
    count = dict()
    FName = open('mbox-short.txt')

    for line in FName:
        line = line.rstrip()
        content = line.split()
# use the if statment 
        if 'From:' in content :
            continue
        if 'From' in content:
         selected_option = content[2]

         if selected_option not in count:
          count[selected_option] = 1
         else:
          count[selected_option] += 1

          #use the get statment
          #count[selected_option] = count.get(selected_option,0) + 1

    print(count)
   
 
Mail()  


# the email with the highest
def mail():
    count= dict()
    FName = open('mbox-short.txt')

    for line in FName :
        line = line.rstrip()
        words = line.split()
        if 'From:' in words:
            continue
        if 'From' in words:
         Email = words[1]
         if Email not in count :
            count[Email] = 1
         else:
            count[Email] = count[Email] + 1
    print(count)
    maxValue = (max(count, key=count.get))
    print(maxValue,count[Email])
       

mail()

# the email domin 
def mail():
    count= dict()
    FName = open('mbox-short.txt')

    for line in FName :
        line = line.rstrip()
        words = line.split()
        if 'From:' in words:
            continue
        if 'From' in words:
         Email_domain = words[1]
         #print(Email_domain)
         domain = Email_domain.split('@')
         Actual_domain = domain[1]
         print(Actual_domain)
         if Actual_domain not in count :
            count[Actual_domain] = 1
         else:
            count[Actual_domain] = count[Actual_domain] + 1
    print(count)
    

mail()



#a person with the most messages
def mail():

    count = dict()
    FName = open('mbox-short.txt')
    
    for line in FName:
        line = line.rstrip()
        words = line.split()
        if 'From:' in words :
            continue
        elif 'From' in words :
           # print(words[1])
         Email = words[1]
         count[Email] = count.get(Email,0) + 1

    #print(count)  
    Address_occurance = list()  
    for key,val in list(count.items())  :
       Address_occurance.append((val,key))
       #print(Address_occurance)

    Address_occurance.sort(reverse=True)

    for val,key in Address_occurance[:1]:
       print(key,val)

    
mail()


# the distribution of the hour of the day for each of the messages.


def mail():

    count = dict()
    FName = open('mbox-short.txt')
    
    for line in FName:
        line = line.rstrip()
        words = line.split()
        if 'From:' in words :
            continue
        elif 'From' in words :
           #print(words[5])
           Time = words[5]
           Time = Time.split(':')
           Hour = Time[0]
           #print(Hour)
           count[Hour] = count.get(Hour,0) + 1
    #print(count)     
    
    Hours_ocurrence = list()
    for key,val in list(count.items()) :
        Hours_ocurrence.append((key,val))

    Hours_ocurrence.sort() 

    for key , val in Hours_ocurrence:
        print(key,val)


mail()

# finding the occurance of words in a text file

def mail():
 
 import string
 
 count = dict()
 FName = open('Hi Sam Smith.txt')
  
 for line in FName :
  line = line.strip()
  line = line.translate(line.maketrans('','',string.punctuation))
  line = line.lower()
  words = line.split()

  for word in words :
   count[word] = count.get(word,0) + 1

 Names = list()
 for key , val in list(count.items()):
  Names.append((val,key))

  Names.sort(reverse=True)
 for val,key in Names[:20] :
  print(f'{key} = {val} ocurring times')


mail()

# The Average number for the New Revision 
#using Regular Expressions
import re
total = 0
count = 0
hand = open('mbox-short.txt')
for line in hand:
 line = line.rstrip()
 #if 'New Revision:' in line:
 # print(line)

 x = re.findall('^New Revision: ([0-9.]+)', line)
 if len(x) > 0:
  #print(x)
  for num in x :
   Number_need = float(num)
   total += Number_need 
   count += 1
   Aver_Num = total/count
print(f'The Average number for the New Revision is : {Aver_Num}')


#pulling the host name of a url entered by a user
import socket


URL = input('Enter - ')

try:

 hostName = URL.split('/')[2]
 Port = 80
 mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 mysock.connect((hostName,Port))

except IndexError:
 print('please enter valid url')
except socket.error as e:
 print(f'error:{e}')


import socket

def receive_data():
    # Create a socket
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to a server (replace 'example.com' and 80 with the actual server and port)
    my_socket.connect(('example.com', 80))

    # Send a request (replace 'GET / HTTP/1.1\r\nHost: example.com\r\n\r\n' with your actual request)
    request = 'GET / HTTP/1.1\r\nHost: example.com\r\n\r\n'
    my_socket.send(request.encode())

    # Receive and display data
    total_characters = 0
    while True:
        data = my_socket.recv(1024)  # Receive data in chunks of 1024 bytes
        if not data:
            break  # Break if no more data is received

        # Display data
        print(data.decode(), end='')

        # Update the total character count
        total_characters += len(data)

        # Check if the total character count exceeds 3000
        if total_characters >= 3000:
            break

    # Display the total number of characters
        print(f"\nTotal characters received: {total_characters}")

    # Close the socket
    my_socket.close()

# Call the function to receive data
receive_data()