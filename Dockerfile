from python:3.12

WORKDIR:/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py ./
COPY regression.joblib ./
EXPOSE 5000

CMD["fastapi", "run", "app.py", "--port", "5000"]