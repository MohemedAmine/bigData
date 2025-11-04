from pyspark import SparkContext

# Initialisation du SparkContext
sc = SparkContext("local", "Average Height")
rdd = sc.textFile("hdfs:///user/hadoop/arbres.csv")
header = rdd.first()

def safe_float(value):
    try:
        return float(value)
    except ValueError:
        return None
    
heights = rdd.filter(lambda x: x != header and len(x.split(";")) == 13).map(lambda x: safe_float(x.split(";")[6]))  # On applique safe_float

heights = heights.filter(lambda x: x is not None)

average_height = heights.mean()

print("Hauteur moyenne des arbres : {}".format(average_height))
