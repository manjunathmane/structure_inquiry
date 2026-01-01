FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install pytest
CMD ["python", "app.py", "Alice", "Python", "4", "DevOps", "3"]