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

#Set up loggin file with all the performance info we need
#1) You need to create /conf directory under $SPARK_HOME
#2) 
#from pyspark import SparkConf
#log4j = sc._jvm.org.apache.log4j
#conf = sc.getConf()
#app_id = conf.get('spark.app.id')
#app_name = conf.get('spark.app.name')
#message_prefix = '<' + app_name + ' ' + app_id + '>'
#logger = log4j.LogManager.getLogger(message_prefix)

sc.setLogLevel("INFO")


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


#Calculates the matrix M^TM
#M is an IndexedRowMatrix of size (m x n)
def do_spark_Gramian(M):  
    G = M.computeGramianMatrix()
    return "Gramian matrix calculation complete"
    

#Calculates the SVD decomposition of M
#M is an IndexedRowMatrix of size (m x n)
#k is the number of singular values 1 <= k <= m
#u is logical indicating if matrix U is returned   
def do_spark_SVD(M,k,u):
    svd = M.computeSVD(k,u)
    return "SVD decomposition complete"
    
#Calculates the cosine similarities between the columns of M
#M is an IndexedRowMatrix of size (m x n)
def do_spark_cosine_sim(M):
    cs = M.columnSimilarities()
    return "Column similarities calculated"


#Function for convert numpy matrix to Indexed Spark (Distributable Matrix)
def indexed_matrix_from_numpy(M):
    t = tuple(map(tuple, M))
    t2 = range(len(t))
    l = list(t)
    for i in t2:
        l[i]=tuple((i,l[i]))
    idxM = IndexedRowMatrix(sc.parallelize(l))    
    return idxM


#Testing the functions defined above
mat = IndexedRowMatrix(sc.parallelize([(0, (0, 1)), (1, (2, 3)), (2,(4,5))]))
do_spark_Gramian(mat)
do_spark_SVD(mat,2,"false")
do_spark_cosine_sim(mat)


#Bigger matrices
n = 1000
s1 = np.random.normal(0, 1, n*n)
M = np.reshape(s1,(n,n))
mat = indexed_matrix_from_numpy(M)
do_spark_Gramian(mat)
do_spark_SVD(mat,n,"false")
do_spark_cosine_sim(mat)

