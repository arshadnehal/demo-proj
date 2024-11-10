import configparser
from pyspark import SparkConf


# Reading application data in the dictionary

def get_app_configs(env):
    configs = configparser.ConfigParser()
    configs.read('configs/application.conf')
    app_info = {}
    for key, value in configs.items(env):
        app_info[key] = value
    return app_info

# Loading Pyspark configuration and creating spark conf

def get_spark_configs(env):
    configs = configparser.ConfigParser()
    configs.read('configs/spark.conf')
    conf = SparkConf()
    for key,value in configs.items(env):
        conf.set(key,value)
    return conf
