dag = DAG('dags_name', start_date=datetime(2023, 1, 1))  # define DAG, schedule
# operators; system integration part
first_task = DummyOperator(task_id='task_1')
second_task = DummyOperator(task_id='task_2')
third_task = DummyOperator(task_id='task_3')

task_1 >> task_2 >> task_3  # bishift operators / jobs (task depoendencies)
