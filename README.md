# Big Data Labs Repository

## Overview

This repository provides a comprehensive collection of laboratory exercises designed to develop expertise in modern big data technologies and distributed systems. The curriculum progresses through fundamental data processing concepts to advanced orchestration and integrated data engineering architectures.

**Repository**: `bigData` | **Owner**: MohemedAmine | **Current Branch**: master

## Table of Contents

- [Lab Overview](#lab-overview)
- [System Architecture](#system-architecture)
- [Prerequisites & Installation](#prerequisites--installation)
- [Lab Descriptions](#lab-descriptions)
- [Running Instructions](#running-instructions)
- [Technology Stack](#technology-stack)
- [Configuration Guide](#configuration-guide)
- [Troubleshooting & Diagnostics](#troubleshooting--diagnostics)
- [Learning Path & Best Practices](#learning-path--best-practices)
- [Resources & References](#resources--references)

---

## Lab Overview

### Lab2: Distributed Data Analysis with Apache Spark RDD

**Objective**: Master fundamental RDD operations and distributed data processing patterns

**Description**: Analysis of tree demographic data using Apache Spark's Resilient Distributed Dataset API. This lab establishes core competencies in working with unstructured data and transformation pipelines.

**Deliverables**:

- `count_lines.py` - Dataset size metrics
- `count_by_genus.py` - Categorical aggregation
- `average_height.py` - Statistical computation
- `tallest_tree.py` - Extreme value identification
- `arbres.csv` - Input dataset (13 fields, tree taxonomy and measurements)

**Core Competencies**: RDD transformations, map/reduce operations, data cleaning, error handling

**Technology Stack**: Apache Spark 2.4+, Python 3.7+

---

### Lab3: SQL-based Analytics with Spark DataFrames

**Objective**: Develop advanced data querying and analytical skills using structured APIs

**Description**: N-gram frequency analysis leveraging Google Books dataset. Demonstrates transition from RDDs to DataFrames and structured SQL queries for complex analytical tasks.

**Deliverables**:

- `lab.py` - Production-grade analysis script with SQL and DataFrame APIs
- `lab.ipynb` - Interactive analysis with visualizations
- `ngram.csv` - Historical n-gram frequency data (5 columns: ngram, year, count, pages, books)

**Core Competencies**:

- Spark SQL query optimization
- Window functions and ranking operations
- DataFrame to SQL view conversion
- Data filtering and aggregation patterns

**Technology Stack**: Apache Spark SQL, Jupyter Notebook, Python 3.7+

---

### Lab4: Machine Learning Pipeline Development

**Objective**: Build production-ready machine learning workflows using distributed computing

**Description**: Predictive modeling on automotive dataset. Covers feature engineering, model training, and evaluation within Spark ML framework.

**Deliverables**:

- `tp5_BigData.ipynb` - End-to-end ML pipeline implementation
- `Data/cars_train_data.csv` - Labeled training dataset
- `Data/cars_train/` - Preprocessed dataset format

**Core Competencies**:

- Feature engineering and transformation
- ML pipeline construction
- Model training and hyperparameter tuning
- Distributed model evaluation

**Technology Stack**: Apache Spark MLlib, Jupyter Notebook, Python 3.7+

---

### Lab5: Real-world Data Processing & Exploration

**Objective**: Apply data engineering practices to production-like datasets

**Description**: Analysis of transit systems data including station information and trip records. Emphasizes data quality assessment and exploratory data analysis.

**Deliverables**:

- `lab6.ipynb` - Data exploration and transformation notebook
- `station_data.csv` - Transit infrastructure metadata
- `trip_data.csv` - Transaction records

**Core Competencies**:

- Data quality assessment
- Exploratory data analysis
- Schema inference and handling
- Data type conversions

**Technology Stack**: Apache Spark, Pandas, Jupyter Notebook, Python 3.7+

---

### Lab6: Container Orchestration Fundamentals

**Objective**: Establish containerization practices for big data infrastructure

**Description**: Docker Compose configuration for local big data environment deployment. Foundational infrastructure-as-code approach.

**Deliverables**:

- `docker-compose.yml` - Multi-container orchestration definition

**Core Competencies**:

- Container definitions and configurations
- Service networking
- Volume management
- Environment variable management

**Technology Stack**: Docker 20.10+, Docker Compose 1.29+

---

### Lab8: Workflow Orchestration - Apache Airflow

**Objective**: Master workflow orchestration and data pipeline scheduling at scale

**Description**: Production-grade DAG implementation for rocket launch data ingestion and processing pipeline. Demonstrates dependency management, error handling, and automated retry logic.

**Deliverables**:

- `tp8.py` - Primary DAG definition
- `dags/tp8.py` - DAG package entry point
- Comprehensive execution logs with task-level debugging information

**Pipeline Stages**:

1. **Acquisition**: HTTP API integration with fallback mechanisms
2. **Enhancement**: Image data retrieval and correlation
3. **Notification**: Event-driven alerting system
4. **Scheduling**: Cron-based automation with retry policies (3 retries, 5-min intervals)

**Core Competencies**:

- DAG design and dependency management
- Task operators (Bash, Python, HTTP)
- Error handling and recovery strategies
- Monitoring and logging

**Technology Stack**: Apache Airflow 2.0+, Python 3.7+

---

### Lab9: Integrated Enterprise Data Architecture

**Objective**: Implement a complete data engineering ecosystem with multiple service tiers

**Description**: Production-grade integration of Airflow, NiFi, MinIO, and PostgreSQL. Demonstrates enterprise-level data platform architecture with multiple ingestion, storage, and processing components.

**Architectural Components**:

1. **Orchestration Layer**: Apache Airflow

   - DAG definitions for multi-system integration
   - Postgres connectivity and operations
   - Object storage workflows
   - Data ingestion processes

2. **Data Integration**: Apache NiFi

   - Flow definition management
   - Processor configurations
   - Credential management
   - JDBC database connectivity

3. **Object Storage**: MinIO (S3-compatible)

   - Distributed data lake
   - File lifecycle management
   - Bucket organization

4. **Relational Database**: PostgreSQL
   - Structured data persistence
   - Transactional integrity
   - Connection pooling

**DAG Implementations**:

- `hello_postgres.py` - Database connectivity validation
- `minio_dags.py` - Object storage operations (upload, retrieval)
- `nifi_dags.py` - NiFi processor orchestration

**Core Competencies**:

- Multi-service architecture design
- Cross-service communication
- Credential and configuration management
- Production logging and monitoring

**Technology Stack**: Apache Airflow 2.0+, Apache NiFi 1.13+, MinIO, PostgreSQL 12+, Docker Compose 1.29+

---

### Hadoop MapReduce: Classical Big Data Computing

**Objective**: Understand foundational distributed computing paradigms

**Description**: Implementation of word frequency analysis using Hadoop MapReduce framework. Covers classical map-shuffle-reduce pattern fundamental to big data processing.

**Deliverables**:

- Mapper implementations (4 variants)
- Reducer implementations (4 variants)
- `tp1.ipynb` - Theory, design patterns, and implementation guide

**Implementation Details**:

- `mapper.py` - Baseline word tokenization
- `reducer.py` - Aggregation logic
- Variants explore optimization strategies

**Core Competencies**:

- MapReduce programming model
- Key-value pair manipulation
- Data partitioning strategies
- Job configuration and submission

**Technology Stack**: Apache Hadoop 3.2+, Python 3.7+

---

## System Architecture

The curriculum is structured as a progression from foundational distributed computing to enterprise-level data engineering:

```
┌─────────────────────────────────────────────────────────────┐
│               ENTERPRISE ARCHITECTURE (Lab9)                │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │ Airflow  │  │   NiFi   │  │  MinIO   │  │ PostSQL  │   │
│  │ Workflow │  │ Ingestion│  │ Storage  │  │ Database │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │
└─────────────────────────────────────────────────────────────┘
                           ▲
                           │
┌─────────────────────────────────────────────────────────────┐
│             ORCHESTRATION LAYER (Lab8)                      │
│  ┌──────────────────────────────────────────────────────┐  │
│  │         Apache Airflow DAG Execution Engine          │  │
│  │  ├─ Task Scheduling  ├─ Monitoring  ├─ Logging      │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                           ▲
                           │
┌─────────────────────────────────────────────────────────────┐
│             PROCESSING LAYER (Lab2-5)                       │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │ Spark RDD    │  │ Spark SQL    │  │ Spark MLlib  │     │
│  │ (Lab2)       │  │ (Lab3, Lab4) │  │ (Lab4)       │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
└─────────────────────────────────────────────────────────────┘
                           ▲
                           │
┌─────────────────────────────────────────────────────────────┐
│             STORAGE LAYER                                   │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │     HDFS     │  │ Local FS     │  │   S3 (MinIO) │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
└─────────────────────────────────────────────────────────────┘
```

---

## Prerequisites & Installation

### System Requirements

| Component      | Minimum Version | Recommended | Notes                                        |
| -------------- | --------------- | ----------- | -------------------------------------------- |
| Python         | 3.7             | 3.9+        | Conda recommended for environment management |
| Java           | 8               | 11          | Required for Spark and Hadoop                |
| Docker         | 19.0            | 20.10+      | For Labs 6, 8, 9                             |
| Docker Compose | 1.25            | 1.29+       | Multi-container orchestration                |
| Memory         | 4GB             | 16GB+       | For comfortable local development            |
| Disk Space     | 20GB            | 50GB+       | For datasets and containers                  |

### Installation Steps

1. **Clone the repository:**

```bash
git clone https://github.com/MohemedAmine/bigData.git
cd bigData
```

2. **Create Python virtual environment:**

```bash
python -m venv venv

# Activate virtual environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

3. **Install Python dependencies:**

```bash
pip install --upgrade pip setuptools wheel
pip install pyspark pandas numpy jupyter jupyterlab matplotlib scikit-learn
```

4. **Set up environment variables:**

```bash
# Linux/Mac (.bashrc or .zshrc)
export JAVA_HOME=/path/to/java
export SPARK_HOME=/path/to/spark
export HADOOP_HOME=/path/to/hadoop
export PATH=$JAVA_HOME/bin:$SPARK_HOME/bin:$HADOOP_HOME/bin:$PATH

# Windows (PowerShell or Command Prompt)
set JAVA_HOME=C:\path\to\java
set SPARK_HOME=C:\path\to\spark
set HADOOP_HOME=C:\path\to\hadoop
```

5. **For Docker-based labs (optional but recommended):**

```bash
# Ensure Docker daemon is running, then:
docker --version
docker-compose --version
```

---

## Running Instructions

### Lab2: Distributed Data Analysis

```bash
cd Lab2

# Run individual analyses
spark-submit count_lines.py
spark-submit count_by_genus.py
spark-submit average_height.py
spark-submit tallest_tree.py

# Expected outputs: console statistics and metrics
```

### Lab3: SQL-based Analytics

```bash
cd Lab3

# Interactive notebook (recommended)
jupyter lab lab.ipynb

# Or execute script directly
spark-submit lab.py

# Outputs include aggregations, rankings, and visualizations
```

### Lab4: Machine Learning Pipeline

```bash
cd Lab4

# Open notebook environment
jupyter lab tp5_BigData.ipynb

# Execute cells in sequence
# Outputs: model performance metrics and visualizations
```

### Lab5: Real-world Data Processing

```bash
cd Lab5

# Launch notebook
jupyter lab lab6.ipynb

# Execute exploratory analyses
# Generates data quality reports and transformations
```

### Lab8: Apache Airflow Orchestration

```bash
cd lab8

# Initialize and start Airflow
docker-compose up -d

# Monitor execution
docker-compose logs -f airflow-webserver

# Access UI: http://localhost:8080
# Default credentials: admin/airflow

# Trigger DAG execution via UI or CLI:
docker-compose exec airflow-webserver airflow dags trigger rocket_launches

# View task logs
docker-compose exec airflow-webserver airflow tasks logs rocket_launches download_launches [EXECUTION_DATE]
```

### Lab9: Integrated Enterprise Architecture

```bash
cd lab9

# Start all services
docker-compose up -d

# Verify service health
docker-compose ps

# Access services:
# - Airflow UI: http://localhost:8080
# - MinIO UI: http://localhost:9001 (credentials: minioadmin/minioadmin)
# - NiFi UI: http://localhost:8161/nifi
# - PostgreSQL: localhost:5432

# Monitor logs
docker-compose logs -f [service_name]

# Execute specific DAGs
docker-compose exec airflow-webserver airflow dags trigger hello_postgres
docker-compose exec airflow-webserver airflow dags trigger minio_dags
docker-compose exec airflow-webserver airflow dags trigger nifi_dags
```

### MapReduce Implementation

```bash
cd My_first_hadoop_job

# Review theory and examples
jupyter lab tp1.ipynb

# Submit MapReduce job
hadoop jar $HADOOP_HOME/share/hadoop/tools/hadoop-streaming-*.jar \
  -input <input_path> \
  -output <output_path> \
  -mapper mapper.py \
  -reducer reducer.py
```

---

## Technology Stack

### Data Processing & Analytics Tier

| Technology       | Version    | Labs                   | Purpose                               |
| ---------------- | ---------- | ---------------------- | ------------------------------------- |
| Apache Spark     | 2.4+ / 3.x | Lab2, Lab3, Lab4, Lab5 | Distributed batch processing engine   |
| Spark Core       | -          | Lab2                   | RDD API for low-level transformations |
| Spark SQL        | -          | Lab3, Lab4             | Structured API for SQL queries        |
| Spark MLlib      | -          | Lab4                   | Distributed machine learning library  |
| Hadoop MapReduce | 3.2+       | My_first_hadoop_job    | Classical distributed computing       |

### Analysis & Visualization

| Technology       | Purpose                             | Labs                                  |
| ---------------- | ----------------------------------- | ------------------------------------- |
| Jupyter Notebook | Interactive computational notebooks | Lab3, Lab4, Lab5, My_first_hadoop_job |
| Pandas           | DataFrames and data manipulation    | Lab5                                  |
| NumPy            | Numerical and scientific computing  | Lab4, Lab5                            |
| Matplotlib       | Data visualization library          | Lab3, Lab4, Lab5                      |

### Orchestration & Integration (Enterprise Layer)

| Technology     | Version | Purpose                               | Labs       |
| -------------- | ------- | ------------------------------------- | ---------- |
| Apache Airflow | 2.0+    | Workflow orchestration and scheduling | Lab8, Lab9 |
| Apache NiFi    | 1.13+   | Data routing and transformation       | Lab9       |
| MinIO          | Latest  | S3-compatible object storage          | Lab9       |
| PostgreSQL     | 12+     | Relational database backend           | Lab9       |

### Infrastructure & Container Management

| Technology     | Version | Purpose                       | Labs                   |
| -------------- | ------- | ----------------------------- | ---------------------- |
| Docker         | 20.10+  | Container runtime environment | Lab6, Lab8, Lab9       |
| Docker Compose | 1.29+   | Multi-container orchestration | Lab6, Lab8, Lab9       |
| HDFS           | 3.2+    | Distributed filesystem        | Lab2, Lab3, Lab4, Lab5 |

---

## Configuration Guide

### Apache Spark Configuration

**Local Development Mode**

```python
from pyspark import SparkContext
from pyspark.sql import SparkSession

# RDD-based processing (Lab2)
sc = SparkContext("local[*]", "ApplicationName")

# SQL-based processing (Lab3, Lab4)
spark = SparkSession.builder \
    .appName("ApplicationName") \
    .master("local[*]") \
    .getOrCreate()
```

**Cluster Deployment (YARN)**

```python
spark = SparkSession.builder \
    .appName("ApplicationName") \
    .master("yarn") \
    .config("spark.executor.memory", "4g") \
    .config("spark.driver.memory", "2g") \
    .config("spark.executor.cores", "4") \
    .config("spark.sql.shuffle.partitions", "200") \
    .getOrCreate()
```

**Performance Tuning**

```python
# Optimize for large datasets
spark.conf.set("spark.sql.adaptive.enabled", "true")
spark.conf.set("spark.sql.adaptive.skewJoin.enabled", "true")
spark.conf.set("spark.serializer", "org.apache.spark.serializer.KryoSerializer")
```

### HDFS Data Access Patterns

```python
# Read from HDFS
rdd = sc.textFile("hdfs:///user/hadoop/data.csv")
df = spark.read.csv("hdfs:///user/hadoop/data.csv", header=True)

# Write to HDFS
rdd.saveAsTextFile("hdfs:///user/hadoop/output")
df.write.csv("hdfs:///user/hadoop/output", header=True)

# Configure HDFS connection
spark.conf.set("fs.defaultFS", "hdfs://namenode:8020")
```

### Apache Airflow Configuration (Lab8/Lab9)

**Core Settings**

```bash
AIRFLOW_HOME=/opt/airflow
AIRFLOW__CORE__DAGS_FOLDER=/opt/airflow/dags
AIRFLOW__CORE__LOAD_EXAMPLES=False
AIRFLOW__CORE__EXECUTOR=LocalExecutor
AIRFLOW__CORE__SQL_ALCHEMY_CONN=postgresql://user:password@postgres:5432/airflow
AIRFLOW__CORE__FERNET_KEY=$(python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())")
```

**Connection Management**

- PostgreSQL: `postgresql://airflow:airflow@postgres:5432/airflow`
- MinIO: Configure as S3 with custom endpoint `http://minio:9000`
- HTTP: For external API calls with authentication

**DAG Configuration Best Practices**

```python
from airflow import DAG
from datetime import datetime, timedelta

default_args = {
    'owner': 'data-engineer',
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2025, 1, 1),
    'email_on_failure': True,
    'email': ['admin@example.com']
}

dag = DAG('my_dag', default_args=default_args, schedule_interval='@daily')
```

### Container Networking (Lab9)

```yaml
version: '3.8'
services:
  airflow:
    container_name: airflow
    networks:
      - big-data-net
  postgres:
    container_name: postgres
    networks:
      - big-data-net
  minio:
    container_name: minio
    networks:
      - big-data-net
  nifi:
    container_name: nifi
    networks:
      - big-data-net

networks:
  big-data-net:
    driver: bridge
    ipam:
      config:
        - subnet: 172.25.0.0/16
```

---

## Troubleshooting & Diagnostics

### Common Issues & Solutions

#### Apache Spark Issues

**Issue**: `JAVA_HOME not set or invalid`

```bash
# Verify Java installation
java -version

# Set JAVA_HOME
export JAVA_HOME=$(dirname $(dirname $(readlink -f $(which java))))
echo $JAVA_HOME  # Verify output
```

**Issue**: `ERROR SparkContext: Error initializing SparkContext`

```bash
# Check Hadoop configuration
export HADOOP_HOME=/opt/hadoop
export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
export LD_LIBRARY_PATH=$HADOOP_HOME/lib/native:$LD_LIBRARY_PATH

# Verify namenode connectivity
hdfs dfs -ls /
```

**Issue**: `Out of memory or Executor failures`

```bash
# Increase Spark memory allocation
spark-submit --driver-memory 4g \
             --executor-memory 4g \
             --executor-cores 4 \
             script.py

# Or configure in SparkSession
spark = SparkSession.builder \
    .config("spark.driver.memory", "4g") \
    .config("spark.executor.memory", "4g") \
    .getOrCreate()
```

#### Docker Issues

**Issue**: `Port 8080 already in use`

```bash
# Find process using port
lsof -i :8080  # On Mac/Linux
netstat -ano | findstr :8080  # On Windows

# Modify docker-compose.yml ports or stop conflicting containers
docker-compose down
docker ps  # Verify all stopped
```

**Issue**: `Service fails to start with no logs`

```bash
# Check detailed logs
docker-compose logs [service_name] --tail 100

# Verify image pulled successfully
docker images | grep [service_name]

# Rebuild if necessary
docker-compose build --no-cache [service_name]
```

**Issue**: `Container cannot reach other containers`

```bash
# Verify network
docker network ls
docker network inspect [network_name]

# Test connectivity
docker exec [container1] ping [container2]
```

#### HDFS Issues

**Issue**: `Connection refused to namenode`

```bash
# Verify namenode status
jps  # Check for NameNode process

# Restart HDFS
start-dfs.sh
hdfs dfs -ls /  # Verify connectivity
```

**Issue**: `Permission denied on file operations`

```bash
# Check HDFS permissions
hdfs dfs -ls -la /user/hadoop/

# Modify permissions
hdfs dfs -chmod 755 /user/hadoop/data
hdfs dfs -chown -R hadoop:hadoop /user/hadoop/
```

**Issue**: `HDFS datanode errors`

```bash
# Check namenode logs
tail -100f $HADOOP_HOME/logs/hadoop-*-namenode-*.log

# Check datanode logs
tail -100f $HADOOP_HOME/logs/hadoop-*-datanode-*.log
```

#### Jupyter Notebook Issues

**Issue**: `ModuleNotFoundError: No module named 'pyspark'`

```bash
# Install in notebook Python environment
pip install pyspark

# Or specify kernel path in notebook
import sys
print(sys.executable)  # Verify correct Python
```

**Issue**: `Kernel not available or kernel crashes`

```bash
# List available kernels
jupyter kernelspec list

# Restart kernel
# Use Jupyter UI: Kernel → Restart Kernel

# Or from command line
jupyter kernelspec uninstall python3 --yes
python -m ipykernel install --user
```

---

## Learning Path & Best Practices

### Recommended Progression

1. **Foundation** (Lab2)

   - Understand RDD operations
   - Learn map-reduce patterns
   - Practice data cleaning

2. **Intermediate** (Lab3, Lab4)

   - Transition to DataFrames
   - Master SQL operations
   - Explore ML pipelines

3. **Advanced** (Lab5)

   - Apply to real datasets
   - Optimize performance
   - Handle edge cases

4. **Production** (Lab8, Lab9)
   - Implement orchestration
   - Design systems architecture
   - Deploy at scale

### Development Best Practices

**Code Quality**

- Follow PEP 8 style guidelines
- Use type hints for clarity
- Document complex logic
- Include error handling

**Data Processing**

- Validate input data quality
- Handle missing values appropriately
- Log transformation steps
- Test edge cases

**Performance Optimization**

- Profile code before optimizing
- Monitor memory and CPU usage
- Use appropriate data formats (Parquet vs CSV)
- Partition data strategically

**Monitoring & Logging**

- Use structured logging
- Track execution metrics
- Preserve audit trails
- Alert on anomalies

---

## Resources & References

### Official Documentation

- **Apache Spark**: https://spark.apache.org/docs/latest/
- **Hadoop**: https://hadoop.apache.org/docs/
- **Apache Airflow**: https://airflow.apache.org/docs/
- **Apache NiFi**: https://nifi.apache.org/docs.html
- **MinIO**: https://docs.min.io/
- **PostgreSQL**: https://www.postgresql.org/docs/

### Learning Materials

- Spark RDD Programming Guide
- Spark SQL, DataFrame and Dataset Guide
- Spark MLlib Guide
- Airflow Architecture and Best Practices

### Community & Support

- Stack Overflow: `[apache-spark]` `[airflow]` `[hadoop]`
- GitHub: Official repositories and discussions
- Mailing Lists: Apache project communities

---

## Project Metadata & Information

| Attribute          | Value                      |
| ------------------ | -------------------------- |
| Repository Name    | bigData                    |
| Repository Owner   | MohemedAmine               |
| Current Branch     | master                     |
| Educational Level  | Intermediate to Advanced   |
| Primary Language   | Python 3.7+                |
| License            | Educational Use            |
| Total Labs         | 8 (+ MapReduce)            |
| Estimated Duration | 40+ hours                  |
| Last Updated       | November 15, 2025          |
| Curriculum Version | 2.0 - Professional Edition |

---

## Final Notes

### Data & Ethics

- All datasets are anonymized or publicly available
- Comply with data privacy regulations
- Document data sources and lineage
- Apply ethical principles to analysis

### Contributing & Feedback

- Report issues with detailed context
- Include relevant logs and configurations
- Test changes before contributing
- Follow code review process

### Maintenance

- Keep dependencies updated
- Monitor for security patches
- Test with new Spark/Hadoop versions
- Update documentation regularly

---

**Contact & Support**: For issues or questions, consult official documentation or community forums

**Repository**: [https://github.com/MohemedAmine/bigData](https://github.com/MohemedAmine/bigData)

**Last Updated**: November 15, 2025 | **Curriculum Version**: 2.0 - Professional Edition
