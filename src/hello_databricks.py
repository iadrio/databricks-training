# Databricks notebook source

# COMMAND ----------

# Creamos el DataFrame directamente con datos de ejemplo
# (Así evitamos depender de archivos externos en el cluster)

data = [
    (1, "Ana", 25, "Madrid"),
    (2, "Carlos", 30, "Barcelona"),
    (3, "Lucia", 28, "Valencia"),
    (4, "Pedro", 35, "Sevilla"),
    (5, "Maria", 22, "Bilbao"),
]

columns = ["id", "nombre", "edad", "ciudad"]

df = spark.createDataFrame(data, columns)

# COMMAND ----------

# Mostramos el schema
df.printSchema()

# COMMAND ----------

# Mostramos los datos
df.show()

# COMMAND ----------

# Una transformación simple: media de edad por ciudad
df.groupBy("ciudad").avg("edad").show()

# COMMAND ----------

print("Hello Databricks! El pipeline funciona correctamente.")
