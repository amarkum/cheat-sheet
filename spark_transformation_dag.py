from airflow.contrib.operators.spark_submit_operator import SparkSubmitOperator
from airflow.models import DAG
from airflow.utils.dates import days_ago

command = "{{dag_run.conf.get('command')}}"
input_file = "{{dag_run.conf.get('input')}}"
output_file = "{{dag_run.conf.get('output')}}"

args = {
    'owner': 'Amar Kumar',
    'start_date': days_ago(2),
}
dag_conf = DAG(dag_id="spark_transformation_dag", default_args=args, schedule_interval=None)

dedupe_config = {
    "application_args": [input_file, output_file]
}

dedupe_spark_job = SparkSubmitOperator(task_id="de-dupe-transformation",
                                       java_class="com.canusi.spark.core.DeDupeRecords",
                                       application="/airflow/spark-core.jar",
                                       conn_id="spark-local", dag=dag_conf, **dedupe_config)

if command == "dedupe":
    dedupe_spark_job

