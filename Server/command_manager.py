import pickle
import re

from Classes import Lecturer_Class
import datetime
import time
from collections import Counter


class c_manager:

    def __get_all_lec(self, args):
        args[0].execute("SELECT lec_name,lec_id FROM finalproj.lecturers WHERE institute_id = " + str(
            args[2]) + " order by lec_name;")
        return pickle.dumps(args[0].fetchall())

    def __get_all_lec_by_id(self, args):
        lec_table = []
        args[0].execute("SELECT lec_id,lec_name,faculty FROM finalproj.lecturers WHERE institute_id = " + str(
            args[2]) + " order by lec_name;")
        lecturers = args[0].fetchall()

        for lec in lecturers:
            lec_data = {}
            curr_lec = Lecturer_Class.Lecturer(lec[0], lec[1], {})
            lec_data["lecturer_name"] = lec[1]
            lec_data["faculty"] = lec[2]
            args[0].execute(
                "SELECT comment_num,trans_content FROM finalproj.lec_comments where lec_id='" + str(lec[0]) + "';")
            curr_lec.comments = dict(args[0].fetchall())
            lec_data["rate"] = curr_lec.analyze_comments()
            lec_data["num_of_comments"] = curr_lec.comments.__len__()
            curr_lec.comments.clear()
            lec_table.append(lec_data)
            print(lec_table.__sizeof__())
        return pickle.dumps(lec_table)

    def __get_all_ins(self, args):
        args[0].execute("SELECT ins_name,ins_id FROM finalproj.institutes;")
        return pickle.dumps(args[0].fetchall())

    def __analyze_commments(self, args):
        args[0].execute("SELECT lec_name FROM finalproj.lecturers WHERE lec_id=" + str(args[2]) + ";")
        name = "".join(args[0].fetchone())
        args[0].execute(
            "SELECT comment_num,trans_content FROM finalproj.lec_comments WHERE lec_id=" + str(args[2]) + " ;")
        lec = Lecturer_Class.Lecturer(str(args[2]), name, dict(args[0].fetchall()))
        rate = lec.analyze_comments()
        return pickle.dumps(rate)

    def __comments_by_period(self, args):
        rate_dict = {}
        rates = []
        comments_num = []

        args[0].execute("select distinct year(lec_comments.comment_date) from lec_comments where lec_id=" + str(
            args[2]) + " order by comment_date;")
        years = args[0].fetchall()
        args[0].execute("SELECT lec_name FROM finalproj.lecturers WHERE lec_id=" + str(args[2]) + ";")
        name = "".join(args[0].fetchone())
        lec = Lecturer_Class.Lecturer(str(args[2]), name, {})

        for i in range(len(years)):
            years[i] = re.sub("[^0-9]", "", str(years[i]))
            args[0].execute(
                "SELECT comment_num,trans_content FROM finalproj.lec_comments where lec_id=" + str(
                    args[2]) + " and year(comment_date)=" + str(years[i]) + ";")
            lec.comments = dict(args[0].fetchall())
            print(len(lec.comments))
            print(years[i])
            rate = lec.analyze_comments()
            if rate != -1:
                rates.append(round(rate, 2))
                comments_num.append(len(lec.comments))
            else:
                years.pop(i)

        rate_dict['years'] = years
        rate_dict['rates'] = rates
        rate_dict['comments_num'] = comments_num
        return pickle.dumps(rate_dict)

    def __comments_by_department(self, args):
        data_res = {}
        avg_rate = 0
        args[0].execute("SELECT distinct faculty FROM finalproj.lecturers where institute_id=" + str(args[2]) + ";")
        faculties = [i[0] for i in args[0].fetchall()]
        for i in range(len(faculties) - 1, 0, -1):
            if len(faculties[i].split(',')) > 1:
                faculties.pop(i)
        for faculty in faculties:
            args[0].execute("select lec_comments.lec_id ,trans_content ,lec_name from"
                            " (select lec_id, lec_name FROM "
                            "finalproj.lecturers where faculty like'%" + faculty + "%'"
                                                                                   " and institute_id=" + str(args[
                                                                                                                  2]) + ") as t,lec_comments where t.lec_id=lec_comments.lec_id ;")

            data = args[0].fetchall()
            comment_name_dict = {}

            lec_list = []
            comment_list = {}
            id_counts = Counter([lec_id[0] for lec_id in data])
            i = 0
            while i < len(data):
                comment_name_dict["lec_name"] = data[i][2]
                for j in range(id_counts[data[i][0]]):
                    comment_list[i + j] = (data[i + j][1])

                lec = Lecturer_Class.Lecturer(data[i][0], comment_name_dict["lec_name"], comment_list.copy())
                lec_list.append(lec)
                comment_list.clear()
                i = i + j + 1

            for lec in lec_list:
                avg_rate += lec.analyze_comments() * len(lec.comments)

            avg_rate = avg_rate / len(data)
            data_res[faculty] = [avg_rate, len(data)]

        return pickle.dumps(data_res)

    def __ins_comments_by_period(self, args):
        args[0].execute("select lecturers.lec_id from lecturers where institute_id=" + str(args[2]) + ";")
        lec_list = args[0].fetchall()
        data_dict_rate = {}
        data_dict_comments_num = {}
        data_dict_return = {}
        for lec in lec_list:
            lec = int(re.sub("[^0-9]", "", str(lec)))
            data_rec = dict(pickle.loads(self.__comments_by_period([args[0], '', lec]), encoding="ASCII"))
            for i in range(len(data_rec["years"])):
                if data_rec["years"][i] not in data_dict_rate:
                    data_dict_rate[str(data_rec["years"][i])] = []
                    data_dict_comments_num[str(data_rec["years"][i])] = []
                data_dict_rate[str(data_rec["years"][i])].append(data_rec["rates"][i])
                data_dict_comments_num[str(data_rec["years"][i])].append(data_rec["comments_num"][i])

        for key, value in data_dict_rate.items():
            rate_sum = 0
            comments_sum = 0
            for i in range(len(value)):
                rate_sum += value[i] * data_dict_comments_num[key][i]
                comments_sum += data_dict_comments_num[key][i]
            data_dict_return[key] = rate_sum / comments_sum

        return pickle.dumps(data_dict_return)

    def switch_demo(self, argument):
        switcher = {
            "get_lecturers": self.__get_all_lec,
            "get_lecturers_table": self.__get_all_lec_by_id,
            "get_institutes": self.__get_all_ins,
            "analyze_comments": self.__analyze_commments,
            "analyze_comments_by_period": self.__comments_by_period,
            "analyze_comments_by_department": self.__comments_by_department,
            "analyze_ins_comments_by_period": self.__ins_comments_by_period

        }
        if not switcher.get(argument[1]):
            return None
        return switcher.get(argument[1])(argument)
