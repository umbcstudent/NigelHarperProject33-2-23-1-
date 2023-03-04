#Show the Quiz Title
print(r"""
╔╗ ╔╗                   ╔╗        ╔═══╗           
║║ ║║                   ║║        ║╔═╗║           
║╚═╝║╔══╗ ╔═╗╔══╗╔══╗╔═╗╚╝╔══╗    ║║ ║║╔╗╔╗╔╗╔═══╗
║╔═╗║╚ ╗║ ║╔╝║╔╗║║╔╗║║╔╝  ║══╣    ║║ ║║║║║║╠╣╠══║║
║║ ║║║╚╝╚╗║║ ║╚╝║║║═╣║║   ╠══║    ║╚═╝║║╚╝║║║║║══╣
╚╝ ╚╝╚═══╝╚╝ ║╔═╝╚══╝╚╝   ╚══╝    ╚══╗║╚══╝╚╝╚═══╝
             ║║                      ╚╝           
             ╚╝                                   
""")
print("Welcome to Harper's Quiz! You will answer three True or False questions. Please ONLY enter the following letter T or F. Good Luck! ")


#Setup Inquiry 
inquiry = ('Q1. Light travels in space goes in a straight line.', 'Q2. The Mona Liza was stolen from the Lourve in 1911.', 'Q3. Are greyhound faster than cheetah?')

#Setup Answers
answers = ('T', 'T', 'F')
correctAnswer = 1

#Show the user question 1
print(inquiry[0])
#Get the answer from the user
userGuess = input("Please enter 'T' for true or 'F' for false ")
userGuess = int(len(userGuess))
#Compare the answer to the correct answers
if(answers == answers[0]):
  #Print a blank space
  print()
#Show the user question 2
print(inquiry[1])
#Get the answer from the user
userGuess = input("Please enter 'T' for true or 'F for false. ")
userGuess = int(len(userGuess))
#Compare the answer to the correct answers
if(answers == answers[1]):
  #Print a blank space
  print()
#Show the user question 3
print(inquiry[2])
#Get the answer from the user
userGuess = input("Please enter 'T' for true or 'F' for false. ")
userGuess = int(len(userGuess))
if(answers == answers[2]):
  #Print a blank space
  print()

#Calculate the total number of inquiry
numberOfInquiry = len(inquiry) 

#Add to correct answers
correctAnswer += 1

#Loop once for each inquiry
for index in range(numberOfInquiry):
    print(f'You got {correctAnswer} out of {len(inquiry)} correct! Thanks for playing!')
  
#Print a blank space
print()

