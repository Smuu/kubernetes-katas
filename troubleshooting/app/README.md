# Troubleshooting application

## Usage

Container has entrypoint `python -u` and cmd `app.py`.
You can override cmd on startup.

Container webservice listening on port `80`.

Application need up to 5 seconds to start.

Provide 3 replicas in the cluster.

Resources:
```yaml
resources:
    requests:
        memory: "128Mi"
        cpu: "150m"
    limits:
        memory: "128Mi"
        cpu: "150m"
```


## Version

| Tag    | Description                                    |
| ------ | ---------------------------------------------- |
| v0.0.1 | BROKEN. First release of application           |
| v0.0.2 | Fixed first release of application             |
| v1.0.0 | UPCOMING. Not yet available next major release |