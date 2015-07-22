"""
Created 3 different dictionaries with 3 duplicate keys: Peter, test1, and test2. Keys are spread out across the dictionaries.
Added all duplicate keys into one dictionary and non-duplicates into another.
Merged the two dictionaries together into a dictionary, secondComboDict.
"""

firstDict = {'Peter': 'Griffin', 'Glenn': 'Quagmire', 'Adam': 'West', 'test1': 'testing1', 'test1': 'differentValue'}
secondDict = {'Tetsuo': 'Shima', 'Shotaro': 'Kaneda', 'Lady': 'Miyako', 'test1': 'testing1', 'test2': 'testing2', 'test2': 'anotherValue'}
thirdDict = {'Peter': 'Gregory', 'Richard': 'Hendriks', 'Kumail': 'Nanjiani', 'test1': 'testing1', 'test2': 'testing2'}

firstComboDict = {}

for key in (firstDict.keys() | secondDict.keys() | thirdDict.keys()):
    if key in firstDict and key in secondDict:
        firstComboDict.setdefault(key, []).append(firstDict[key])
        firstComboDict.setdefault(key, []).append(secondDict[key])
    if key in secondDict and key in thirdDict:
        firstComboDict.setdefault(key, []).append(secondDict[key])
        firstComboDict.setdefault(key, []).append(thirdDict[key])
    if key in firstDict and key in thirdDict:
        firstComboDict.setdefault(key, []).append(firstDict[key])
        firstComboDict.setdefault(key, []).append(thirdDict[key])
        
secondComboDict = {}

for key in (firstDict.keys() | secondDict.keys() | thirdDict.keys()):
    if key not in firstDict and key not in secondDict:
        secondComboDict.update(firstDict)
        secondComboDict.update(secondDict)
    if key not in secondDict and key not in thirdDict:
        secondComboDict.update(secondDict)
        secondComboDict.update(thirdDict)
    if key not in firstDict and key not in thirdDict:
        secondComboDict.update(firstDict)
        secondComboDict.update(thirdDict)

secondComboDict.update(firstComboDict)

print(secondComboDict)

"""--------------------------------Output--------------------------------------
>>> 
{'test1': ['differentValue', 'testing1', 'testing1', 'testing1', 'differentValue', 'testing1'], 'Tetsuo': 'Shima', 'Glenn': 'Quagmire', 'test2': ['anotherValue', 'testing2'], 'Lady': 'Miyako', 'Adam': 'West', 'Kumail': 'Nanjiani', 'Richard': 'Hendriks', 'Shotaro': 'Kaneda', 'Peter': ['Griffin', 'Gregory']}
>>> 
"""
