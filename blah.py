firstDict = {'Peter': 'Griffin', 'Glenn': 'Quagmire', 'Adam': 'West', 'test1': 'testing1', 'test1': 'differentValue'}
secondDict = {'Tetsuo': 'Shima', 'Shotaro': 'Kaneda', 'Lady': 'Miyako', 'test1': 'testing1', 'test2': 'testing2', 'test2': 'anotherValue'}
thirdDict = {'Peter': 'Gregory', 'Richard': 'Hendriks', 'Kumail': 'Nanjiani', 't

def merge_dicts(dict_a, dict_b, dict_c):
    merged_dict = {key: [value] for key, value in dict_a.iteritems()}
    for key, value in dict_a.iteritems():
        try:
            merged_dict[key].append(value)
        except KeyError:
            meeged_dict[key] = [value]
    return ret_dict

