[![PR's Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat)](http://makeapullrequest.com)  [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

# RealTime Sign Language Detection using Action Recognition

## Approach

Real-Time Sign Language is commonly predicted using models whose architecture consists of multiple CNN layers followed by multiple LSTM layers. However , the accuracy of these state of the art models is pretty low.
On the other hand, this approach , Mediapipe Holistic with LSTM Model gives a much better accuracy. This approach produced better results with very less amount of data . Since this model trained on fewer parameters, it trained much faster thus resulting in lesser computation time.

## Project

This project is divided into two parts:
1. Keypoints extraction using MediaPipe Holistic
2. LSTM Model trained on these keypoints to predict realtime sign language using video sequences.

## Dataset

Data is collected using MediaPipe Holistic for 3 actions :
* Hello
* Thanks 
* I Love You

30 frames have been collected for each action and 30 sequences for each frame have been collected from real time actions using `Computer Vision` and `MediaPipe Holistic`.
For each sequence , 1662 keypoints have been extracted.
* Face Landmarks - 468*3
* Pose Landmarks - 33*4
* Left Hand Landmarks - 21*3
* Right Hand Landmarks - 21*3

<p align="left">
<img width=40% src="Images/1.png"> &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;
<img width=40% src="Images/2.png"> &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp; 
</p>

The dataset can be accessed from the `Feature_Extraction` Folder.

## Model 

LSTM Model is trained using the extracted keypoints from the `Feature_Extraction` folder and later used for real time predictions.

<p align="left">
<img width=50% src="Images/3.jpg"> &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;
</p>

The Weights of the model are saved in the `lstm_model.h5` file.

## How to Use

* Clone the repository using :

        $ git clone https://github.com/rishusiva/Pose-Network
                
* Enter the directory using:

        $ cd Pose-Network/
      
* Install the requirements using:

        $ pip install -r requirements.txt

* To Predict Sign Languages in Real Time , run : 

        $ python3 test.py
        
## Results

* Our LSTM Model, after training for only 100 epochs, has an accuracy of *70%*
* It produced an accuracy score of *1.0* on a test set of 5 images.
* Our Trained LSTM Model is then used for real time testing. 

### Prediction Results:

<p align="left">
<img width=50% src="Images/4 (1).gif"> &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;
</p>

## Author
* Rishikesh Sivakumar

[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://GitHub.com/Naereen/) by [Rishikesh Sivakumar](https://www.linkedin.com/in/rishikesh-sivakumar-1a166a18b/)

## Contribution 

Contributions are always welcome! You can contribute to this project in the following way:
- [ ] Increasing the accuracy 
- [ ] Adding more signs 
- [ ] Bug fixes if any
- [ ] Creating an application

Do check out the <a href="https://github.com/rishusiva/Pose-Network/blob/main/Docs/Contribution.md">documentation</a> for Contribution Guidelines.
