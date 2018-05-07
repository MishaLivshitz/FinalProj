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

        # soup = bs4.BeautifulSoup(text, 'html.parser').prettify()
        for key, value in letters.items():
            text = str(text).replace('\\x' + key, value)
        # print(soup)
        return text

    def __translate(self, trans):
        trans = self.__myencode(trans.read())
        i = trans.find('לא נמצא תרגום מילוני')
        if trans.find('לא נמצא תרגום מילוני') != -1:
            return None
        indx_start = trans.find(
            '<div id="_ctl0_mainContent_googleTranslateControl_btResult" class="machineTranslateResult"')
        indx_start = trans.find('>', indx_start)
        indx_end = trans.find('</div>', indx_start)
        words = trans[indx_start + 1:indx_end].split(' ')
        return words

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

                # com = value.split(" ")
                value = value.replace('.', ' ')
                value = value.replace(',', ' ')
                value = value.replace('!', ' ')
                value = value.replace('#34&', ' ')
                value = value.replace("%", ' ')
                encoded_com = str(value.encode("utf-8"))
                encoded_com = encoded_com[2:encoded_com.__len__() - 1]
                encoded_com = encoded_com.replace("\\x", '%')
                encoded_com = encoded_com.replace(" ", '%20')
                trans = self.__get_source_code("http://www.morfix.co.il/" + encoded_com)
                list_en_words = self.__translate(trans)
                if list_en_words:
                    for word_in_list in list_en_words:
                        if word_in_list in bad_words:
                            bad = bad + 1
                            print('bad - ', word_in_list)
                        else:
                            if word_in_list in good_word:
                                good = good + 1
                                print('good - ', word_in_list)
                else:
                    continue

                if (good / bad) > 1.5:
                    pos_post = pos_post + 1
                    print("post_good-", value)
                else:
                    if good / bad < 1:
                        neg_post = neg_post + 1
                        print("post_bad-", value)
                    else:
                        neu_post=neu_post+1
                        print("post_neutral-", value)
                bad = 1
                good = 1

            print("rate = ", ((pos_post+neu_post/2) / (pos_post+neg_post+neu_post)) * 5)
