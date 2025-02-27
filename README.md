1.
```
poetry run uvicorn main:app --host 0.0.0.0 --port 8080 --reload
```

2.
```
curl -X GET http://localhost:8080/default
curl -X GET http://localhost:8080/decimal
```
