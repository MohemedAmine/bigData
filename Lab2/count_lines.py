from pyspark import SparkContext, SparkConf

# Configuration de Spark
conf = SparkConf().setAppName("CountLines")
sc = SparkContext(conf=conf)

# Chargement du fichier HDFS
file_path = "hdfs:///user/hadoop/arbres.csv"
lines = sc.textFile(file_path)

# Comptage des lignes
line_count = lines.count()

print("Nombre de lignes dans le fichier : {}".format(line_count))

