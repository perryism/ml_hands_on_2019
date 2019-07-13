#!/bin/bash

docker run -it --rm --name ml101 -p 8888:8888 -v $(pwd)/notebooks/:/workspace/notebooks ml101 
