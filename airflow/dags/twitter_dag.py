from airflow.models import DAG
from os.path import join
from airflow.operators.alura import TwitterOperator
from datetime import date, datetime

with DAG(dag_id="twitter_dag", start_date=datetime.now()) as dag:
    twitter_operator = TwitterOperator(
        task_id="twitter_aluraonline",
        query="AluraOnline",
        file_path=join(
            "/home/anonymous/Documents/datapipeline/datalake",
            "twitter_aluraonline",
            "extract_date={{ ds }}",
            "AluraOnline_{{ ds_nodash }}.json"
        )
    )

