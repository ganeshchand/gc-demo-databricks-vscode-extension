// Databricks notebook source

import org.apache.spark.sql.types._
import org.apache.spark.sql.Row

val schema = StructType(Array(
  StructField("CustomerID", IntegerType, false),
  StructField("FirstName",  StringType, false),
  StructField("LastName",   StringType, false)
))

val data = List(
  Row(1000, "Mathijs", "Oosterhout-Rijntjes"),
  Row(1001, "Joost",   "van Brunswijk"),
  Row(1002, "Stan",    "Bokenkamp"),
)

val rdd = spark.sparkContext.makeRDD(data)
val customers = spark.createDataFrame(rdd, schema)

display(customers) // display is a Databricks notebook function. It is not available in Spark.
