#!/usr/bin/env python3.6

from flask import request, jsonify
from ..service.employee_service import *
from app.main.model.employee import EmpSchema
from app.app_objs import app


emp_schema = EmpSchema()
emps_schema = EmpSchema(many=True)


@app.route('/emps', methods=['POST'])
def create_emp_route():
    return emp_schema.jsonify(create_emp())


@app.route('/emps', methods=['GET'])
def get_emps_route():
    all_emps = get_emps()
    result = emps_schema.dump(all_emps)
    return jsonify(result)


@app.route('/emps/<id>', methods=['GET'])
def get_emp_route(id):
    return emp_schema.jsonify(get_emp(id))


@app.route('/emps/<id>', methods=['PUT'])
def update_emp_route(id):
    return emp_schema.jsonify(update_emp(id))


@app.route('/emps/<id>', methods=['DELETE'])
def delete_emp_route(id):
    return emp_schema.jsonify(delete_emp(id))


@app.route('/', methods=['GET'])
def index():
    return jsonify({'status': 1})

