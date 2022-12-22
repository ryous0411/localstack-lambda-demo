import json

import boto3
import uvicorn
from fastapi import FastAPI

app = FastAPI()

client = boto3.client('lambda', endpoint_url="http://localhost:4566")


@app.get("/")
async def root():
    response = __get_from_lambda()
    payload = response.get("Payload").read()
    return json.loads(payload)


@app.get("/hello/{name}")
async def say_hello(name: str):
    payload = {
        "PathParameters": name
    }
    response = __get_from_lambda(payload)
    payload = response.get("Payload").read()
    return json.loads(payload)


def __get_from_lambda(payload={}):
    return client.invoke(
        FunctionName="hello-world-lambda",
        InvocationType="RequestResponse",
        LogType="Tail",
        Payload=json.dumps(payload)
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
