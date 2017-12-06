# cong:utf-8
from flask import jsonify
from flask import render_template
from flask import request
import app.interfaces as model
from app import app


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/hello", methods=['GET', ])
def hello():
    return jsonify(msg=model.query_building_types(u"上海"))

@app.route("/query_building_types", methods=['POST', ])
def query_building_types():
    input_data = request.form
    province_name = input_data['province_name']
    return jsonify(data=model.query_building_types(province_name))

@app.route("/query_first15_material", methods=['POST', ])
def query_first15_material():
    input_data = request.form
    province_name = input_data['province_name']
    building_type = input_data['building_type']
    result_df = model.query_first15_material(province_name,building_type).to_json()
    print(result_df)
    out_data = {"data":result_df}
    return result_df


@app.route("/query_cost_per_area", methods=['POST', ])
def query_cost_per_area():
    input_data = request.form
    province_name = input_data['province_name']
    building_type = input_data['building_type']
    prices = input_data['prices'].splite(",")

    return jsonify(data=model.query_cost_per_area(province_name,building_type,prices))