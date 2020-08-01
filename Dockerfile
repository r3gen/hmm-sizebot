FROM python:3
ADD sizebot.py /
RUN pip3 install discord
CMD [ "python3", "./sizebot.py" ]