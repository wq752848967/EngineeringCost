# cong:utf-8
from flask import jsonify
from flask import render_template
from flask import request
import app.service as service
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

@app.route("/test", methods=['POST', ])
def test():
    input_data = request.form
    content = input_data['content']
    service.testSchemaInit(content)

@app.route("/query_avg_price_by_pro", methods=['POST', ])
def query_avg_price_by_pro():
    input_data = request.form
    province_name = input_data['province_name']
    building_type = input_data['building_type']
    all_data = model.query_all_info()
    key=(province_name,building_type)

    comp = all_data[1][key]
    avg_price =  all_data[2][key]
    comp['avg_price'] = avg_price

    result = {'data':comp.to_json()}

    return result



@app.route("/query_building_type_by_pro", methods=['POST', ])
def query_building_type_by_pro():
    input_data = request.form
    province_name = input_data['province_name']
    all_data = model.query_all_info()

    building_types =  all_data[0][province_name]
    return jsonify(data=building_types)