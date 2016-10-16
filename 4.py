# http://stackoverflow.com/questions/5967500/how-to-correctly-sort-a-string-with-a-number-inside

import os
import sys
import re


def atoi(text):
    return int(text) if text.isdigit() else text


def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [atoi(c) for c in re.split('(\d+)', text)]


def compare_list(list1, list2, diffs):
    if len(list1) != len(list2):
        raise NameError('Different length')
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            if list1[i] != 'so' and list2[i] != 'semper':
                diff = (list1[i], list2[i])
                diffs.append(diff)
            # else:
            #     diff = (list1[i], ' ')
            # diffs.append(diff)
    return diffs


# get relative path from arg
mypath = 'loremisnotipsum'

files = []
# iterate dirs and files
for f in os.listdir(mypath):
    path = os.path.join(mypath, f)
    files.append(path)

reference = None
files.sort(key=natural_keys)
count = 0
diffs = []
for path in files:
    with open(path) as f:
        data = f.read()
    if count == 0:
        reference = data.split(' ')
    else:
        diffs = compare_list(reference, data.split(' '), diffs)
    count = count + 1

# for diff in diffs:
#     print diff

print ''.join([diff[1] for diff in diffs])
