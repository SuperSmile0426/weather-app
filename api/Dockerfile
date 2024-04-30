FROM python:3.12

#
WORKDIR /app


COPY requirements.txt ./

#
RUN --mount=type=cache,target=/root/.cache/pip pip3 install -r requirements.txt

#
COPY . .

#
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]