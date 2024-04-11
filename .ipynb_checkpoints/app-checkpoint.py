import os
import pickle
import streamlit as st

# Print the current working directory
print("Current working directory:", os.getcwd())

# Loading the trained model
pickle_in = open("classifier.pkl", 'rb')
classifier = pickle.load(pickle_in)

# Define mapping for smoking history options
smoking_history_mapping = {
    "Former": 0,
    "Never": 1,
    "Ever": 2,
    "Current": 3,
    "Not Current": 4,
    "No info": 5
}

# Defining the function to make predictions using the user input
@st.cache()
def prediction(HbA1c_level, Blood_glucose_level, BMI, Age, Smoking_history):
   
    # Map smoking history to numerical value
    smoking_history_numeric = smoking_history_mapping[Smoking_history]

    # Making Predictions
    prediction = classifier.predict([[HbA1c_level, Blood_glucose_level, BMI, Age, smoking_history_numeric]])

    if prediction == 0:
        pred = "Negative"
    else:
        pred = "Positive"

    return pred

# Main function to define the Streamlit web app
def main():
    # Front end elements of the web page
    html_temp = '''
    <div style='background-color: yellow; padding:13px'>
    <h1 style='color: black; text-align: center;'>Churn Prediction ML App</h1>
    </div>
    '''

    # Display the front end aspect
    st.markdown(html_temp, unsafe_allow_html=True)

    # Input fields for user data
    HbA1c_level = st.number_input("HbA1c Level")
    Blood_glucose_level = st.number_input("Blood Glucose Level")
    BMI = st.number_input("BMI")
    Age = st.number_input("Age")
    Smoking_history = st.selectbox('Smoking History', tuple(smoking_history_mapping.keys()))

    result = ""

    # When 'Predict' is clicked, make prediction and display the result
    if st.button("Predict"):
        result = prediction(HbA1c_level, Blood_glucose_level, BMI, Age, Smoking_history)
        st.success("Patient is {}".format(result))

if __name__ == '__main__':
    main()