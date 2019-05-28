# -*- coding: utf-8 -*-
"""
Created on Fri May 24 11:29:23 2019

@author: tmgkn
"""
from pyspark.sql import SparkSession
from pyspark.ml.linalg import Vectors
from pyspark.ml.linalg import Matrices
from pyspark.mllib.linalg import QRDecomposition
from pyspark.mllib.linalg.distributed import IndexedRowMatrix
from pyspark.mllib.linalg.distributed import DistributedMatrix


#Define Spark and SQL context
from pyspark import SparkContext
sc = SparkContext("local", "First App") #This runs in the "local" cluster
from pyspark.sql import SQLContext
from pyspark import sql
sqlContext = sql.SQLContext(sc)

from pyspark import SparkConf
logFile = "logFile.txt"

#import scipy as sc
import numpy as np

def do_spark():
    #sparky = SparkSession.builder.getOrCreate()
    #df = sparky.sql('''select 'spark' as hello ''')
    	
    v = Vectors.dense(2.0, 0.0, 3.0, 4.0, 5.0)
    
    #dm1 = Matrices.dense(2, 3, [1, 2, 3, 4, 5, 6])
    #dm2 = Matrices.dense(2, 3, [7, 8, 9, 10, 11, 12])
    
    #mat = sc.io.mmread('494_bus.mtx')
	
	#Something bigger with matrices
    n = 50
    s1 = np.random.normal(0, 1, n*n)
    s2 = np.random.normal(0, 1, n*n)
    dm3 = Matrices.dense(n,n,s1)
    dm4 = Matrices.dense(n,n,s2)
  
    dm3s = dm3.toSparse()
    dm4s = dm4.toSparse()    
    
    return "{}".format(v.norm(2))

#print(do_spark())

def do_spark_distributed():
    print "This is example for distributed Matrix operations"
    mat = IndexedRowMatrix(sc.parallelize([(0, (0, 1)), (1, (2, 3))]))
    G = mat.computeGramianMatrix()
    return "{}".format(G.numCols)






