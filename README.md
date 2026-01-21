# Simple MCP Server

# Run the server application
uvicorn app.main:app --port 8000

# API Documentation
http://127.0.0.1:8000/docs


# Api Endpoint
http://127.0.0.1:8000/mcp


# Invoke Discovery Endpoint
```ps
Invoke-RestMethod -Uri "http://127.0.0.1:8000/mcp" `
    -Method Post `
    -ContentType "application/json" -Body '{"verb": "discovery"}'
```

# Invoke Tool 
```ps
Invoke-RestMethod  -Uri "http://127.0.0.1:8000/mcp" `
    -Method Post `
    -ContentType "application/json" `
    -Body '{"verb": "execute", "tool_name": "get_weather", "arguments": {"location": "dallas"}}'
```