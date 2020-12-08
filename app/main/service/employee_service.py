#!/usr/bin/env python3.6
from flask import request
from app.main import db
from app.main.model.employee import Employee


def create_emp():
    emp_name = request.json['emp_name']
    email = request.json['email']
    return create_employee(emp_name, email)


def create_employee(emp_name, email):
    new_emp = Employee(emp_name, email)
    db.session.add(new_emp)
    db.session.commit()
    return new_emp


def get_emps():
    return Employee.query.all()


def get_emp(id):
    emp = Employee.query.get(id)
    return emp if emp else {'emp_name': 'No emp with given id'}


def update_emp(id):
    emp_name = request.json['emp_name']
    email = request.json['email']
    return update_employee(id, emp_name, email)


def update_employee(emp_id, emp_name, email):
    emp = Employee.query.get(emp_id)
    if emp:
        emp.emp_name = emp_name
        emp.email = email
        db.session.commit()
    return emp if emp else {'emp_name': 'No emp with given id'}


def delete_emp(id):
    emp = Employee.query.get(id)
    if emp:
        db.session.delete(emp)
        db.session.commit()
        return emp
    return {'emp_name': 'No emp with given id'}




