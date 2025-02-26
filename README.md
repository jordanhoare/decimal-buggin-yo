1.
```
poetry run uvicorn main:app --host 0.0.0.0 --port 8080
```

2.
```
curl -X POST http://localhost:8080/ \
  -H "Content-Type: application/json" \
  -d '{"a": "asdasd", "b": "asdasdasd"}'
```
