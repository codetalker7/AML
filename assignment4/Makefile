build:
	docker build --tag aml-assignment .

run:
	docker run -d -p 5000:5000 --name aml-assignment aml-assignment

clean:
	docker stop aml-assignment
	docker rm aml-assignment
	docker container prune
	docker image rm aml-assignment
