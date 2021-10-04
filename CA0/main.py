import pandas

initial_data = pandas.read_csv('CA0\\FuelConsumptionCo2.csv')

initial_data['FUELTYPE'] = initial_data['FUELTYPE'].astype('category').cat.codes
initial_data['ENGINESIZE'].fillna(value=initial_data['ENGINESIZE'].mean(),inplace=True)
initial_data['CYLINDERS'].fillna(value=initial_data['CYLINDERS'].mean(),inplace=True)
nan_data = initial_data[initial_data.CO2EMISSIONS.isna()]
# print(nan_data.to_string())
# print(len(initial_data.index)-initial_data.count())
# print(initial_data.describe())
print(initial_data['FUELCONSUMPTION_CITY'].mean())
# print(initial_data[initial_data['FUELCONSUMPTION_CITY'] < 240].FUELCONSUMPTION_CITY.mean())
# print(initial_data[initial_data['FUELCONSUMPTION_CITY'] < 240].FUELCONSUMPTION_CITY.mean())
print(initial_data[initial_data['CO2EMISSIONS'] < 240].FUELCONSUMPTION_CITY.mean())
print(initial_data[initial_data['CO2EMISSIONS'] > 300].FUELCONSUMPTION_CITY.mean())
