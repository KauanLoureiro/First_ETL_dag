import sqlite3
from pathlib import Path
from airflow.configuration import conf

def loading(df):
    BASE_PATH = conf.get("core", "dags_folder")
    DB_PATH = Path(BASE_PATH).parent / "Data" / "Test.db"

    con = sqlite3.connect(DB_PATH)

    df.to_sql("Test_table",con=con, if_exists="replace")

    con.close()