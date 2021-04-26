# cheat-sheet
### most frequently used command for major platform

# Airflow
### commands to refresh DAG in Airflow
`$ python -c "from airflow.models import DagBag; d = DagBag();"`

# Docker

### Login to container as a root user
`$ docker exec -u 0 -it container_id /bin/bash`

# GitLab

### Login to GitLab
`docker login registry.gitlab.com`

```text
WARNING! Your password will be stored unencrypted in /home/amarkumar/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store
```

