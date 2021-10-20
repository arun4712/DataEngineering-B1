# Databricks notebook source
dbutils.widgets.removeAll()

# COMMAND ----------

#dbutils widgets commands
#to create 
dbutils.widgets.text("MovieId","")

# COMMAND ----------

dbutils.widgets.dropdown("MovieId","1",["1","2","3"])

# COMMAND ----------

dbutils.widgets.multiselect("MovieId","1",["1","2","3"])

# COMMAND ----------

#to get input from widgets
movieid=dbutils.widgets.get("MovieId")

# COMMAND ----------

print(movieid)

# COMMAND ----------

# configs = {"fs.azure.account.auth.type": "OAuth",
#           "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
#           "fs.azure.account.oauth2.client.id": "e399ad64-eefa-4b88-a947-6c4267865e2a",
#           "fs.azure.account.oauth2.client.secret": dbutils.secrets.get(scope="scopenm",key="ADLSappkey"),
#           "fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/bdc88327-5e6f-4d59-95e8-671703c2e2de/oauth2/token"}

# # Optionally, you can add <directory-name> to the source URI of your mount point.
# dbutils.fs.mount(
#   source = "abfss://devcontainer@devstoragerg.dfs.core.windows.net/",
#   mount_point = "/mnt/connectADLS1",
#   extra_configs = configs)

# COMMAND ----------

dbutils.fs.mounts()

# COMMAND ----------

#to run cell=>shift+enter
dfmovie = spark.read.format("csv").option("header","true").load("/mnt/connectADLS1/movies.csv")

# COMMAND ----------

dfmovie.show(10)

# COMMAND ----------

#by default show() shows ony 20 records
dfmovie.show()

# COMMAND ----------

display(dfmovie)

# COMMAND ----------

dfmovie.createOrReplaceTempView("vwMovie")  #createOrReplaceTempView is used to create temporary view

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from vwMovie

# COMMAND ----------

qry="select * from vwMovie where movieId in ({})"
print(qry)
x=qry.format(movieid)
print(x)
dfx=spark.sql(x)


# COMMAND ----------

qry="select * from vwMovie where movieId={}"
dfx=spark.sql(qry.format(movieid))

# COMMAND ----------

dfx.show()

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE TABLE vwMovie

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from vwMovie limit 10

# COMMAND ----------

# Spark sql
dftenrecords=spark.sql("select * from vwMovie limit 10")

# COMMAND ----------

display(dftenrecords)

# COMMAND ----------

#mode:-
append->100+10=110
overwrite->100+10->10

# COMMAND ----------

#csv
#parquet
#delta

# COMMAND ----------

dftenrecords.write.format("csv").mode("overwrite").options(header='true',overwriteSchema='true').save("/mnt/connectADLS1/procData/")

# COMMAND ----------

dbutils.fs.rm("/mnt/connectADLS1/procData/",recurse=True)

# COMMAND ----------

#parquet file format
dftenrecords.write.format("parquet").mode("overwrite").options(header='true',overwriteSchema='true').save("/mnt/connectADLS1/procData/")

# COMMAND ----------

#delta file format(it follows ACID property)
dftenrecords.write.format("delta").mode("overwrite").options(header='true',overwriteSchema='true').save("/mnt/connectADLS1/procDataDelta/")

# COMMAND ----------

df9=spark.read.format("delta").option("header","true").load("/mnt/connectADLS1/procDataDelta/")

# COMMAND ----------

df9.show()

# COMMAND ----------

dftenrecords.printSchema()

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE TABLE vwMovie

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from vwMovie

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from vwMovie where movieId in(2,4,6,5,6,97,5)

# COMMAND ----------

df1=spark.sql("select * from vwMovie where movieId in(2,4,6,5,6,97,5)")

# COMMAND ----------

df1.show()

# COMMAND ----------

df1.write.format("csv").mode("overwrite").options(header='true',overwriteSchema='true').save("/mnt/connectADLS1/processedData/")

# COMMAND ----------

df2 = spark.read.format("csv").option("header","true").load("/mnt/connectADLS1/processedData/")

# COMMAND ----------

df2.show()

# COMMAND ----------

df2.count()

# COMMAND ----------

#writing modes->append and overwrite
df2.write.format("csv").mode("append").options(header='true',overwriteSchema='true').save("/mnt/connectADLS1/processedData/")

# COMMAND ----------

df2 = spark.read.format("csv").option("header","true").load("/mnt/connectADLS1/processedData/")

# COMMAND ----------

df3 = spark.read.format("csv").option("header","true").load("/mnt/connectADLS1/processedData/")

# COMMAND ----------

df3.count()

# COMMAND ----------

# dbutils.widgets.removeAll()

# COMMAND ----------

# dbutils.widgets.dropdown("Type",'')

# COMMAND ----------

# dbutils.fs.ls()

# COMMAND ----------

# dbutils.fs.rm()

# COMMAND ----------

# dbutils.fs.mv()
# dbutils.fs.cp()

# COMMAND ----------

# run location
# RDD
# dataset
# dataframe
# immutable
# ACID property of delta table

# COMMAND ----------

dbutils.fs.mounts()

# COMMAND ----------

#command to unmount the  path
dbutils.fs.unmount("/mnt/<mount-name>")

# COMMAND ----------

dbutils.fs.ls("/mnt/connectADLS1/")

# COMMAND ----------

#dbutils.fs.cp(path1,path2)
dbutils.fs.cp("/mnt/connectADLS1/ratings.csv","/mnt/connectADLS1/newdata/")

# COMMAND ----------

dbutils.fs.rm("/mnt/connectADLS1/newdata/ratings.csv")

# COMMAND ----------

#dbutils.fs.mv(path1,path2)
dbutils.fs.mv("/mnt/connectADLS1/tags.csv","/mnt/connectADLS1/newdata/")

# COMMAND ----------


