import pyspark
from pyspark.sql import SparkSession

#importando as classes que possuem as funcoes do Spark que vamos utilizar nessa aula
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql import *

spark = SparkSession.builder.getOrCreate()

# df = (spark.read.csv('access_log_Jul95'))
df = (spark.read
     .option('sep', ' ')
     .csv('access_log_Jul95'))

df_with_column = df.withColumnRenamed("_c0","host") \
.withColumnRenamed("_c5", "resquest") \
.withColumnRenamed("_c6", "return_code") \
.withColumnRenamed("_c7", "bytes") \
.withColumn("time_stamp", concat(df["_c3"], df["_c4"])) \
.drop("_c1").drop("_c2").drop("_c3").drop("_c4")

df_with_column.cache()

unique_hosts = df_with_column.select("host").distinct().count()

error_count = df_with_column.filter(df_with_column.return_code == "404").count()

most_recent = df_with_column.filter(df_with_column.return_code == "404").orderBy(df_with_column.time_stamp.desc())

df_date = df_with_column.withColumn('date_column', regexp_replace(split(df_with_column['time_stamp'], ':')[0], "\[", ""))

df_date_group = df_date.groupBy('date_column').count()

df_with_column.createOrReplaceTempView('temp_table')

sql_str = "select sum(bytes) as sum_bytes from {0} ".format("temp_table")

df_sum = spark.sql(sql_str)

print('Distinct hosts: {0}'.format(unique_hosts))
print('404 errors: {0}'.format(error_count))

print('\nTop 5 most frequent 404')
most_recent.show(5, False)

print('\n 404 per day')
df_date_group.show(100, False)

print('\n Sum Bytes')
df_sum.show(10, False)
