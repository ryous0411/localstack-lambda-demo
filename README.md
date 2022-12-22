## localstack-lambda-demo
FastAPIで作成したAPIからLocalStack上のLambdaを呼び出すデモ

### 事前準備
Docker & Docker Compose
- https://www.docker.com/products/docker-desktop/

LocalStack
```shell
pip install localstack
```
make
```shell
brew install make
```

### インストール
```shell
poetry install
```

### Lambda作成
```shell
docker-compose up &
make
```
### API起動
```shell
python main.py
```

### 動作確認
```shell
curl http://127.0.0.1:8000
curl http://127.0.0.1:8000/hello/test
```