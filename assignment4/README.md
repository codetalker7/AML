# Running tests

To run the tests, simply do

```shell
pytest
```

To generate the coverage report, do

```shell
pytest --cov > coverage.txt
```

# The Flask application

To run the flask app, do

```shell
python3 -m flask --app app run
```

By default the server runs at `http://localhost:5000`. An example POST request is given in the file `example_post.py`. To see it in action, simply do

```shell
python3 example_post.py
```

while the app is running.

# Building Docker image

To build the Docker image, run the following.

```bash
make build
```

To check the list of built images, you can do

```bash
docker images
```

To run the image, do

```bash
make run
```

To stop the container, do

```bash
docker stop aml-assignment
docker rm aml-assignment
```

To start fresh and remove everything, do

```bash
make clean
```
