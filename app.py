import streamlit as st
import pickle

pickle_in = open("rf_model.pkl","rb")
classifier=pickle.load(pickle_in)

def predict_note_authentication(type_,air_temp,process_temp,rpm,torque,tool_wear):
    prediction=classifier.predict([[type_,air_temp,process_temp,rpm,torque,tool_wear]])
    print(prediction)
    return prediction

def main():
    st.title("Machine Maintenance Classification")
    type_ = st.selectbox("Product Quality Varient",("Low","Medium","High"))
    air_temp = st.text_input("Air Temprature in K")
    process_temp = st.text_input("Process Temperature in K")
    rpm = st.text_input("Rotational Speed in RPM")
    torque = st.text_input("Torque in Nm")
    tool_wear = st.text_input("Tool Wear in minutes")
    # print(type_, type(air_temp), type(process_temp), type(rpm), type(torque), type(tool_wear))

    result = ""
    if st.button("Predict"):
        if type_ == "Low":
            type_ = 0
        elif type_ == "Medium":
            type_ = 1
        else:
            type_ = 2
        result=predict_note_authentication(type_,float(air_temp),float(process_temp),int(rpm),float(torque),int(tool_wear))
        if result[0]==0:
            st.success('The machine is working fine, no need to replace the tool.')
        elif result[0]==1:
            st.success('Machine failure, replace the tool.')
    st.text("@Analytika - The Data Science Club")

if __name__=='__main__':
    main()