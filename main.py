import urllib.request
import re
from bs4 import BeautifulSoup
from Classes import Institute, Lecturer


def myencode(text):
    letters = dict(
        {'e0': 'א', 'e1': 'ב', 'e2': 'ג', 'e3': 'ד', 'e4': 'ה', 'e5': 'ו', 'e6': 'ז', 'e7': 'ח', 'e8': 'ט'
            , 'e9': 'י', 'ea': 'ך', 'eb': 'כ', 'ec': 'ל', 'ed': 'ם', 'ee': 'מ', 'ef': 'ן', 'f0': 'נ',
         'f1': 'ס',
         'f2': 'ע', 'f3': 'ף', 'f4': 'פ', 'f5': 'ץ', 'f6': 'צ', 'f7': 'ק', 'f8': 'ר', 'f9': 'ש', 'fa': 'ת'});

    # soup = BeautifulSoup(text, 'html.parser').prettify();
    for key, value in letters.items():
        text = str(text).replace('\\x' + key, value);
    # print(soup);
    return text;


def getinstitutes(dargooSource):
    start = dargooSource.find("בחר מוסד לימודים")
    end = dargooSource.find("</div>", start)
    names = dargooSource[start:end]
    size = names.count("<option value=")
    for i in range(size):
        id_index = names.find("<option value=") + 14
        id_number = re.sub("[^0-9]", "", names[id_index:id_index + 3])
        print(id_number)
        if int(id_number) >= 10:
            name_index = id_index + 3
        else:
            name_index = id_index + 2

        names = names[name_index:]
        name = names[0:names.find("</option")]
        print(name)

    # print(names)

    return


url = "http://www.dargoo.co.il/"
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)

getinstitutes(myencode(response.read()))

# check = Institute.Institute('Bruade', '23', {Lecturer.Lecturer(23, 'moshe'), Lecturer.Lecturer(25, 'David')})
# check1 = Institute.Institute('SCE', '27', {Lecturer.Lecturer(23, 'moshe')})
# check2 = Institute.Institute('TAU', '21', {Lecturer.Lecturer(23, 'moshe')})
# check4 = Institute.Institute('OBU', '8', {Lecturer.Lecturer(23, 'moshe')})

# instituteList = {check, check1, check2, check4}

# for i in instituteList:
#   print(i.__call__());

# with open("Output.txt", "w") as text_file:
#   print(f"{myencode(response.read())}", file=text_file)
