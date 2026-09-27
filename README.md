# First API

My first API: a minimal Flask server with two JSON endpoints.

## Endpoints

| Method | Path | Returns |
|---|---|---|
| GET | `/` | `{"status": "ok"}`, a simple health check |
| GET | `/api/hello` | A greeting plus the current UTC time in ISO 8601 |

## Run it

```bash
pip install flask
python server.py
```

The server starts on http://localhost:3000.

```bash
curl http://localhost:3000/api/hello
# {"message": "Hello, world!", "time": "2026-07-10T09:30:00.123456+00:00"}
```
