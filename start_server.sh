#!/bin/bash

docker exec -it table_to_database_web_dev flask run --host=0.0.0.0 --debug
