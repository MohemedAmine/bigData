from pyspark import SparkContext

def safe_float(value):
    try:
        return float(value)
    except ValueError:
        return None  

sc = SparkContext("local", "Tallest Tree")
rdd = sc.textFile("hdfs:///user/hadoop/arbres.csv")
header = rdd.first()


tree_data = rdd.filter(lambda x: len(x.split(";")) == 13 and x != header)

pairs = tree_data.map(lambda x: (safe_float(x.split(";")[6]), x.split(";")[2]))


valid_pairs = pairs.filter(lambda x: x[0] is not None)


tallest = valid_pairs.sortByKey(ascending=False).first()

if tallest:
    print("Genre de l'arbre le plus haut : {} (Hauteur : {})".format(tallest[1], tallest[0]))
else:
    print("Aucun arbre valide trouvé.")
