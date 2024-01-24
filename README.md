# Flywheel gear that implements Histoqc

HistoQC is an open-source quality control tool for digital pathology slides.

## **Requirements**:


- openslide
- python-openslide
- matplotlib
- numpy
- scipy
- skimage
- sklearn

Tested with Python 3.7 and 3.8 Note: the DockerFile installs Python 3.8.


**Required inputs:**
Input image

**Optional inputs:**
Config file (.ini)

## **Local Gear Testing**
1. Clone repo to local machine
2. Copy a pathology file to the same directory (e.g., "HandE.svs")
3. Build the docker container
```
docker build -t chop.flywheel.io/histoqc:[version#] ./
```
4. Run gear locally
```
fw gear local --input_image HandE.svs
```

##  **Citation**
If you find this software useful, please drop me a line and/or consider citing it:

"HistoQC: An Open-Source Quality Control Tool for Digital Pathology Slides", Janowczyk A., Zuo R., Gilmore H., Feldman M., Madabhushi A., JCO Clinical Cancer Informatics, 2019

“Assessment of a computerized quantitative quality control tool for kidney whole slide image biopsies”, Chen Y., Zee J., Smith A., Jayapandian C., Hodgin J., Howell D., Palmer M., Thomas D., Cassol C., Farris A., Perkinson K., Madabhushi A., Barisoni L., Janowczyk A., Journal of Pathology, 2020

