# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pyspark
from pyspark.ml.linalg import Vectors
from pyspark.sql import SparkSession
from pyspark.ml.linalg import Matrices
spark = SparkSession.builder.getOrCreate()

df = spark.sql('''select 'spark' as hello ''')
df.show()

#Trying something with linalg
v = Vectors.dense(2.0, 0.0, 3.0, 4.0, 5.0)
print(v.norm(2))

dm1 = Matrices.dense(2, 3, [1, 2, 3, 4, 5, 6])
dm2 = Matrices.dense(2, 3, [7, 8, 9, 10, 11, 12])