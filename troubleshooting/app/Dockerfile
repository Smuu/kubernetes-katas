FROM python:3.9

WORKDIR /app

ARG VERSION

COPY $VERSION.py app.py

ENTRYPOINT [ "python", "-u" ]

CMD [ "/app/app.py" ]
