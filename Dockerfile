FROM python:3.11

# Create the user that will run the app
RUN adduser --disabled-password --gecos '' ml-api-user

WORKDIR /opt/model_api

# ARG PIP_EXTRA_INDEX_URL

# Install requirements, including from Gemfury
ADD ./model_api /opt/model_api/
ADD ./model_package /opt/model_package/
RUN pip install --upgrade pip
RUN pip install -r /opt/model_api/requirements/req.txt

RUN chmod +x /opt/model_api/run.sh
RUN chown -R ml-api-user:ml-api-user ./

USER ml-api-user

EXPOSE 8001

CMD ["bash", "./run.sh"]
