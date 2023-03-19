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
docker build --tag aml-assignment .
```

To check the list of built images, you can do

```bash
docker images
```

To run the image, do

```bash
docker run -d -p 5000:5000 --name aml-assignment aml-assignment
```

To stop the container, do

```bash
docker stop aml-assignment
```
