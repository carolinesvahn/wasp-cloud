# -*- coding: utf-8 -*-
"""
Created on Fri May 24 11:29:23 2019

@author: tmgkn
"""
from pyspark.sql import SparkSession
from pyspark.ml.linalg import Vectors
from pyspark.ml.linalg import Matrices
import scipy as sc

def do_spark():
    #sparky = SparkSession.builder.getOrCreate()
    #df = sparky.sql('''select 'spark' as hello ''')
    
    v = Vectors.dense(2.0, 0.0, 3.0, 4.0, 5.0)
    
    dm1 = Matrices.dense(2, 3, [1, 2, 3, 4, 5, 6])
    dm2 = Matrices.dense(2, 3, [7, 8, 9, 10, 11, 12])
    
    #mat = sc.io.mmread('494_bus.mtx')
    
    return "{}".format(v.norm(2))

#print(do_spark())