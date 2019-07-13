#!/bin/bash

set -e

function launch_browser() {
	until docker logs ml101 2>&1 | grep "The Jupyter Notebook is running at" ; do sleep 1; done

	open http://localhost:8888
}

launch_browser &
docker run -it --rm --name ml101 -p 8888:8888 -v $(pwd)/notebooks/:/workspace/notebooks ml101 
