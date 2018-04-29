import urllib.request
import bs4
from numpy import unicode
from urllib.parse import unquote


class Lecturer:

    def __init__(self, num, name, comments):
        self.num = num
        self.name = name
        self.comments = comments
        print("size=", len(comments))

    def __get_source_code(self, url):
        request = urllib.request.Request(url)
        return urllib.request.urlopen(request)

    def __myencode(self, text):
        letters = dict(
            {'e0': 'א', 'e1': 'ב', 'e2': 'ג', 'e3': 'ד', 'e4': 'ה', 'e5': 'ו', 'e6': 'ז', 'e7': 'ח', 'e8': 'ט'
                , 'e9': 'י', 'ea': 'ך', 'eb': 'כ', 'ec': 'ל', 'ed': 'ם', 'ee': 'מ', 'ef': 'ן', 'f0': 'נ',
             'f1': 'ס',
             'f2': 'ע', 'f3': 'ף', 'f4': 'פ', 'f5': 'ץ', 'f6': 'צ', 'f7': 'ק', 'f8': 'ר', 'f9': 'ש', 'fa': 'ת'});

        soup = bs4.BeautifulSoup(text, 'html.parser').prettify()
        for key, value in letters.items():
            text = str(text).replace('\\x' + key, value)
        print(soup)
        return text

    def __translate(self, trans):
        trans = self.__myencode(trans.read())
        print(trans)

    def print_comments(self):
        i = 1
        for z in self.comments:
            if z != "":
                print(i, ":", z, '\n')
                i = i + 1

    def analyze_comments(self):
        bad = 1
        good = 1

        pos_post = 0
        neg_post = 0
        neu_post = 0
        bad_words = open("negative_words_he.txt", encoding="utf8").read().split("\n")
        good_word = open("positive_words_he.txt", encoding="utf8").read().split("\n")

        bad_words.remove("")
        good_word.remove("")
        if len(self.comments) != 0:
            for key, value in self.comments.items():

                com = value.split(" ")
                for word in com:
                    word = str(word.encode("utf-8"))
                    word = word[2:word.__len__() - 1]
                    word = word.replace("\\x", '%')
                    trans = self.__get_source_code("http://www.morfix.co.il/" + word)
                    self.__translate(trans)
                    if word in bad_words:
                        bad = bad + 1
                    else:
                        if word in good_word:
                            good = good + 1

                if (good / bad) >= 1.5:
                    pos_post = pos_post + 1
                    print("good-", com)
                else:
                    if good / bad <= 0.8:
                        neg_post = neg_post + 1
                        print("bad-", com)
                bad = 1
                good = 1

            if neg_post != 0:
                neu_post = 1
                print("rate = ", (pos_post / (pos_post + neg_post)) * 5)
