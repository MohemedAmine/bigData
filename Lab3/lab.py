# lab.py
from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    countDistinct, split, col, row_number, sum as spark_sum
)
from pyspark.sql.window import Window

if __name__ == '__main__':
  
    spark = SparkSession.builder.appName("NgramAnalysis").getOrCreate()

    df = spark.read.csv("hdfs:///user/hadoop/ngram.csv", sep="\t", header=False, inferSchema=True)

    df = df.toDF("Ngram", "Year", "Count", "Pages", "Books")

    df.createOrReplaceTempView("ngram_table")

    print("3.1) Bigrams with Count > 5 (SQL):")
    result_3_1_sql = spark.sql("""
        SELECT Ngram, Year, Count, Pages, Books
        FROM ngram_table
        WHERE Count > 5
    """)
    result_3_1_sql.show(truncate=False)

    print("3.1) Bigrams with Count > 5 (DataFrame API):")
    result_3_1_api = df.filter(col("Count") > 5)
    result_3_1_api.show(truncate=False)

    print("3.2) Total number of bigrams for each year (SQL):")
    result_3_2_sql = spark.sql("""
        SELECT Year, COUNT(Ngram) AS total_bigrams
        FROM ngram_table
        GROUP BY Year
        ORDER BY Year
    """)
    result_3_2_sql.show(truncate=False)

    print("3.2) Total number of bigrams for each year (DataFrame API):")
    result_3_2_api = df.groupBy("Year").count().withColumnRenamed("count", "total_bigrams").orderBy("Year")
    result_3_2_api.show(truncate=False)

    print("3.3) Bigrams with highest Count for each year (SQL):")
    query_3_3_sql = """
        SELECT Ngram, Year, Count
        FROM ngram_table t1
        WHERE Count = (
            SELECT MAX(Count)
            FROM ngram_table t2
            WHERE t2.Year = t1.Year
        )
        ORDER BY Year
    """
    result_3_3_sql = spark.sql(query_3_3_sql)
    result_3_3_sql.show(truncate=False)

    print("3.3) Bigrams with highest Count for each year (DataFrame API):")
    windowSpec = Window.partitionBy("Year").orderBy(col("Count").desc())
    df_with_rank = df.withColumn("rank", row_number().over(windowSpec))
    result_3_3_api = df_with_rank.filter(col("rank") == 1).select("Ngram", "Year", "Count").orderBy("Year")
    result_3_3_api.show(truncate=False)

    print("3.4) Bigrams that appeared in 20 different years (SQL):")
    query_3_4_sql = """
        SELECT Ngram
        FROM ngram_table
        GROUP BY Ngram
        HAVING COUNT(DISTINCT Year) = 20
    """
    result_3_4_sql = spark.sql(query_3_4_sql)
    result_3_4_sql.show(truncate=False)

    print("3.4) Bigrams that appeared in 20 different years (DataFrame API):")
    result_3_4_api = df.groupBy("Ngram") \
                       .agg(countDistinct("Year").alias("year_count")) \
                       .filter(col("year_count") == 20) \
                       .select("Ngram")
    result_3_4_api.show(truncate=False)

    print("3.5) Bigrams with '!' in first part and '9' in second part (SQL):")
    query_3_5_sql = """
        SELECT Ngram
        FROM ngram_table
        WHERE SPLIT(Ngram, ' ')[0] LIKE '%!%' AND SPLIT(Ngram, ' ')[1] LIKE '%9%'
    """
    result_3_5_sql = spark.sql(query_3_5_sql)
    result_3_5_sql.show(truncate=False)

    print("3.5) Bigrams with '!' in first part and '9' in second part (DataFrame API):")
    df_split = df.withColumn("first_part", split(col("Ngram"), " ")[0]) \
                 .withColumn("second_part", split(col("Ngram"), " ")[1])
    result_3_5_api = df_split.filter(col("first_part").contains("!") & col("second_part").contains("9")).select("Ngram")
    result_3_5_api.show(truncate=False)

    print("3.6) Bigrams that appeared in all years (SQL):")
    query_3_6_sql = """
        WITH total_years AS (
            SELECT COUNT(DISTINCT Year) AS total FROM ngram_table
        )
        SELECT Ngram
        FROM ngram_table
        GROUP BY Ngram
        HAVING COUNT(DISTINCT Year) = (SELECT total FROM total_years)
    """
    result_3_6_sql = spark.sql(query_3_6_sql)
    result_3_6_sql.show(truncate=False)

    print("3.6) Bigrams that appeared in all years (DataFrame API):")
    total_years = df.select(countDistinct("Year")).collect()[0][0]
    result_3_6_api = df.groupBy("Ngram") \
                       .agg(countDistinct("Year").alias("year_count")) \
                       .filter(col("year_count") == total_years) \
                       .select("Ngram")
    result_3_6_api.show(truncate=False)

    print("3.7) Total pages and books per bigram per year (SQL):")
    query_3_7_sql = """
        SELECT Ngram, Year, SUM(Pages) AS total_pages, SUM(Books) AS total_books
        FROM ngram_table
        GROUP BY Ngram, Year
        ORDER BY Ngram ASC
    """
    result_3_7_sql = spark.sql(query_3_7_sql)
    result_3_7_sql.show(truncate=False)

    print("3.7) Total pages and books per bigram per year (DataFrame API):")
    result_3_7_api = df.groupBy("Ngram", "Year") \
                       .agg(spark_sum("Pages").alias("total_pages"), spark_sum("Books").alias("total_books")) \
                       .orderBy("Ngram")
    result_3_7_api.show(truncate=False)

    print("3.8) Total number of distinct bigrams per year (SQL):")
    query_3_8_sql = """
        SELECT Year, COUNT(DISTINCT Ngram) AS total_distinct_bigrams
        FROM ngram_table
        GROUP BY Year
        ORDER BY Year DESC
    """
    result_3_8_sql = spark.sql(query_3_8_sql)
    result_3_8_sql.show(truncate=False)

    print("3.8) Total number of distinct bigrams per year (DataFrame API):")
    result_3_8_api = df.groupBy("Year") \
                       .agg(countDistinct("Ngram").alias("total_distinct_bigrams")) \
                       .orderBy(col("Year").desc())
    result_3_8_api.show(truncate=False)

    spark.stop()
