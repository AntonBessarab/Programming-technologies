FROM alpine
RUN apk add --update python3 py-pip
COPY . /app
WORKDIR /app
ENTRYPOINT ["python"]
CMD ["main.py"]