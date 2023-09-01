from sqlalchemy import create_engine, text

# Create an SQLite database in memory (you can change this to a file-based database)
engine = create_engine('sqlite:///:memory:')

# Define a sample table schema and create the table
create_table_query = """
CREATE TABLE employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    salary INTEGER
);
"""
engine.execute(create_table_query)

# Insert some sample data into the table
insert_data_query = """
INSERT INTO employees (first_name, last_name, salary)
VALUES
    ('John', 'Doe', 50000),
    ('Jane', 'Smith', 60000),
    ('Bob', 'Johnson', 55000),
    ('Alice', 'Williams', 62000);
"""
engine.execute(insert_data_query)

# SQL query to calculate the average salary
average_salary_query = "SELECT AVG(salary) FROM employees;"
result = engine.execute(text(average_salary_query))
average_salary = result.scalar()

print(f"Average Salary: ${average_salary:.2f}")

# SQL query to find employees with a salary greater than the average
above_average_query = "SELECT first_name, last_name FROM employees WHERE salary > :avg_salary;"
result = engine.execute(text(above_average_query), avg_salary=average_salary)
above_average_employees = result.fetchall()

print("Employees with above-average salaries:")
for employee in above_average_employees:
    print(f"{employee.first_name} {employee.last_name}")

# Cleanup: Close the database connection (not needed for SQLite in-memory database)
engine.dispose()
