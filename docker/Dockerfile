FROM python:3.12

WORKDIR /code

COPY ../ /code

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

CMD ["uvicorn", "azairnotifier.app:app", "--host", "0.0.0.0", "--port", "80", "--reload"]
