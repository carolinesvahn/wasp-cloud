# wasp-cloud :)

## Activate logging
1. Create the configuration directory in "C:\Users\Hector\Anaconda\Lib\site-packages\pyspark\conf" or similar
2. Add logging config file log4j.properties (I uploaded to github)
3. Edit the option log4j.appender.FILE.File=C:/temp/log.out so it works in your system

## Checking CPU times and memory usage
1. When we send tasks to Spark some cpu and memory info goes to the log
2. Usually is one single task that is divided in several stages
3. One call to a function (e.g. SVD) may take one or several stages
4. For CPU times: Open the log file and search for "Finished Task", and you will see results in ms
5. For memory usage: Open the log file and search for "memory", you should see info on memory usage per Block
6. As far as I know, both cpu times and memory usage for a task must be calculated by hand, i.e. aggregating all stages

