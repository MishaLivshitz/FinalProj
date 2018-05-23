import urllib.request
from typing import Any


class Lecturer:

    def __init__(self, num, name, comments):
        self.num = num
        self.name = name
        self.comments = comments

    def __get_source_code(self, url):
        request = urllib.request.Request(url)
        return urllib.request.urlopen(request)

    def __myencode(self, text):
        letters = dict(
            {'e0': 'א', 'e1': 'ב', 'e2': 'ג', 'e3': 'ד', 'e4': 'ה', 'e5': 'ו', 'e6': 'ז', 'e7': 'ח', 'e8': 'ט'
                , 'e9': 'י', 'ea': 'ך', 'eb': 'כ', 'ec': 'ל', 'ed': 'ם', 'ee': 'מ', 'ef': 'ן', 'f0': 'נ',
             'f1': 'ס',
             'f2': 'ע', 'f3': 'ף', 'f4': 'פ', 'f5': 'ץ', 'f6': 'צ', 'f7': 'ק', 'f8': 'ר', 'f9': 'ש', 'fa': 'ת'})

        for key, value in letters.items():
            text = str(text).replace('\\x' + key, value)

        return text

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
        bad_words = open("english_bad.txt", encoding="utf8").read().splitlines()
        good_word = open("english_good.txt", encoding="utf8").read().splitlines()

        if len(self.comments) != 0:
            for key, value in self.comments.items():
                list_en_words = value.split(" ")
                if list_en_words:
                    for word_in_list in list_en_words:
                        if word_in_list in bad_words:
                            bad = bad + 1

                        else:
                            if word_in_list in good_word:
                                good = good + 1

                else:
                    continue

                if (good / bad) > 1.5:
                    pos_post = pos_post + 1

                else:
                    if good / bad < 1:
                        neg_post = neg_post + 1

                    else:
                        neu_post = neu_post + 1

                bad = 1
                good = 1
            print("Pos=", pos_post)
            print("Neg-", neg_post)
            print("Neu-", neu_post)
            #print("rate = ", (pos_post / (pos_post + neg_post)) * 5)
            print("rate = ", ((pos_post + (neu_post / 2)) / (pos_post + neg_post + neu_post)) * 5)
            return ((pos_post + neu_post / 2) / (pos_post + neg_post + neu_post)) * 5
           # return (pos_post / (pos_post + neg_post)) * 5
        else:
            return -1
