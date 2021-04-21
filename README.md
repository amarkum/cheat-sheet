# dev-ops
Configuration files for DevOps

### commands to refresh DAG in Airflow
`$ python -c "from airflow.models import DagBag; d = DagBag();"`


### Login to container as a root user
`$ docker exec -u 0 -it container_id /bin/bash`
