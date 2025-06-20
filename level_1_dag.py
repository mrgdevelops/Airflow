from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

args = {
    'owner': 'packt-developer',
}

with DAG(
    dag_id='hello_world_airflow',
    default_args=args,
    schedule='0 5 * * *',
    start_date=days_ago(1),
) as dag:

    print_hello = BashOperator(
        task_id='print_hello',
        bash_command='echo Hello',
    )

    print_world = BashOperator(
        task_id='print_world',
        bash_command='echo World',
    )

    print_hello >> print_world

if __name__ == "__main__":
    dag.cli()

# This code defines a simple Airflow DAG that prints "Hello" and "World" using Bash commands.
# The DAG is scheduled to run daily at 5:00 AM, starting from one day ago.
# The tasks are defined using BashOperator, and the dependencies are set so that "print_hello" runs before "print_world".
# The DAG can be executed from the command line using `dag.cli()`.
# Note: The `dag.cli()` method allows you to run the DAG from the command line for testing purposes.
# Make sure to run this code in an environment where Airflow is properly set up.
# This code is a simple example of how to create a DAG in Apache Airflow.
# It demonstrates the basic structure of a DAG, including task definitions and dependencies.
