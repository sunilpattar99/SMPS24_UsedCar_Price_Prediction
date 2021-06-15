import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

def predict_price(year, kilometers_driven, mileage, engine, power, seats, location11, fuel_type, transmission, owner_type):
    l1 = [year, kilometers_driven, mileage, engine, power, seats]
    l2 = ['Banglore','Chennai','Coimbatore', 'Delhi', 'Hyderabad','Jaipur', 'Kochi', 'Kolkata','Mumbai','Pune']
    l22 = []
    l3 = ['Diesel', 'LPG', 'Petrol']
    l33 = []
    l4 = []
    l5 = []
    for i in range(len(l2)):
        if location11 == l2[i]:
            l2[i] = 1
        else:
            l2[i] = 0
    
    for i in range(len(l3)):
        if fuel_type == l3[i]:
            l3[i] = 1
        else:
            l3[i] = 0
        
    if transmission == "Manual":
        l4.append(1)
    else:
        l4.append(0)
    
    if owner_type == "First":
        l5.append(1)
    elif owner_type == "Second":
        l5.append(2)
    elif owner_type == "Third":
        l5.append(3)
    else:
        l5.append(4)
    
    result = rf_reg.predict([l1 + l2 + l3 + l4 + l5])
    return round(result[0], 2)


data = pd.read_csv("clean_data.csv")
data = data.iloc[:,1:]

X = data.loc[:,['Year', 'Kilometers_Driven', 'Owner_Type', 'Seats',
       'Mileage', 'Engine', 'Power', 
       'Location_Bangalore', 'Location_Chennai', 'Location_Coimbatore',
       'Location_Delhi', 'Location_Hyderabad', 'Location_Jaipur',
       'Location_Kochi', 'Location_Kolkata', 'Location_Mumbai',
       'Location_Pune', 'Fuel_Type_Diesel', 'Fuel_Type_LPG',
       'Fuel_Type_Petrol', 'Transmission_Manual']]

y = data.loc[:,['Price']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 25)

rf_reg = RandomForestRegressor()
rf_reg.fit(X_train, y_train)
y_pred2= rf_reg.predict(X_test)
# print("Accuracy on Traing set: ",rf_reg.score(X_train,y_train))
# print("Accuracy on Testing set: ",rf_reg.score(X_test,y_test))

# print(predict_price(2012, 160000, 15.2, 1248, 74, 5.0, 'Pune', 'Diesel', 'Manual', 'First'))