install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
		
format:
	black *.py
	
lint:
	pylint --disable=R,C *.py
	
test:
	python -m pytest -vv --cov=calCli.py

# container-lint:
# 	docker run --rm -i hadolint/hadolint < Dockerfile
	
# deploy:
# 	aws ecr get-login-password --region ap-northeast-1 | docker login --username AWS --password-stdin 339713188295.dkr.ecr.ap-northeast-1.amazonaws.com
# 	docker build -t logistic .
# 	docker tag logistic:latest 339713188295.dkr.ecr.ap-northeast-1.amazonaws.com/logistic:latest
# 	docker push 339713188295.dkr.ecr.ap-northeast-1.amazonaws.com/logistic:latest
	
all: install lint test