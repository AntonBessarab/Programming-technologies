FROM alpine
RUN apk add --update python3 py3-pip
RUN python3 -m venv /venv
RUN /venv/bin/pip install flask
COPY . /app
WORKDIR /app
ENTRYPOINT ["/venv/bin/python"]
CMD ["app.py"]