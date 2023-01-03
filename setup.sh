#!/bin/bash

pip install -r requirements.txt
export AIRFLOW_HOME=.

airflow db init

airflow users create \
--username admin \
--password 1234 \
--firstname chaejin \
--lastname jeong \
--role Admin \
--email joung6517@gmail.com

airflow webserver --port 8080
airflow scheduler
