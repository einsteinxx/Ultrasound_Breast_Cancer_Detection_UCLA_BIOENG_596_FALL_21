# UCLA_BIOENG_596_FALL_21/Winter 2022/Spring2022
# Ultrasound Breast Cancer Detection
Keane Gonzalez

Code and script for Ultrasound Cancer tumor detection using Faster R-CNN with a ResNet50 pre-trained backbone

-- Pre-Processing and Results scripts are also in this area.


Data:
1. BUSI ultrasound images for first fine-tuning (~700 images)
    https://scholar.cu.edu.eg/?q=afahmy/pages/dataset
3. UCLA Ultrasound set for final classification & Region detection (~8800 images)


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

***
NOTES:
1. The Ultrasound system (Phillips) burns the workspace information onto the images (or the US image is embedded into the workspace and saved). Cropping removes the breast map, but some of the scale markers (right side slider-type) and orientation text may remain in the final image.
2. BUSI training can complete within a normal Google Colab sequence (8-12 hours). Fine-tuning with the larger UCLA dataset requires saving checkpoints and restarting. The initial restarts have loss that bounces at the start each time, but quickly get back to the loss/IOU of the previous checkpoint (might still be some tweaks/fixes to be made to loading from checkpoints).
3. GradCam on Colab has some issues with the version Colab seems to support (or I'm not using it correctly). Attaching hooks and manually getting heatmaps is in there as debug code,but a prepared library would be better (many of them didn't work out of the box with Faster-RCNN architectures).
4. Final model is saved based upon IOU criteria instead of classification validation criteria (best IOU gets saved off). Checking validation against class metrics might produce increased classifier results.
5. US images that are mostly black or very low intensity may throw off the simple cropping (looks for distinct window edge thresholds to differentiate ultrasound embedded image and GUI stuff.
***

References:
1. Al-Dhabyani W, Gomaa M, Khaled H, Fahmy A. Dataset of breast ultrasound images. Data in Brief. 2020 Feb;28:104863. DOI: 10.1016/j.dib.2019.104863.
2. 
