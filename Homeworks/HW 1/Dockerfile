
FROM Aditya/ubuntu:16.04

COPY test-docker.sh /test-docker.sh
COPY cpu-tests.sh /cpu-tests.sh
COPY test-File-io.sh /test-File-io.sh
COPY test-Memory.sh /test-Memory.sh

RUN chmod +x test-docker.sh
RUN chmod +x cpu-tests.sh
RUN chmod +x test-File-io.sh
RUN chmod +x test-Memory.sh

ENTRYPOINT ["bash", "test-docker.sh"]
