FROM python:3.11-slim 
# Install Java 
RUN apt-get update && \
    apt-get install -y default-jdk wget && \
    rm -rf /var/lib/apt/lists/*
# Set Java environment
ENV JAVA_HOME=/usr/lib/jvm/default-java
ENV PATH=$JAVA_HOME/bin:$PATH
# Install PySpark 
RUN pip install --no-cache-dir pyspark 
WORKDIR /app 
COPY . /app 
CMD ["python", "app.py"]