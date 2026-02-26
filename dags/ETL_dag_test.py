from airflow.sdk import dag, task
import pandas as pd
from ETL_process.Extract import extraction
from ETL_process.Transform import transformation
from ETL_process.Load import loading

@dag(
        dag_id="ETL_dag_test",
)
def ETL_dag():

    @task.python
    def extract():
        df = extraction()
        return df

    @task.python
    def transform(data:pd.DataFrame):
        df = transformation(data)
        return df

    @task.python
    def load(data:pd.DataFrame):
        loading(data)
        
    first = extract()
    second = transform(first)
    third = load(second)

    first >> second >> third

ETL_dag()