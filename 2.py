import requests
import re
import numpy as np


def magic_square_3x3(n=15):
    s = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    # magic rules
    s[1][1] = n / 3
    s[0][0] = s[1][1] + 1
    s[0][2] = s[1][1] + 3
    s[2][0] = s[1][1] - 3
    s[2][2] = s[1][1] - 1
    # calculate the rest
    s[0][1] = n - s[0][0] - s[0][2]
    s[1][0] = n - s[0][0] - s[2][0]
    s[1][2] = n - s[0][2] - s[2][2]
    s[2][1] = n - s[2][0] - s[2][2]
    return np.array(s)


def is_magic_square_3x3(m):
    if len(np.unique(m)) != m.size:
        return False
    n = sum(m[0, :])
    if n != sum(m[1, :]) or n != sum(m[2, :]):
        return False
    if n != sum(m[:, 0]) or n != sum(m[:, 1]) or n != sum(m[:, 2]):
        return False
    return True


# main
url = 'http://task-00000010.itrace.systems/square.php'

r = requests.get(url)
sessid = r.cookies['PHPSESSID']
print sessid

# <span class="x">30</span>
res = re.search(r'<span class=x>([0-9]+)</span>', r.text, re.M | re.I)
x = int(res.groups(1)[0])

for i in xrange(11):
    # create magic
    s = magic_square_3x3(x)

    print x
    print s
    print is_magic_square_3x3(s)

    numbers = ','.join(str(v) for v in s.ravel().tolist())

    # post answer
    r = requests.post(url, data={'numbers': numbers}, cookies={'PHPSESSID': sessid})
    try:
        res = r.json()
        print res
        x = res['nextsum']
    except:
        print r.text
