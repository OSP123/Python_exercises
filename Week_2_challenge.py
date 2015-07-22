'''
This is my answer to Week 2's challenge. The program creates a main list,
which will then hold 3 other lists containing the inputs from the user. Once
the lists are populated within the while loop, the lists are converted to tuples.
The strings within the tuples in the list replace the %s parts of the
letterString, to give a modular letter program. 
'''

inputList = []
firstVariables = ["placement","placement","placement"]
secondVariables = ["placement","placement","placement"]
thirdVariables = ["placement","placement","placement"]
letterString = 'Dear %s,\n\nI would like you to vote for %s\nbecause I think he is best for this state.\n\nSincerely,\n%s\n'
quitStatement = 'type q at any time when you are finished'
while True:
    print(quitStatement)
    
    addressee1 = input('Enter the first addressee: ')
    if addressee1.strip() == 'q':
       break
    firstVariables[0] = addressee1
    candidate1 = input('Enter the first candidate: ')
    if candidate1.strip() == 'q':
       break
    firstVariables[1] = candidate1
    sender1 = input('Enter the first sender: ')
    if sender1.strip() == 'q':
       break
    firstVariables[2] = sender1

    print(quitStatement)
    addressee2 = input('Enter a second addressee: ')
    if addressee2.strip() == 'q':
       break
    secondVariables[0] = addressee2
    candidate2 = input('Enter a second candidate: ')
    if candidate2.strip() == 'q':
       break
    secondVariables[1] = candidate2
    sender2 = input('Enter a second sender: ')
    if sender2.strip() == 'q':
       break
    secondVariables[2] = sender2

    print(quitStatement)
    addressee3 = input('Enter a third addressee: ')
    if addressee3.strip() == 'q':
       break
    thirdVariables[0] = addressee3
    candidate3 = input('Enter a third candidate: ')
    if candidate3.strip() == 'q':
       break
    thirdVariables[1] = candidate3
    sender3 = input('Enter a third sender: ')
    if sender3.strip() == 'q':
       break
    thirdVariables[2] = sender3
    
firstTuples = tuple(firstVariables)
secondTuples = tuple(secondVariables)
thirdTuples = tuple(thirdVariables)

inputList.append(firstTuples)
inputList.append(secondTuples)
inputList.append(thirdTuples)

print ( letterString   %   inputList[0])

print ( letterString   %   inputList[1])

print ( letterString   %   inputList[2])

'''-------------------Output----------------------
type q at any time when you are finished
Enter the first addressee: Cat Anderson
Enter the first candidate: Meows Mckenzie
Enter the first sender: Gato Delicious
type q at any time when you are finished
Enter a second addressee: Woof McDog
Enter a second candidate: Ruff Lyfe
Enter a second sender: Hydrant Gruff
type q at any time when you are finished
Enter a third addressee: Nemo Underland
Enter a third candidate: Something Fishy
Enter a third sender: Under TheSea
type q at any time when you are finished
Enter the first addressee: q
Dear Cat Anderson,

I would like you to vote for Meows Mckenzie
because I think he is best for this state.

Sincerely,
Gato Delicious

Dear Woof McDog,

I would like you to vote for Ruff Lyfe
because I think he is best for this state.

Sincerely,
Hydrant Gruff

Dear Nemo Underland,

I would like you to vote for Something Fishy
because I think he is best for this state.

Sincerely,
Under TheSea
'''

    
