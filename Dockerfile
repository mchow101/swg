FROM python:3.9

COPY requirements.txt ./

EXPOSE 8501
# RUN apk --update add python py-pip openssl ca-certificates py-openssl wget bash linux-headers
# RUN apk --update add --virtual build-dependencies libffi-dev openssl-dev python-dev py-pip build-base \
#   && pip install --upgrade pip \
#   && pip install --upgrade pipenv\
#   && pipenv install --upgrade
#   && apk del build-dependencies

RUN pip install -r requirements.txt
COPY . .

# ENTRYPOINT [ "python" ]

# CMD [ "hello.py" ]
CMD ["streamlit run app.py --server.port 8080"]