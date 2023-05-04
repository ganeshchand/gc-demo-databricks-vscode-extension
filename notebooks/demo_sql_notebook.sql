-- Databricks notebook source

CREATE TABLE IF NOT EXISTS vscode_demo_customers(
  CustomerID INT,
  FirstName  STRING,
  LastName   STRING
);

-- COMMAND ----------
INSERT INTO vscode_demo_customers VALUES
  (1000, "Mathijs", "Oosterhout-Rijntjes"),
  (1001, "Joost",   "van Brunswijk"),
  (1002, "Stan",    "Bokenkamp");

-- COMMAND ----------
SELECT * FROM vscode_demo_customers;

-- Output:
--
-- +----------+---------+-------------------+
-- |CustomerID|FirstName|           LastName|
-- +----------+---------+-------------------+
-- |      1000|  Mathijs|Oosterhout-Rijntjes|
-- |      1001|    Joost|      van Brunswijk|
-- |      1002|     Stan|          Bokenkamp|
-- +----------+---------+-------------------+

-- COMMAND ----------
DROP TABLE IF EXISTS vscode_demo_customers;