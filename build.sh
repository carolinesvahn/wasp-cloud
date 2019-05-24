#!/bin/bash
# 
docker build -t gcr.io/matrix-master/firstattempt .
docker push gcr.io/matrix-master/firstattempt
kubectl run firstattempt --replicas=3 --image=gcr.io/matrix-master/firstattempt --port 5000
kubectl expose deployment firstattempt --type=LoadBalancer --name=my-service --port 80 --target-port 5000