# AI-Powered Blind Spot Detection System for Foggy and Rainy Conditions  

## Team NOPE  

### Members  
- Varad Rane  
- Nishaad Gangal  
## Project Structure
The project is organized into two topic folders:  
- **Datasets** – Contains the required datasets for training/testing.  
- **Setup** – Includes setup instructions and dependencies.  
## Problem Statement  

Visibility is significantly reduced in foggy and rainy conditions, making traditional object detection methods unreliable. Our solution focuses on developing an AI-based detection and risk assessment system that enhances vehicle safety under such conditions.  

## 2.2.1 Machine Learning-Based Object Detection  

**Objective:**  
Develop an AI-based detection system that improves object recognition and classification in foggy and rainy conditions.  

**Tasks:**  

- **Dataset Selection & Augmentation:**  
  - Used datasets like BDD100K and Foggy Cityscapes.  
  - Applied data augmentation techniques such as synthetic fog effects, contrast adjustments, and noise reduction.  

- **Object Detection Model Development:**  
  - Trained deep learning models using **YOLO** and **Faster R-CNN**.  
  - Fine-tuned the model for low-visibility scenarios by enhancing contrast, edge detection, and depth estimation.  

- **Preprocessing & Enhancement:**  
  - Implemented **Dehazing, Rain Removal, and Noise Reduction** using Deep Learning-based Image Processing techniques.  
  - Compared traditional filters (**CLAHE, Bilateral Filtering**) vs. AI-based enhancement methods.  

- **Performance Evaluation:**  
  - Evaluated detection accuracy in normal vs. foggy conditions using metrics like **mAP (Mean Average Precision)** and **IoU (Intersection over Union)**.  
  - Optimized the model for **real-time performance** in edge computing environments.  

## 2.2.2 AI-Powered Risk Assessment and Adaptive Decision-Making  

**Objective:**  
Develop an AI-based risk assessment model that classifies potential threats and triggers real-time warnings or adaptive vehicle responses.  

**Tasks:**  

- **Risk Assessment Algorithm Development:**  
  - Trained an AI model to predict potential collisions based on **object distance, velocity, movement trajectory, and vehicle speed**.  
  - Used **Decision Trees** and **Bayesian Networks** for real-time risk prediction.  

- **Adaptive Warning Mechanism:**  
  - Developed a **smart alert system** that provides warnings based on real-time object proximity and motion analysis.  
  - Implemented alert mechanisms such as **audio-visual signals and dashboard notifications**.  

- **Scenario-Based Simulation:**  
  - Tested the system in different driving conditions such as **merging lanes, sharp turns, and highway driving in fog/rain**.  
  - Implemented **real-time decision-making** for vehicle assistance, including **automatic braking and lane departure warnings**.  

## How to Run the Project  

1. Clone the repository:  
   ```bash
   git clone https://github.com/your-repo/IEEE-CodeClash.git
   cd blindspot-detection

2. Further Steps are in the Readme Files inside the Subtopic Folders.
