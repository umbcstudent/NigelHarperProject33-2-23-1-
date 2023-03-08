# Show the Quiz Title
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
print(
    "Welcome to Harper's Quiz! You will answer three True or False questions. Please ONLY enter the following letter T or F. Good Luck! ")

# Setup Inquiry
inquiry = (
'Q1. Light travels in space goes in a straight line.', 'Q2. The Mona Liza was stolen from the Louvre in 1911.',
'Q3. Are greyhound faster than cheetah?')

# Setup Answers
answers = ('T', 'T', 'F')
correctAnswer = 0

# Calculate the total right answers
numberOfInquiry = len(inquiry)

# Show the user question 1
print(inquiry[0])
# Get the answer from the user
userGuess = input("Please enter 'T' for true or 'F'' for false: ")
# Create awhile loop that runs until 'T' or 'F'
while userGuess not in answers:
    # Prompt user for a new answer
    userGuess = input("Please enter 'T' for true or 'F' for false: ")
#Create a loop that scans each question
for index in range(numberOfInquiry):
    #Compare the answers to the correct answers
    if userGuess == answers[0]:
        # Add a point for correct answer
        correctAnswer += 1
        

# Show the user question 2
print(inquiry[1])
# Get the answer from the user
userGuess = input("Please enter 'T' for true or 'F for false: ")
# Create awhile loop that runs until 'T' or 'F'
while userGuess not in answers:
    # Prompt user for a new answer
    userGuess = input("Please enter 'T' for true or 'F' for false. ")
    #Compare the answer to the correct answers
    if userGuess == answers[1]:
        # Add a point for correct answer
        correctAnswer += 1
        # Print a blank space

# Show the user question 3
print(inquiry[2])
# Get the answer from the user
userGuess = input("Please enter 'T' for true or 'F' for false. ")
# Create awhile loop that runs until 'T' or 'F'
while userGuess not in answers:
    # Prompt user for a new answer
    userGuess = input("Please enter 'T' for true or 'F' for false. ")
    # Compare the answer to the correct answers
    if  userGuess == answers[2]:
        # Add a point for correct answer
        correctAnswer += 1

       
# Loop once for each inquiry
for index in range(numberOfInquiry != 1):
    print(f'You got {correctAnswer} out of {numberOfInquiry} correct! Thanks for playing!')
