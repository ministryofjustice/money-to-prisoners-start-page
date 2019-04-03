FROM python:3-alpine

RUN set -ex; \
  addgroup -S mtp && \
  adduser -D -S -h /app -s /sbin/nologin -G mtp mtp && \
  test $(id -u mtp) = 100

WORKDIR /app
COPY requirements.txt .
RUN python -m pip install -r requirements.txt
COPY app .
USER 100

ARG APP_GIT_COMMIT
ARG APP_GIT_BRANCH
ARG APP_BUILD_TAG
ARG APP_BUILD_DATE
ENV APP_GIT_COMMIT ${APP_GIT_COMMIT}
ENV APP_GIT_BRANCH ${APP_GIT_BRANCH}
ENV APP_BUILD_TAG ${APP_BUILD_TAG}
ENV APP_BUILD_DATE ${APP_BUILD_DATE}

ENV FLASK_APP app.py
ENTRYPOINT ["flask", "run", "--host", "0.0.0.0", "--port"]
CMD ["80"]
