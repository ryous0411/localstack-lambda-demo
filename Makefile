all:
	make create-zip
	make delete-lambda
	make create-lambda
	make delete-zip

create-zip:
	zip -g hello-world-lambda.zip lambda/hello_world.py

delete-lambda:
	aws lambda delete-function \
    --function-name=hello-world-lambda \
    --region ap-northeast-1 \
    --endpoint-url=http://localhost:4566

create-lambda:
	aws lambda create-function \
    --function-name=hello-world-lambda \
    --runtime=python3.9 \
    --role=DummyRole \
    --handler=lambda/hello_world.lambda_handler \
    --zip-file fileb://hello-world-lambda.zip \
	--region ap-northeast-1 \
    --endpoint-url=http://localhost:4566

delete-zip:
	rm hello-world-lambda.zip

