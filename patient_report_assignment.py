import pandas as pd
import numpy as np

#patient data 
data = {
    'Name':['Patien-1','Patient-2','Patient-3','Patient-4'],
    'HeartRate': [76, 74, 72, 78],
    'BloodPressure': [126, 120, 118, 136],
    'Temperature': [38.0, 38.0, 37.5, 37.0]
}
patient_data = pd.DataFrame(data)

# Calculate mean values 
mean_heart_rate = patient_data['HeartRate'].mean()
mean_temperature = patient_data['Temperature'].mean()
mean_blood_pressure = patient_data['BloodPressure'].mean()

# Subtract mean values from each patient's data and store it centered_data variable
centered_data = patient_data.copy()
centered_data['HeartRate'] -= mean_heart_rate
centered_data['Temperature'] -= mean_temperature
centered_data['BloodPressure'] -= mean_blood_pressure

# Calculate vector magnitudes 
magnitudes = np.sqrt(centered_data['HeartRate']+ centered_data['Temperature'] + centered_data['BloodPressure'])

#patient farthest from the rest
farthest_patient_index = magnitudes.idxmax()
farthest_patient = patient_data.loc[farthest_patient_index]

print("Farthest Patient:")
print(farthest_patient)

# Two patients with the smallest magnitudes using index fn
nearest_indices = magnitudes.nsmallest(2).index
nearest_patients = patient_data.loc[nearest_indices]

print("Nearest Patients:")
print(nearest_patients)

# dummy patient
new_patient = pd.DataFrame({
    'Name':['Dummy '],
    'HeartRate': [80],
    'BloodPressure': [125],
    'Temperature': [38.5]
})

# Calculate mean values for the new patient
mean_heart_rate_new = new_patient['HeartRate'].mean()
mean_temperature_new = new_patient['Temperature'].mean()
mean_blood_pressure_new = new_patient['BloodPressure'].mean()

# Subtract mean values from the new patient's data
centered_new_patient = new_patient.copy()
centered_new_patient['HeartRate'] -= mean_heart_rate_new
centered_new_patient['Temperature'] -= mean_temperature_new
centered_new_patient['BloodPressure'] -= mean_blood_pressure_new

# Calculate vector magnitudes for the new patient
magnitudes_new_patient = np.sqrt( centered_new_patient['HeartRate'] + centered_new_patient['Temperature'] + centered_new_patient['BloodPressure'])

# Find the index of the closest patient to the new dummy patient
closest_index = magnitudes.idxmin()
closest_patient = patient_data.loc[closest_index]

print("Closest Patient to the New Dummy Patient:")
print(closest_patient)





