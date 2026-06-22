from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import os

spark = SparkSession.builder.appName("Sales Data Analysis").getOrCreate()

df = spark.read.csv("sales_data.csv", header=True, inferSchema=True)

# 🔥 FIX: strip spaces from column names
df = df.toDF(*[c.strip() for c in df.columns])

print("\n===== Cleaned Columns =====")
print(df.columns)

df.show()

# Now this will work
sorted_df = df.orderBy(col("sales").desc())
sorted_df.show()

top3_df = sorted_df.limit(3)
top3_df.show()

filtered_df = df.filter(col("sales") > 80000)
filtered_df.show()

output_path = "output/filtered_sales.csv"

if os.path.exists(output_path):
    import shutil
    shutil.rmtree(output_path)

filtered_df.coalesce(1).write.mode("overwrite").option("header", True).csv(output_path)

spark.stop()