import pandas
from matplotlib import pyplot

initial_data = pandas.read_csv('CA0\\FuelConsumptionCo2.csv')

initial_data['FUELTYPE'] = initial_data['FUELTYPE'].astype('category').cat.codes
initial_data['ENGINESIZE'].fillna(value=initial_data['ENGINESIZE'].mean(),inplace=True)
initial_data['CYLINDERS'].fillna(value=initial_data['CYLINDERS'].mean(),inplace=True)
nan_data = initial_data[initial_data.CO2EMISSIONS.isna()]
# print(nan_data.to_string())
# print(len(initial_data.index)-initial_data.count())
# print(initial_data.describe())
# print(initial_data['FUELCONSUMPTION_CITY'].mean())
# print(initial_data[initial_data['FUELCONSUMPTION_CITY'] < 240].FUELCONSUMPTION_CITY.mean())
# print(initial_data[initial_data['FUELCONSUMPTION_CITY'] < 240].FUELCONSUMPTION_CITY.mean())
# print(initial_data[initial_data['CO2EMISSIONS'] < 240].FUELCONSUMPTION_CITY.mean())
# print(initial_data[initial_data['CO2EMISSIONS'] > 300].FUELCONSUMPTION_CITY.mean())

# co2_240_sum = 0
# co2_240_count = 0
# co2_300_sum = 0
# co2_300_count = 0
# for index,row in initial_data.iterrows():
#     if row['CO2EMISSIONS'] < 240:
#         co2_240_sum += row['FUELCONSUMPTION_CITY']
#         co2_240_count += 1
#     elif row['CO2EMISSIONS'] > 300:
#         co2_300_sum += row['FUELCONSUMPTION_CITY']
#         co2_300_count += 1
# # start = time.time()
# print(f"CO2 Emotion < 240 : {co2_240_sum/co2_240_sum}")
# print(f"CO2 Emotion > 300 : {co2_300_sum/co2_300_count}")

# initial_data['FUELCONSUMPTION_CITY'].hist(grid=True,legend=True)
# pyplot.subplot(1)
# initial_data['ENGINESIZE'].hist(grid=True)
# pyplot.suptitle("Fuel Consumption City Histogram")
# pyplot.ylabel("Frequency")
# pyplot.xlabel("Fuel Consumption")

# pyplot.subplot(2)
# initial_data['CYLINDERS'].hist(grid=True)
# pyplot.suptitle("Fuel Consumption City Histogram")
# pyplot.ylabel("Frequency")
# pyplot.xlabel("Fuel Consumption")

# pyplot.subplot()
# initial_data['FUELCONSUMPTION_CITY'].hist(grid=True)
# pyplot.suptitle("Fuel Consumption City Histogram")
# pyplot.ylabel("Frequency")
# pyplot.xlabel("Fuel Consumption")

# pyplot.subplot()
# initial_data['FUELCONSUMPTION_HWY'].hist(grid=True)
# pyplot.suptitle("Fuel Consumption City Histogram")
# pyplot.ylabel("Frequency")
# pyplot.xlabel("Fuel Consumption")

# pyplot.subplot()
# initial_data['FUELCONSUMPTION_COMB'].hist(grid=True)
# pyplot.suptitle("Fuel Consumption City Histogram")
# pyplot.ylabel("Frequency")
# pyplot.xlabel("Fuel Consumption")

# pyplot.subplot()
# initial_data['FUELCONSUMPTION_COMB_MPG'].hist(grid=True)
# pyplot.suptitle("Fuel Consumption City Histogram")
# pyplot.ylabel("Frequency")
# pyplot.xlabel("Fuel Consumption")

# pyplot.subplot()
# initial_data['CO2EMISSIONS'].hist(grid=True)
# pyplot.suptitle("Fuel Consumption City Histogram")
# pyplot.ylabel("Frequency")
# pyplot.xlabel("Fuel Consumption")

# initial_data.hist(column=['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_CITY','FUELCONSUMPTION_HWY',
#                           'FUELCONSUMPTION_COMB','FUELCONSUMPTION_COMB_MPG','CO2EMISSIONS'],figsize=(10,10))

normalized_data = initial_data
normalized_data['ENGINESIZE'] = (initial_data['ENGINESIZE']-initial_data['ENGINESIZE'].mean())/initial_data['ENGINESIZE'].std()
normalized_data['CYLINDERS'] = (initial_data['CYLINDERS']-initial_data['CYLINDERS'].mean())/initial_data['CYLINDERS'].std()
normalized_data['FUELCONSUMPTION_CITY'] = (initial_data['FUELCONSUMPTION_CITY']-initial_data['FUELCONSUMPTION_CITY'].mean())/initial_data['FUELCONSUMPTION_CITY'].std()
normalized_data['FUELCONSUMPTION_HWY'] = (initial_data['FUELCONSUMPTION_HWY']-initial_data['FUELCONSUMPTION_HWY'].mean())/initial_data['FUELCONSUMPTION_HWY'].std()
normalized_data['FUELCONSUMPTION_COMB'] = (initial_data['FUELCONSUMPTION_COMB']-initial_data['FUELCONSUMPTION_COMB'].mean())/initial_data['FUELCONSUMPTION_COMB'].std()
normalized_data['FUELCONSUMPTION_COMB_MPG'] = (initial_data['FUELCONSUMPTION_COMB_MPG']-initial_data['FUELCONSUMPTION_COMB_MPG'].mean())/initial_data['FUELCONSUMPTION_COMB_MPG'].std()
normalized_data['CO2EMISSIONS'] = (initial_data['CO2EMISSIONS']-initial_data['CO2EMISSIONS'].mean())/initial_data['CO2EMISSIONS'].std()
print(normalized_data.to_string())