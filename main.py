import urllib.request
import re
import math
import pyodbc

from bs4 import BeautifulSoup
from Classes import Institute, Lecturer
import mysql.connector


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


def get_source_code(url):
    request = urllib.request.Request(url)
    return urllib.request.urlopen(request)


def get_page(page, id_number):
    url = "http://www.dargoo.co.il/searchResult.asp?page=" + str(page) + "&searchby=3&ddlCategories=" + str(
        id_number) + "&searchword=&button_search="
    lec_response = myencode(get_source_code(url).read())
    return lec_response

def get_comments(lec_id):
    comment_response = get_source_code("http://dargoo.co.il/displayRanking.asp?lecturerID="+str(lec_id))


def get_lecturer(id_number):
    page = 1;
    lec_response = get_page(1, id_number)
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
            #try:
             #   data.execute(
              #      "INSERT INTO `finalproj`.`lecturers` (`lec_id`, `institute_id`, `lec_name`) VALUES ('" + str(
               #         lec_id) + "', '" + str(id_number) + "', '" + lec_name + "');")
                #cnx.commit()
            #except mysql.connector.Error as err:
             #   print("problem")

            get_comments(lec_id)


        page = page + 1
        lec_response = get_page(page, id_number)

    return


def get_details(dargoo_source):
    start = dargoo_source.find("בחר מוסד לימודים")
    end = dargoo_source.find("</div>", start)
    names = dargoo_source[start:end]
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
       # try:
        #    data.execute("INSERT INTO `finalproj`.`institutes` (`ins_id`, `ins_name`) VALUES ('" + str(
         #       id_number) + "', '" + name + "');")
          #  cnx.commit()
        #except mysql.connector.Error as err:
         #   print("problem")
        print(name)
        get_lecturer(id_number)
    return


#cnx = mysql.connector.connect(user='root', password='misha1991',
 #                             host='127.0.0.1',
  #                            database='finalproj')
#data = cnx.cursor()
response = get_source_code("http://www.dargoo.co.il/")
get_details(myencode(response.read()))
