from pyspark import SparkContext, SparkConf

# Configurer Spark pour utiliser le cluster
conf = SparkConf().setAppName("Count by Genus")  # Remplacez par l'URL de votre master Spark
sc = SparkContext(conf=conf)

# Charger les données avec une répartition adéquate (par exemple 8 partitions)
rdd = sc.textFile("hdfs:///user/hadoop/arbres.csv", 8)  # 8 partitions, ajustez en fonction de votre cluster

# Récupérer l'en-tête du fichier
header = rdd.first()

# Appliquer un filtre pour exclure l'en-tête et mapper les genres
genus = rdd.filter(lambda x: x != header).map(lambda x: (x.split(";")[2], 1))

# Optionnel : Répartition avant réduction pour optimiser la distribution
genus = genus.repartition(8)  # Répartir sur 8 partitions (ajustez selon la taille de votre cluster)

# Agrégation des genres
result = genus.reduceByKey(lambda a, b: a + b)

# Afficher les résultats
for genus, count in result.collect():
    print("{}: {}".format(genus, count))

# Arrêter le SparkContext pour libérer les ressources
sc.stop()
