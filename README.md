# First_ETL_dag
Mini projeto de engenharia de dados utilizando Apache Airflow (TaskFlow API) para orquestrar um pipeline ETL completo.

O projeto realiza:

Extract → Download de dataset via KaggleHub

Transform → Filtro de ferramentas com rating > 4.6 e API disponível

Load → Persistência dos dados em banco SQLite
