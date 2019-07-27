#!/bin/bash

docker run -it --rm --name ml101_tf -p 6006:6006 -v $(pwd)/notebooks/:/workspace/notebooks ml101 tensorboard --logdir=/workspace/notebooks/movie_reviews/logs
