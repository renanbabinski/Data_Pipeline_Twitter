from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession\
        .builder\
        .appName("twitter_transformation")\
        .getOrCreate()
    
    df = spark.read.json(
        "/home/anonymous/Documents/datapipeline/datalake/twitter_aluraonline"
    )
    df.printSchema()
    df.show()
