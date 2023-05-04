def spark_session_factory():
  import os
  if "DATABRICKS_RUNTIME_VERSION" in os.environ:
    # return the SparkSession from Databricks Cluster
    return spark
  else:
    from databricks.connect import DatabricksSession
    # Add the options you need and return DatabricksSession 
    return DatabricksSession.builder.getOrCreate()


spark = spark_session_factory()

df = spark.read.table("samples.nyctaxi.trips")
df.show(5)


