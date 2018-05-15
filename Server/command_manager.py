import pickle
from Classes import Lecturer_Class
import datetime
import time


class c_manager:

    def __get_all_lec(self, args):
        args[0].execute("SELECT lec_name,lec_id FROM finalproj.lecturers WHERE institute_id = 22;")
        return pickle.dumps(args[0].fetchall())

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
        years = []
        rates = []
        comments_num = []
        args[0].execute(
            "SELECT max(comment_date) FROM finalproj.lec_comments where lec_id=" + str(args[2]) + ";")
        max_year = (args[0].fetchone())[0]
        max_year = max_year.strftime("%Y")
        args[0].execute(
            "SELECT min(comment_date) FROM finalproj.lec_comments where lec_id=" + str(args[2]) + ";")
        min_year = (args[0].fetchone())[0]
        min_year = min_year.strftime("%Y")
        args[0].execute("SELECT lec_name FROM finalproj.lecturers WHERE lec_id=" + str(args[2]) + ";")
        name = "".join(args[0].fetchone())
        lec = Lecturer_Class.Lecturer(str(args[2]), name, {})

        for i in range(int(max_year) - int(min_year) + 1):
            args[0].execute(
                "SELECT comment_num,trans_content FROM finalproj.lec_comments where lec_id=" + str(
                    args[2]) + " and year(comment_date)=" + str(int(max_year) - i) + ";")
            lec.comments = dict(args[0].fetchall())
            rate = lec.analyze_comments()
            if rate != -1:
                years.append(int(max_year) - i)
                rates.append(round(rate, 2))
                comments_num.append(len(lec.comments))

        rate_dict['years'] = years
        rate_dict['rates'] = rates
        rate_dict['comments_num'] = comments_num

        return pickle.dumps(rate_dict)

    def switch_demo(self, argument):
        switcher = {
            "get_lecturers": self.__get_all_lec,
            "get_institutes": self.__get_all_ins,
            "analyze_comments": self.__analyze_commments,
            "analyze_comments_by_period": self.__comments_by_period

        }
        if not switcher.get(argument[1]):
            return None
        return switcher.get(argument[1])(argument)
