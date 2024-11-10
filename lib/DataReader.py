from ConfigReader import get_app_configs
from pyspark.sql.functions import *

# Reading the data and returning the dataframe

def get_path_info(var):
    if lower(var) == 'customer':
        return 'customers.file.path'
    else:
        return 'orders.file.path'

#defining customers schema
def get_customers_schema():
    schema = "customer_id int,customer_fname string,customer_lname string,username string,password string,address string,city string,state string,pincode string"
    return schema

#defining orders schema

def get_orders_schema():
    schema = "order_id int,order_date string,customer_id int,order_status string"
    return schema

def read_data_frame(spark,env,file_path,header = 'true'):
    file_path_data = get_app_configs(env)[file_path]
    if 'customers.csv' in file_path_data:
        schema = get_customers_schema()
    elif 'orders.csv' in file_path_data:
        schema = get_orders_schema()

    return spark.read \
            .format('csv') \
            .option('header', header) \
            .schema(schema) \
            .load(file_path_data)
