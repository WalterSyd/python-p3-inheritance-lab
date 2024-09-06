#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        #initializes with empty list attribute "knowledge"
        self.knowledge = []

    def learn(self, new_info_string):
        self.knowledge.append(new_info_string)
        