from pyspark.ml import Pipeline
from sparknlp.annotator import *
from sparknlp.common import *
from sparknlp.base import *
import pandas as pd
from sparknlp.training import CoNLL
import pyspark.sql.functions as F
import nlu
from sklearn.metrics import classification_report

from pyspark.sql import SparkSession
spark = SparkSession.builder \
.appName("Spark NLP") \
.master("local[*]") \
.config("spark.driver.memory", "20G") \
.config("spark.serializer", "org.apache.spark.serializer.KryoSerializer") \
.config("spark.kryoserializer.buffer.max", "2000M") \
.config("spark.driver.maxResultSize", "20G") \
.config("spark.jars.packages", "com.johnsnowlabs.nlp:spark-nlp_2.11:2.6.2").getOrCreate()

with open("../Dataset/nerdata.txt", "r", encoding="utf-8") as file:
    text_ln = file.readlines()