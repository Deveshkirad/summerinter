# Customer Data Processing Pipeline Using Apache Airflow

## Project Title

Customer Data Processing Pipeline Using Apache Airflow and Docker

---

# Project Objective

The objective of this project is to automate customer data processing using Apache Airflow.

The pipeline performs the following operations:

1. Extract customer data from a CSV file.
2. Validate customer records.
3. Process and load valid customer data.
4. Generate notification messages.
5. Execute all tasks automatically through Airflow DAG orchestration.

---

# Technologies Used

* Python
* Apache Airflow 3.0.2
* Docker
* Docker Compose
* Pandas
* NumPy
* OpenPyXL

---

# Project Structure

```text
airflow-basic/
│
├── dags/
│   └── customer_pipeline.py
│
├── data/
│   └── customer.csv
│
├── output/
│
├── Dockerfile
├── compose.yml
└── requirements.txt
```

---

# Software Requirements

Install the following software before running the project:

1. Docker Desktop
2. Git
3. VS Code (Optional)

Verify Docker installation:

```bash
docker --version
docker compose version
```

---

# Dockerfile

```dockerfile
FROM apache/airflow:3.0.2

COPY requirements.txt /

RUN pip install --no-cache-dir -r /requirements.txt
```

---

# requirements.txt

```text
pandas
numpy
openpyxl
```

---

# compose.yml

```yaml
services:
  airflow:
    build: .
    container_name: airflow

    ports:
      - "8080:8080"

    command: standalone

    environment:
      AIRFLOW__CORE__LOAD_EXAMPLES: "False"

    volumes:
      - ./dags:/opt/airflow/dags
      - ./data:/opt/airflow/data
      - ./output:/opt/airflow/output
```

---

# Input Dataset

File Location:

```text
data/customer.csv
```

Dataset:

```csv
id,name,email
1,John,john@gmail.com
2,Ram,
3,Shyam,shyam@gmail.com
4,,test@gmail.com
5,Amit,amit@gmail.com
```

---

# Step 1: Open Project Directory

Open Git Bash and move to project folder.

```bash
cd "D:/collage files/internship/airflow-basic"
```

Verify files:

```bash
ls
```

Expected folders:

```text
dags
data
output
Dockerfile
compose.yml
requirements.txt
```

---

# Step 2: Build Docker Image

Build Airflow image.

```bash
docker compose build
```

Wait for build completion.

---

# Step 3: Start Airflow

Run:

```bash
docker compose up -d
```

Verify container status:

```bash
docker ps
```

Expected:

```text
airflow
```

---

# Step 4: Verify Airflow is Running

Check logs:

```bash
docker logs airflow --tail 20
```

Verify DAG loading:

```bash
docker exec -it airflow airflow dags list
```

Expected:

```text
customer_pipeline
```

Check DAG import errors:

```bash
docker exec -it airflow airflow dags list-import-errors
```

Expected:

```text
No data found
```

---

# Step 5: Open Airflow UI

Open browser:

```text
http://localhost:8080
```

Default Credentials:

```text
Username: admin
Password: admin
```

Locate DAG:

```text
customer_pipeline
```

Turn on the DAG if it is paused.

---

# Step 6: Trigger Pipeline

Trigger DAG manually:

```bash
docker exec -it airflow airflow dags trigger customer_pipeline
```

Expected Output:

```text
state = queued
```

After a few seconds verify execution:

```bash
docker exec -it airflow airflow dags list-runs customer_pipeline
```

Expected:

```text
state = success
```

---

# Step 7: Verify Tasks

List all tasks:

```bash
docker exec -it airflow airflow tasks list customer_pipeline
```

Expected:

```text
extract_customers
validate_customers
load_database
send_notification
```

---

# Step 8: Test Individual Task

Test extraction task:

```bash
docker exec -it airflow airflow tasks test customer_pipeline extract_customers 2026-06-20
```

Expected Output:

```text
Customer data extracted
```

---

# Pipeline Workflow

## Task 1: Extract Customers

Function:

```python
extract_customers()
```

Purpose:

* Read customer.csv
* Convert records into Python dictionary format
* Store records using XCom

Output:

```text
List of customer records
```

---

## Task 2: Validate Customers

Function:

```python
validate_customers()
```

Validation Rules:

* ID should not be empty
* Name should not be empty
* Email should not be empty

Valid Records:

```text
John
Shyam
Amit
```

Output File:

```text
valid_customers.csv
```

---

## Task 3: Load Database

Function:

```python
load_database()
```

Operation:

* Read valid customers
* Add status column

Added Column:

```text
Loaded
```

Output File:

```text
processed_customers.csv
```

---

## Task 4: Send Notification

Function:

```python
send_notification()
```

Operation:

Generate notification messages for all processed customers.

Output File:

```text
notification.txt
```

Example:

```text
Message sent to John (john@gmail.com)
Message sent to Shyam (shyam@gmail.com)
Message sent to Amit (amit@gmail.com)
```

---

# Verify Generated Files

Enter container:

```bash
docker exec -it airflow bash
```

Check output folder:

```bash
ls -la /opt/airflow/output
```

Expected Files:

```text
valid_customers.csv
processed_customers.csv
notification.txt
```

View Files:

```bash
cat /opt/airflow/output/valid_customers.csv
```

```bash
cat /opt/airflow/output/processed_customers.csv
```

```bash
cat /opt/airflow/output/notification.txt
```

Exit:

```bash
exit
```

---

# Common Commands

## Stop Project

```bash
docker compose down
```

---

## Start Existing Project

```bash
docker compose up -d
```

---

## Restart Project

```bash
docker compose restart
```

---

## Rebuild Project

```bash
docker compose down

docker compose build

docker compose up -d
```

---

## View Logs

```bash
docker logs airflow
```

Last 100 lines:

```bash
docker logs airflow --tail 100
```

---

# Output Files Generated

1. valid_customers.csv

Contains only valid customer records.

2. processed_customers.csv

Contains validated records with status column.

3. notification.txt

Contains notification messages for processed customers.

---

# Conclusion

This project successfully demonstrates an ETL workflow using Apache Airflow. Customer data is extracted from a CSV file, validated, processed, and notification messages are generated. Docker is used to containerize the Airflow environment, making the project portable and easy to run on any system.
