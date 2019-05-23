FROM python:3.6
MAINTAINER Ewnetu "ewnetu@cs.umu.se"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["firstattempt.py"]
