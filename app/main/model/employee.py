#!/usr/bin/env python3.6

from .. import db, ma


class Employee(db.Model):
    emp_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    emp_name = db.Column(db.String(70))
    email = db.Column(db.String(100))

    def __init__(self, emp_name, email):
        self.emp_name = emp_name
        self.email = email

    def __repr__(self):
        return "<Employee '{}'>".format(self.emp_id)


class EmpSchema(ma.Schema):
    class Meta:
        fields = ('emp_id', 'emp_name', 'email')
