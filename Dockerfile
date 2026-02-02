FROM mcr.microsoft.com/playwright/python:v1.41.0-jammy

WORKDIR /app

COPY . .

RUN pip install pytest pytest-html

CMD ["pytest", "--html=report.html"]
