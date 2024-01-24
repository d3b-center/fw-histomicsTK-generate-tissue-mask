# Uses the released HistomicsTK Docker image

FROM dsarchive/histomicstk:latest

ENV FLYWHEEL="/flywheel/v0"
WORKDIR ${FLYWHEEL}
COPY ./ $FLYWHEEL/

RUN chmod 777 .
ENTRYPOINT ["python","/flywheel/v0/run.py"]
