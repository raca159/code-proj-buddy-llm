FROM huggingface/transformers-pytorch-gpu:4.29.2

ARG server_port=8000
ARG server_host="0.0.0.0"

ENV server_port=$server_port
ENV server_host=$server_host

WORKDIR /app

RUN python3 -m pip install --no-cache-dir fastapi pydantic pandas numpy uvicorn python-dotenv

COPY . .

ENTRYPOINT ["python3", "main.py"]