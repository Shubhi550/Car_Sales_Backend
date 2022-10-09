import json
from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin
import pdb
  
app = Flask(__name__) 
CORS(app) 

with open("config.json") as f:
    f_data = json.load(f)
    host= f_data["hostname"]
    user= f_data["username"]
    password= f_data["password"]
    database= f_data["database"]

app.config['MYSQL_HOST'] = host
app.config['MYSQL_USER'] = user
app.config['MYSQL_PASSWORD'] = password
app.config['MYSQL_DB'] = database
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

# get table data
@app.route('/sales_details')
def car_sales_details():
    cursor = mysql.connection.cursor()
    table_data = "SELECT * FROM car_sales_table"
    cursor.execute(table_data)
    # pdb.set_trace()
    results = cursor.fetchall()
    return jsonify(results)

# add table data
@app.route('/add_sales', methods =['GET', 'POST'])
def Customize_add_sales():
    msg = ''
    data_posted = request.get_json()
    if request.method == 'POST' and 'sales_id' in data_posted and 'Date of Purchase' in data_posted and 'Customer_id' in data_posted and 'Fuel' in data_posted and 'Premium' in data_posted and 'VEHICLE_SEGMENT' in data_posted and 'SellingPrice' in data_posted and 'Power_steering' in data_posted and 'airbags' in data_posted and 'sunroof' in data_posted and 'Matt_finish' in data_posted and 'music system' in data_posted and 'Customer_Gender' in data_posted and 'Customer_Income group' in data_posted and 'Customer_Region' in data_posted and 'Customer_Marital_status' in data_posted:
        sales_id= data_posted['sales_id']
        date_of_purchase= data_posted['Date of Purchase']
        customer_id= data_posted['Customer_id']
        fuel= data_posted['Fuel']
        premium= data_posted['Premium']
        vehicle_segment= data_posted['VEHICLE_SEGMENT']
        selling_price= data_posted['SellingPrice']
        power_steering= data_posted['Power_steering']
        airbags= data_posted['airbags']
        sunroof= data_posted['sunroof']
        matt_finish= data_posted['Matt_finish']
        music_system= data_posted['music system']
        customer_gender= data_posted['Customer_Gender']
        customer_income_group= data_posted['Customer_Income group']
        customer_region= data_posted['Customer_Region']
        customer_marital_status= data_posted['Customer_Marital_status']
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM car_sales_table WHERE sales_id = % s OR Customer_id = % s', (sales_id, customer_id, ))
        id_exits = cursor.fetchone()
        if id_exits:
            msg = 'Sales ID or Customer ID already exists !'
        else:
            cursor.execute('INSERT INTO car_sales_table VALUES (% s, % s, % s, % s, % s, % s, % s, % s, % s, % s, % s, % s, % s, % s, % s, % s)', (sales_id, date_of_purchase, customer_id, fuel, premium, vehicle_segment, selling_price, power_steering, airbags, sunroof, matt_finish, music_system, customer_gender, customer_income_group, customer_region, customer_marital_status, ))
            mysql.connection.commit()
            msg = 'Sales added to DB succesfully!!'
    elif request.method == 'POST':
        msg = 'Please fill out the sales details in customize page !'
    return msg

# filter details by sales_id or customer_id for Customize > Edit
@app.route("/filter_sales", methods =['GET', 'POST'])
def Filter_sales():
        data_posted = request.get_json()
        sales_id= data_posted['sales_id']
        customer_id= data_posted['Customer_id']
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM car_sales_table WHERE sales_id = % s OR Customer_id = % s', (sales_id, customer_id, ))
        results = cursor.fetchone()
        return jsonify(results)

# edit a sales entry
@app.route("/edit_sales", methods =['GET', 'POST'])
def Customize_edit_sales():
    msg = ''
    data_posted = request.get_json()
    if request.method == 'POST' and 'sales_id' in data_posted and 'Date of Purchase' in data_posted and 'Customer_id' in data_posted and 'Fuel' in data_posted and 'Premium' in data_posted and 'VEHICLE_SEGMENT' in data_posted and 'SellingPrice' in data_posted and 'Power_steering' in data_posted and 'airbags' in data_posted and 'sunroof' in data_posted and 'Matt_finish' in data_posted and 'music system' in data_posted and 'Customer_Gender' in data_posted and 'Customer_Income group' in data_posted and 'Customer_Region' in data_posted and 'Customer_Marital_status' in data_posted:
        sales_id= data_posted['sales_id']
        date_of_purchase= data_posted['Date of Purchase']
        customer_id= data_posted['Customer_id']
        fuel= data_posted['Fuel']
        premium= data_posted['Premium']
        vehicle_segment= data_posted['VEHICLE_SEGMENT']
        selling_price= data_posted['SellingPrice']
        power_steering= data_posted['Power_steering']
        airbags= data_posted['airbags']
        sunroof= data_posted['sunroof']
        matt_finish= data_posted['Matt_finish']
        music_system= data_posted['music system']
        customer_gender= data_posted['Customer_Gender']
        customer_income_group= data_posted['Customer_Income group']
        customer_region= data_posted['Customer_Region']
        customer_marital_status= data_posted['Customer_Marital_status']
        cursor = mysql.connection.cursor()
        cursor.execute('UPDATE car_sales_table SET `sales_id` = % s, `Date of Purchase` = % s, `Customer_id` = % s, `Fuel` = % s, `Premium` = % s, `VEHICLE_SEGMENT` = % s, `SellingPrice` = % s, `Power_steering` = % s, `airbags` = % s, `sunroof` = % s, `Matt_finish` = % s, `music system` = % s, `Customer_Gender` = % s, `Customer_Income group` = % s, `Customer_Region` = % s, `Customer_Marital_status` = % s WHERE `sales_id` = % s OR `Customer_id` = % s', (sales_id, date_of_purchase, customer_id, fuel, premium, vehicle_segment, selling_price, power_steering, airbags, sunroof, matt_finish, music_system, customer_gender, customer_income_group, customer_region, customer_marital_status , (sales_id, ), (customer_id, ), ))
        mysql.connection.commit()
        msg = 'Sales updated successfully !!'
    else:
        msg = 'Please fill the sales details for updation !!'
    
    return msg

if __name__ == '__main__':
    app.run(debug=True)