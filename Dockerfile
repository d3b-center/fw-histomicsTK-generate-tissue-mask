# Uses the released HistomicsTK Docker image

FROM dsarchive/histomicstk:latest

ENV FLYWHEEL="/flywheel/v0"
WORKDIR ${FLYWHEEL}
# COPY ./ $FLYWHEEL/
COPY run.py manifest.json $FLYWHEEL/
COPY fw_gear_generate_tissue_mask ${FLYWHEEL}/fw_gear_generate_tissue_mask 

RUN chmod 777 .
ENTRYPOINT ["python","/flywheel/v0/run.py"]
