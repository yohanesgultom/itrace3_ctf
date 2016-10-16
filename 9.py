from PIL import Image
import requests
import io
import operator


def get_least_color(fd):
    image_file = io.BytesIO(fd.read())
    im = Image.open(image_file)
    pix = im.load()
    groups = {}
    for x in xrange(im.size[0]):
        for y in xrange(im.size[1]):
            p = pix[x, y]
            if p in groups:
                groups[p] = groups[p] + 1
            else:
                groups[p] = 1
    # groups_values = {}
    # for k, v in groups.iteritems():
    #     groups_values[k] = sum(k)
    # groups_values_sorted = sorted(groups_values.items(), key=operator.itemgetter(1))
    # least = groups_values_sorted[0][0]
    groups_sorted = sorted(groups.items(), key=operator.itemgetter(1))
    least = groups_sorted[0][0]
    least_hex = ''.join([hex(x)[2:].zfill(2) for x in least])
    # print groups
    print groups_sorted
    # print least
    return least_hex

# open page to get session
url = "http://task-00001001.itrace.systems/racist.php"
r = requests.get(url)
sessid = r.cookies['PHPSESSID']

stop = False
while not stop:
    # open image
    url_img = "http://task-00001001.itrace.systems/image.php"
    r = requests.get(url_img, cookies={'PHPSESSID': sessid}, stream=True)
    least_hex = get_least_color(r.raw)
    print(least_hex)

    # post answer
    r = requests.post(url, data={'color': least_hex}, cookies={'PHPSESSID': sessid})
    print r.text

    # stop condition
    if "ITRACE" in r.text:
        stop = True
