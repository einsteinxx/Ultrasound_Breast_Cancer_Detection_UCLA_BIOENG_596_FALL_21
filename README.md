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
Steps for usage
1. The main options page starts at the first cell. It will import needed libraries for colab and the data directories can be changed here. The code options for choosing training or testing are set here too.


This is the main set of options in cell 1. There are two main modes: training and testing. Set run_testing_only to 1 to load the necessary functions and stop right before the training starts. This allows the user to run the code segment that loads particular saved models for testing. Setting run_testing_only to 0 will cause the code to go through the RESNET training sequence

                        ################################################################################
                        #                    MODEL SPECIFIC OPTIONS
                        #
                        # Choose training sets to use
                        training_set = 0 #0=UCLA US, 1 = UCLA + BUSI, 2 = BUSI

                        #choose the normalization path to use
                        #0 is the 0 to 1 Normalization based upon the ultrasound data
                        #1 is the 0 to 1 Normalization based upon the ImageNet data
                        #
                        #
                        model_branch = 1 #0=0to1, 1 = -2to2
                        transfer_train = 0 #we will load the model states from a checkpoint epoch instead

                        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                        #               TURN TRAINING ON OR OFF
                        # Choose to do training or to load models for use in testing only
                        # run_testing_only = 0 is for training, =1 for a stop after loading models. 1 is
                        # used for running a model on the Test dataset
                        run_testing_only = 1


                        # Set use_last_epoch to 1 to start from a pre-trained checkpoint. Setting to 0
                        #starts training from the beginning
                        use_last_epoch = 1 #
                        ################################################################################


2. TBD


3. TESTING
Once the Training has completed or if staring from a pre-generated model, set run_testin_only to 1. This will kick you out of the main training cell and allow you to load the model separately from all the previous data.  The function tab below is where the user can choose which model to load:
                #Load Saved model dictionary for testing


These are the most important sections needed to load in the model. Data selected for testing is very important as it must have been regenerated with this model or saved previously.

The checkpoint method is reused to load the model, with state dict being necessary when saved. Epoch is not necessary, but was automatically included from the training saves. For the UCLA runs, the same training/validation/test data was reused throughout the whole training sequences to reduce any chance of data being mixed between them. For normal runs, data info was saved along with any other info needed for testing.


                checkpoint = torch.load(model_dict)
                modelr.load_state_dict(checkpoint['model_state_dict'])
                #optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
                start_epoch = checkpoint['epoch']



                #
                # Load relevant saved train/validation/test file sets
                #
                print('Loading previous set of train/val/test files')
                #subdir = '0TO1_UCLA_BEST'
                last_data_list = os.path.join(model_dir, subdir,'last_data_set.pickle') #0TO1
                #'/content/gdrive/My Drive/BreastUS/MODEL_SAVE/UCLA_FINAL/last_data_set.pickle'

                archived_data = pickle.load( open( last_data_list, "rb" ) )
                training_data = archived_data[0][0]
                validation_data = archived_data[0][1]
                test_data =archived_data[0][2]
                bounding_box = archived_data[0][3]
                first50 =archived_data[0][4]



4. Test the model with available data

To test out the model, jump to the section below:
                        #FUNCTION: TEST UCLA FINAL MODELS
This function will take in a cutoff and data for the model. The cell below, Run UCLA METRICS, will call this function for cutoffs from 0 - 90% confidence scores. 




                for loop in range(0,10,1):
                    score_cutoff =  float(loop/10) #to get floating point step sizes
                    test_metrics = test_ucla_classification(modelr,input_dataset=test_data, 
                                                            batch_size=batch_size, 
                                                            score_cutoff=score_cutoff, 
                                                            iou_cutoff = iou_cutoff)
                    saved_metrics[loop] = test_metrics


The output will be saved for use in plotting in the next cell. All of the useful metrics (TP/FP/TN/FN, etc...) will be saved for each confidence cutoff



5. Plot Metrics

A generic set of plots produced by this cell, taken from the confidence score calculations saved as pickle files:

![image](https://user-images.githubusercontent.com/27804848/172364215-4198c7e7-47fe-4647-84d2-b61361540c7c.png)


![image](https://user-images.githubusercontent.com/27804848/172364272-74a26b65-d0db-46cd-958c-2a7d2d935a49.png)


![image](https://user-images.githubusercontent.com/27804848/172364345-aa1f2887-a9fe-43ba-9ce1-ba5f84820b78.png)

![image](https://user-images.githubusercontent.com/27804848/172364395-8eff24eb-659d-4a1c-9faa-b211751683ee.png)






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
