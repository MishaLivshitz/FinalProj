import urllib.request
import re
import math
import mysql.connector
from datetime import datetime


class Process:

    def __init__(self, db_cnx):
        self.__db_cnx = db_cnx
        response = self.__get_source_code("http://www.dargoo.co.il/")
        self.__dargoo_source = self.__myencode(response.read())

    def __myencode(self, text):
        letters = dict(
            {'e0': 'א', 'e1': 'ב', 'e2': 'ג', 'e3': 'ד', 'e4': 'ה', 'e5': 'ו', 'e6': 'ז', 'e7': 'ח', 'e8': 'ט'
                , 'e9': 'י', 'ea': 'ך', 'eb': 'כ', 'ec': 'ל', 'ed': 'ם', 'ee': 'מ', 'ef': 'ן', 'f0': 'נ',
             'f1': 'ס',
             'f2': 'ע', 'f3': 'ף', 'f4': 'פ', 'f5': 'ץ', 'f6': 'צ', 'f7': 'ק', 'f8': 'ר', 'f9': 'ש', 'fa': 'ת'});

        # soup = BeautifulSoup(text, 'html.parser').prettify();
        for key, value in letters.items():
            text = str(text).replace('\\x' + key, value)
        # print(soup);
        return text

    def __get_source_code(self, url):
        try:
            request = urllib.request.Request(url)
            url = urllib.request.urlopen(request)
        except urllib.error.HTTPError as err:
            return None

        return url

    def __get_page(self, page, id_number):
        url = "http://www.dargoo.co.il/searchResult.asp?page=" + str(page) + "&searchby=3&ddlCategories=" + str(
            id_number) + "&searchword=&button_search="
        lec_response = self.__myencode(self.__get_source_code(url).read())
        return lec_response

    def __get_dates(self, comment_response, number_of_comments_in_page):

        index_start_date = comment_response.find('<td align="center" width="60px">')
        index_start_date = comment_response.find('>', index_start_date) + 1
        index_end_date = comment_response.find('</td>', index_start_date)
        dates = []
        for i in range(number_of_comments_in_page):
            if len(comment_response[index_start_date:index_end_date]) > 10:
                datetime_object = datetime.strptime(comment_response[index_start_date:index_end_date],
                                                    '%d/%m/%Y %H:%M:%S')
            else:
                datetime_object = datetime.strptime(comment_response[index_start_date:index_end_date],
                                                    '%d/%m/%Y')
            str = datetime_object.strftime("%Y-%m-%d %H:%M:%S")
            dates.append(str)
            index_start_date = comment_response.find('<td align="center" width="60px">', index_end_date)
            index_start_date = comment_response.find('>', index_start_date) + 1
            index_end_date = comment_response.find('</td>', index_start_date)

        return dates

    def __translate(self, value):

        # value = value.replace('.', ' ')
        # value = value.replace(',', ' ')
        # value = value.replace('!', ' ')
        value = value.replace("\\", ' ')
        value = value.replace('#34&', ' ')
        # value = value.replace("%", ' ')

        value = re.sub('[!@#$%^&*()_+.,;"\']', '', value)
        encoded_com = str(value.encode("utf-8"))
        encoded_com = encoded_com[2:encoded_com.__len__() - 1]
        encoded_com = encoded_com.replace("\\x", '%')
        encoded_com = encoded_com.replace(" ", '%20')
        trans = self.__get_source_code("http://www.morfix.co.il/" + encoded_com)
        if trans is not None:
            trans = self.__myencode(trans.read())
            if trans.find('לא נמצא תרגום מילוני') != -1:
                return None
            indx_start = trans.find(
                '<div id="_ctl0_mainContent_googleTranslateControl_btResult" class="machineTranslateResult"')
            indx_start = trans.find('>', indx_start)
            indx_end = trans.find('</div>', indx_start)
            trans_com = trans[indx_start + 1:indx_end]
            return trans_com
        return ''

    def __get_faculty(self, comment_response, lec_id):
        index_start_faculty = comment_response.find('פקולטה/חוג:<span style="padding-left:10px;">')
        index_start_faculty = comment_response.find('>', index_start_faculty)
        index_end_faculty = comment_response.find('</span>', index_start_faculty)
        faculty = comment_response[index_start_faculty + 1:index_end_faculty]
        try:
            self.__db_cnx.cursor().execute(
                "UPDATE `finalproj`.`lecturers` SET `faculty`='" + faculty + "' WHERE `lec_id`='" + str(lec_id) + "';")
            self.__db_cnx.commit()
        except mysql.connector.Error as err:
            print("problem - ", "__get_faculty", err)


    def __get_comments(self, lec_id):
        comment_list = []
        url2 = "http://dargoo.co.il/displayRanking.asp?lecturerID=" + str(lec_id)
        comment_response = self.__myencode(self.__get_source_code(url2).read())
        self.__get_faculty(comment_response, lec_id)
        number_of_comments_in_page = int(
            (comment_response.count('<td style="white-space:normal;width:160px;padding:3px;">')))
        index_start_comment = comment_response.find('<td style="white-space:normal;width:160px;padding:3px;">')

        index_start_comment = comment_response.find(">", index_start_comment) + 1

        dates = self.__get_dates(comment_response, number_of_comments_in_page)

        for i in range(number_of_comments_in_page):
            index_end_comment = comment_response.find("</td>", index_start_comment)
            cur_comment = comment_response[index_start_comment:index_end_comment].split("\\r\\n")
            index_start_comment = comment_response.find('<td style="white-space:normal;width:160px;padding:3px;">',
                                                        index_end_comment)
            index_start_comment = comment_response.find(">", index_start_comment) + 1
            comment = "".join(cur_comment)
            comment = comment.replace('\\t', '')
            comment = comment.strip()
            comment = comment.lstrip()
            print(comment)
            if comment != "" and comment != "תגובתך ממתינה לאישור":
                text = self.__translate(comment)
                if text != '':
                    try:
                        self.__db_cnx.cursor().execute(
                            "INSERT INTO `finalproj`.`lec_comments` (`lec_id`,`comment_date`,`comment_num`, "
                            "`content`, `trans_content`) "
                            "VALUES ('" + str(
                                lec_id) + "', '" + dates[i] + "','" + str(
                                i + 1) + "', '" + comment + "','" + text + "');")
                        self.__db_cnx.commit()
                    except mysql.connector.Error as err:
                        print("problem - ", "__get_comments", err)
                # print("comment" + str(i) + ":  " + comment + "\n")
        return comment_list

    def __get_lecturer(self, id_number):
        lec_dict = {}
        page = 1;
        lec_response = self.__get_page(1, id_number)
        index_s = lec_response.find("מתוך")
        lec_size = int(re.sub("[^0-9]", "", lec_response[index_s:index_s + 30]))
        pages = math.ceil(lec_size / 20)  # 20 lecturers per page

        for i in range(pages):
            index_lec = [lec.start() for lec in re.finditer('שם המרצה', lec_response)]  # get all indexes of 'שם המרצה'
            for each_lec in index_lec:
                curr_source = lec_response[each_lec:]
                index_start_name = curr_source.find("<span title=")
                index_end_name = curr_source.find(">", index_start_name)
                lec_name = curr_source[index_start_name + 14:index_end_name - 2]
                index_start_id = curr_source.find("displayRanking.asp?lecturerID")
                index_end_id = curr_source.find("'>", index_start_id)
                lec_id = int(re.sub("[^0-9]", "", curr_source[index_start_id:index_end_id]))
                print(str(lec_id) + ":" + lec_name)
                try:
                    self.__db_cnx.cursor().execute(
                        "INSERT INTO `finalproj`.`lecturers` (`lec_id`, `institute_id`, `lec_name`) VALUES ('" + str(
                            lec_id) + "', '" + str(id_number) + "', '" + lec_name + "');")
                    self.__db_cnx.commit()
                except mysql.connector.Error as err:
                    print("problem - ", "__get_lecturer", err)
                lec_key = lec_name + "_" + str(lec_id)
                lec_dict[lec_key] = self.__get_comments(lec_id)

            page = page + 1
            lec_response = self.__get_page(page, id_number)

        return lec_dict

    def get_details(self):
        details_dict = {}
        start = self.__dargoo_source.find("בחר מוסד לימודים")
        end = self.__dargoo_source.find("</div>", start)
        names = self.__dargoo_source[start:end]
        size = names.count("<option value=")
        for i in range(size):
            id_index = names.find("<option value=") + 14
            id_number = re.sub("[^0-9]", "", names[id_index:id_index + 3])

            # print(id_number)
            if int(id_number) >= 10:
                name_index = id_index + 3
            else:
                name_index = id_index + 2

            names = names[name_index:]
            name = names[0:names.find("</option")]
            if int(id_number) == 22:  # only braude
                try:
                    self.__db_cnx.cursor().execute(
                        "INSERT INTO `finalproj`.`institutes` (`ins_id`, `ins_name`) VALUES ('" + str(
                            id_number) + "', '" + name + "');")
                    self.__db_cnx.commit()
                except mysql.connector.Error as err:
                    print("problem-", "get_details", err)
                print(name)
                details_dict[name + "_" + str(id_number)] = (self.__get_lecturer(id_number))
        return details_dict
