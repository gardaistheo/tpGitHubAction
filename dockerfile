FROM python:3.10.10
WORKDIR /app
COPY SimpleMath.py .
RUN pip install pylint
CMD ["python", "-m", "unittest", "SimpleMath.py"]
