# Alzheimer MRI Classification – Early Detection with Machine Learning

## Context
Alzheimer's disease is a neurodegenerative disorder where early detection is critical for therapeutic intervention. This project classifies MRI scans into four stages: Very Mild, Mild, Moderate, and Normal.

## Dataset
- Source: Kaggle Alzheimer MRI Dataset
- Number of images: 6400
- Classes: Very Mild Demented, Mild Demented, Moderate Demented, Normal
- Note: Dataset is imbalanced, with few Moderate Demented cases.

## Preprocessing
- Resize images to 128x128 pixels
- Convert to grayscale
- Convert images to arrays for machine learning

## Models
### Logistic Regression
- Accuracy: 96.5%
- Performs well across all classes, including early-stage detection
- Handles class imbalance better in this dataset

### Random Forest
- Accuracy: 92.0%
- Struggles with Moderate Demented class (recall = 0.23)

## Model Comparison
Logistic Regression outperformed Random Forest on this dataset. Early-stage detection is critical for clinical intervention. Random Forest errors highlight difficulty distinguishing adjacent disease stages.

## Error Analysis
- Visualized misclassified images
- Most errors occur between adjacent stages (Very Mild ↔ Mild)
- Clinically plausible due to subtle structural differences

## Limitations and Future Work
- Class imbalance, few samples for Moderate Demented
- Logistic Regression is a baseline; deep learning may improve results
- Future work: CNN, data augmentation, external validation

## Results
- Confusion matrix
- Classification reports
- Examples of misclassified MRI images
