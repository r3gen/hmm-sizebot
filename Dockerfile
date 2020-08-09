FROM python:3
ENV SIZEBOT_TOKEN "<replace_with_token>"
ADD sizebot.py /
RUN pip3 install discord
CMD [ "python3", "./sizebot.py" ]