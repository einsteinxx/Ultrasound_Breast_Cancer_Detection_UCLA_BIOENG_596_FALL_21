# UCLA_BIOENG_596_FALL_21 & Winter 2022
Keane Gonzalez

Code and script for Ultrasound Cancer tumor detection using Faster R-CNN with a ResNet50 pre-trained backbone

-- Pre-Processing and Results scripts are also in this area.


Data:
1. BUSI ultrasound images for first fine-tuning (~700 images)
2. UCLA Ultrasound set for final classification & Region detection (~8800 images)


Environment:
  Jupyter Notebook in Google Colab (Pro for the extended training time and memory)
 
Code Flow:
1. Pre-Process
2. Data Ingestion
3. Load Faster-RCNN (Resnet50) weights
4. Train on BUSI
5. Load BUSI saved checkpoint with highest IOU results
6. Train with UCLA data
7. Save model with highest IOU value (after penalizing for false positives/negatives)
8. Results plots and verification
9. TBD
  
 Output Example Images with Predictions and Truth Regions:
 
 
![image](https://user-images.githubusercontent.com/27804848/157021672-02047753-a4fa-4568-a18a-a00a829afe0b.png)

![image](https://user-images.githubusercontent.com/27804848/157021810-e5c640ba-8816-40e3-9cc1-dc20166a5d90.png)


***
Currently being retrained/retested without ImageNet normalization
***
