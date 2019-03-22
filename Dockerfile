FROM python:3-alpine

WORKDIR /app
COPY requirements.txt .
RUN ["python", "-m", "pip", "install", "-r", "requirements.txt"]
COPY app .

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
