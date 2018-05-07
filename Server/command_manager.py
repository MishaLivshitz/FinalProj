import pickle


class c_manager:

    def __get_all_lec(self, args):
        args[0].execute("SELECT lec_id,lec_name FROM finalproj.lecturers WHERE institute_id = 11;")
        return pickle.dumps(args[0].fetchall())

    def __get_all_ins(self, args):
        args[0].execute("SELECT * FROM finalproj.institutes;")
        return pickle.dumps(args[0].fetchall())

    def __analyze_commments(self, args):
        args[0].execute("SELECT comment_id,content FROM finalproj.comments WHERE lec_id=" + str(args[2]) + " ;")
        return pickle.dumps(args[0].fetchall())

    def switch_demo(self, argument):
        switcher = {
            "get_lec": self.__get_all_lec,
            "get_ins": self.__get_all_ins,
            "analyze_comments": self.__analyze_commments

        }
        if not switcher.get(argument[1]):
            return None
        return switcher.get(argument[1])(argument)
