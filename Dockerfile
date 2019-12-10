FROM python:3-alpine

RUN set -ex; \
  apk add --no-cache --no-progress tzdata \
  && \
  cp /usr/share/zoneinfo/Europe/London /etc/localtime \
  && \
  echo "Europe/London" > /etc/timezone \
  && \
  apk del tzdata \
  && \
  addgroup -g 1000 mtp \
  && \
  adduser -h /home/mtp -s /sbin/nologin -D -u 1000 -G mtp mtp

WORKDIR /app
COPY requirements.txt .
RUN mkdir /app/static
RUN python -m pip install -r requirements.txt
COPY app .
USER 1000

ENV APP_GIT_COMMIT ${APP_GIT_COMMIT}
ENV APP_GIT_BRANCH ${APP_GIT_BRANCH}
ENV APP_BUILD_TAG ${APP_BUILD_TAG}
ENV APP_BUILD_DATE ${APP_BUILD_DATE}

EXPOSE 8080
ENV FLASK_APP app.py
ENTRYPOINT ["flask", "run", "--host", "0.0.0.0", "--port", "8080"]
