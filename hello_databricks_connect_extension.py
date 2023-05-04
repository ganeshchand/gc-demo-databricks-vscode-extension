import os
is_databricks = True if os.getenv("DATABRICKS_RUNTIME_VERSION") is not None else False
spark = None
if not is_databricks:
  from databricks.connect import DatabricksSession
  from databricks.sdk.core import Config

  config = Config(profile = "dbconnect-dev")
  spark = DatabricksSession.builder.sdkConfig(config).getOrCreate()
else:
    from pyspark.sql import SparkSession
    spark = SparkSession.builder.getOrCreate()  

df = spark.read.table("samples.nyctaxi.trips")
df.show(5)


