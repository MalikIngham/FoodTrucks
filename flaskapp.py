from flask import Flask, request, render_template, jsonify
import pandas as pd
from collections import OrderedDict
import csv

app = Flask(__name__)


def load_csv():
    with open('Mobile_Food_Facility_Permit.csv', mode='r') as csv_file:
        permits = csv.DictReader(csv_file)
        return list(permits)


@app.route('/')
def index():
    df = pd.DataFrame(permits)
    return render_template("index.html", df=df)


@app.route('/api/add/new-food-truck', methods=['POST'])
def api_add_new_truck():
    if request.form:
        tmp = request.form.to_dict()
        new_food_truck = OrderedDict(tmp)
        permits.append(new_food_truck)
    return jsonify(success=True)


if __name__ == '__main__':
    permits = load_csv()
    app.run(debug=True, host='0.0.0.0', port=2000)
