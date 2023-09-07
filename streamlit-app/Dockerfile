FROM python:slim-bullseye

ARG server_port=8000
ARG server_host="0.0.0.0"
ENV server_port=$server_port
ENV server_host=$server_host

WORKDIR /app

RUN python3 -m pip install --no-cache-dir streamlit pydantic pandas numpy python-dotenv

COPY . .

ENTRYPOINT streamlit run main.py --server.port=$server_port --server.address=$server_host