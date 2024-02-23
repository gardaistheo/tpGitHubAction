FROM python:3.10.10
WORKDIR /app
COPY SimpleMath.py .
RUN pip install pylint
COPY . .
CMD ["python", "-m", "unittest", "discover", "-s", ".", "-p", "test*.py"]
