'''
Printing a modular letter:
Program has two variables, a letter string and a list with tuples inside. The print statements print the letterString.
The strings within the tuples in the list replace the %s parts of the letterString. 
'''

letterString = 'Dear %s,\n\nI would like you to vote for %s\nbecause I think he is best for this state.\n\nSincerely,\n%s\n'
listOfTuples = [('Hildegard', 'Barbara Boxer', 'Brunhilda'), ('Cheech', 'Jerry Brown', 'Chong'), ('Kaneda', 'Akira', 'Tetsuo')]

print ( letterString   %   listOfTuples[0])

print ( letterString   %   listOfTuples[1])

print ( letterString   %   listOfTuples[2])

'''---------------Output------------------
Dear Hildegard,

I would like you to vote for Barbara Boxer
because I think he is best for this state.

Sincerely,
Brunhilda

Dear Cheech,

I would like you to vote for Jerry Brown
because I think he is best for this state.

Sincerely,
Chong

Dear Kaneda,

I would like you to vote for Akira
because I think he is best for this state.

Sincerely,
Tetsuo
'''



