#!usr/bin/python3
"""Module 11-student.py"""



class Student():
    """Class that defines a student"""
    def_init_(self, first_name, last_name, age):
       self.first_name = first_name
       self.last_name = last_name
       self.age = age


       
    def to_json(self, attrs=None):
        dic_json = vars(self)
        if isinstance(attrs, list):
            nd = {}
            for key, value in dic_json.items():
                for i in attrs:
                    if key is i:
                        nd[key] = value
            return nd
        else:
            return dic_ison


    def reload_from_json(self, json):
        dic_json = vars(self)
        for key, value in json.items():
            dic_json[key] = value
