To run job1(load data into json) on port 8081 you need run next command: ```uvicorn api.main:job1 --reload --port 8081```


To run job2(transform data into avro) on port 8082 you need run next command: ```uvicorn api.main:job2 --reload --port 8082```