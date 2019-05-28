# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


from spark import do_spark
from spark import do_spark_distributed
from flask import Flask
app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, World!"
@app.route("/spark")
def spark():
    return do_spark()
@app.route("/spark_dist")
def spark_dist():
    return do_spark_distributed()
	
if __name__ == "__main__":
    app.run(debug=True)


#Read one of the matrices
#mat = scipy.io.mmread('494_bus.mtx')
