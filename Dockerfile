FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt /app

RUN python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt --no-cache-dir

COPY . .

RUN echo "BROWSERSTACK_USERNAME=${BROWSERSTACK_USERNAME}" >> .env && \
    echo "BROWSERSTACK_ACCESS_KEY=${BROWSERSTACK_ACCESS_KEY}" >> .env && \
    echo "LOGIN=${LOGIN}" >> .env && \
    echo "PASSWORD=${PASSWORD}" >> .env

RUN cat .env
CMD ["browserstack-sdk", "pytest", "--s", ".\test\test_start_page.py:TestStartPage:test_click_skip_onboarding" ]