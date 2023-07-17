FROM python:3.11-slim

RUN mkdir ./insurance_cost
COPY . ./insurance_cost
WORKDIR /insurance_cost/app
RUN python3 -m pip install -r ../requirements.txt
EXPOSE 8080

CMD ["python3", "main.py"]