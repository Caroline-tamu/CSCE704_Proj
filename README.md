## Malware Detection and Attacker 
This repository contains two main sections:

**Defender**: A model for detecting malware using the MalwareImg method, which transforms malware samples into images, and then applies a Convolutional Neural Network (CNN) for classification.

**Attacker**: This section includes a collection of the attacker's samples, Python scripts, and techniques that I used to make the malware evade detection by bypassing the trained malware detection model. It also includes an analysis demonstrating that the malware behaves almost the same (over 90% similarity) after modification.

## Defender
This section contains the code and resources necessary for building and running a malware detection model using machine learning. The model is trained to classify and detect various malware types based on their features.

`data_preprocessing`: Transforms PE malware files into grayscale images for future training.

`model_training`: Contains the training process, and the model's performance is evaluated on a test set to determine its accuracy, precision, and recall.

`model_layer`: The architecture of the model.

`model`: The trained model.

## Attacker

`Report`: Uses CAPE Sandbox, VirusTotal Jujubox, and ChatGPT to analyze the similarity of the data based on IP addresses, files opened, and registry keys.

`sample`: The malware sample set after applying modifications.

`script`: The script used to append benign (goodware) strings into malware in order to bypass detection by the trained model.


## Dataset
The dataset used for this project is sourced from the [PE Malware Machine Learning Dataset](https://practicalsecurityanalytics.com/pe-malware-machine-learning-dataset/) provided by Practical Security Analytics. This dataset contains:

1. A variety of malware samples in PE (Portable Executable) format.
2. Benign samples to contrast and train the model for classification.


