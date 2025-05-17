FROM ubuntu:20.04

RUN apt-get update && apt-get install -y bash

COPY docker_script.sh /docker_script.sh
RUN chmod +x /docker_script.sh

CMD ["sleep", "60"]
