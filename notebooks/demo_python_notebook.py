# Databricks notebook source
from pyspark.sql.types import *

schema = StructType([
  StructField('CustomerID', IntegerType(), False),
  StructField('FirstName',  StringType(),  False),
  StructField('LastName',   StringType(),  False)
])

data = [
  [ 1000, 'Mathijs', 'Oosterhout-Rijntjes' ],
  [ 1001, 'Joost',   'van Brunswijk' ],
  [ 1002, 'Stan',    'Bokenkamp' ]
]

customers = spark.createDataFrame(data, schema)
customers.show()