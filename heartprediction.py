### import the libraries
import streamlit as st
import keras
from PIL import Image
import numpy as np

# Page configuration
def main():
    st.set_page_config(page_title="Heart Failure Predictor", layout='wide')

### Load the ANN model into the environment
model = keras.models.load_model("heart_disease.h5")

# Create a function for prediction
# Change user's input into arrays
# Change shape into a 2D array by reshape
def heart_prediction(input):
    input_array = np.array(input)
    input_reshape = input_array.reshape(1, -1)
    prediction = model.predict(input_reshape)
    print(prediction)

    # If prediction = 0, return
    if prediction[0] == 0:
        return "You are likely to die from heart failure given your health conditions"
    else:
        return "You are NOT likely to die from heart failure given your health condition"


## Add image
#heart_image = Image.open('bitch.jpg')
#st.Image(heart_image, use_column_width=False)

## Set title and content
st.title('Heart Failure Predictor using Artificial Neural Network')
st.write('Enter your personal data to get your heart risk evaluation')

# Get input from the user
# Using label encoder, know that 1= female and male = 0
# Have consistency, therefore yes=1 and no=0 unless you have documentation

age = st.number_input('Age of the patient:', min_value=0, step=1)
anaemia = st.number_input('Anaemia | Yes or No | yes=1 and no=0', min_value=0, step=1)
creatinine = st.number_input('Level of CPK enzyme in the blood (mg/L)', min_value=0, step=1)
diabetes = st.number_input('Diabetes | Yes or No | yes=1 and no=0', min_value=0, step=1)
ejection_fraction = st.number_input('Percentage of blood leaving the heart', min_value=0, step=1)
high_blood_pressure = st.number_input('Hypertension | Yes or No | yes=1 and no=0', min_value=0, step=1)
platelets = st.number_input('Platelet count of blood', min_value=0, step=1)
serum_creatinine = st.number_input('Level of serum creatinine in the blood (mg/L)', min_value=0, step=1)
serum_sodium = st.number_input('Level of serum sodium in the blood (mg/L)', min_value=0, step=1)
sex = st.number_input('Sex | Male or Female | Female=1 and Male=0', min_value=0, step=1)
smoker = st.number_input('Smoker | Yes or No | yes=1 and no=0', min_value=0, step=1)
time = st.number_input('Follow up period (days)', min_value=0, step=1)

# Code for prediction
predict = ''

# Button for prediction
if st.button('Predict'):
    predict = heart_prediction([age, anaemia, creatinine, diabetes, ejection_fraction, high_blood_pressure, platelets, serum_creatinine, serum_sodium, sex, smoker, time])

st.success(predict)

# Running as script
if __name__ == '__main__':
    main()


#python -m streamlit run PENIS.py
# pip freeze > requirment.txt

