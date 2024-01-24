# Uses the released HistomicsTK Docker image

FROM dsarchive/histomicstk:latest

ENV FLYWHEEL="/flywheel/v0"
WORKDIR ${FLYWHEEL}
COPY run.py manifest.json $FLYWHEEL/
COPY fw_gear_generate_tissue_mask ${FLYWHEEL}/fw_gear_generate_tissue_mask 

RUN pip install flywheel_gear_toolkit
RUN pip install fw_core_client
RUN pip install flywheel-sdk


RUN chmod 777 .
ENTRYPOINT ["python","/flywheel/v0/run.py"]
