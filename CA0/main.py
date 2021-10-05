import pandas
from matplotlib import pyplot
import numpy

initial_data = pandas.read_csv('CA0\\FuelConsumptionCo2.csv')

initial_data['FUELTYPE'] = initial_data['FUELTYPE'].astype('category').cat.codes
initial_data['ENGINESIZE'].fillna(value=initial_data['ENGINESIZE'].mean(), inplace=True)
initial_data['CYLINDERS'].fillna(value=initial_data['CYLINDERS'].mean(), inplace=True)
nan_data = initial_data[initial_data.CO2EMISSIONS.isna()]
initial_data.dropna(subset=['CO2EMISSIONS'], inplace=True)
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
normalized_data['ENGINESIZE'] = (initial_data['ENGINESIZE'] - initial_data['ENGINESIZE'].mean()) / initial_data[
    'ENGINESIZE'].std()
normalized_data['CYLINDERS'] = (initial_data['CYLINDERS'] - initial_data['CYLINDERS'].mean()) / initial_data[
    'CYLINDERS'].std()
normalized_data['FUELCONSUMPTION_CITY'] = (initial_data['FUELCONSUMPTION_CITY'] - initial_data[
    'FUELCONSUMPTION_CITY'].mean()) / initial_data['FUELCONSUMPTION_CITY'].std()
normalized_data['FUELCONSUMPTION_HWY'] = (initial_data['FUELCONSUMPTION_HWY'] - initial_data[
    'FUELCONSUMPTION_HWY'].mean()) / initial_data['FUELCONSUMPTION_HWY'].std()
normalized_data['FUELCONSUMPTION_COMB'] = (initial_data['FUELCONSUMPTION_COMB'] - initial_data[
    'FUELCONSUMPTION_COMB'].mean()) / initial_data['FUELCONSUMPTION_COMB'].std()
normalized_data['FUELCONSUMPTION_COMB_MPG'] = (initial_data['FUELCONSUMPTION_COMB_MPG'] - initial_data[
    'FUELCONSUMPTION_COMB_MPG'].mean()) / initial_data['FUELCONSUMPTION_COMB_MPG'].std()
normalized_data['CO2EMISSIONS'] = (initial_data['CO2EMISSIONS'] - initial_data['CO2EMISSIONS'].mean()) / initial_data[
    'CO2EMISSIONS'].std()
# print(normalized_data.to_string())

# pyplot.scatter(normalized_data['ENGINESIZE'],normalized_data['CO2EMISSIONS'],c='#fc3503')
# pyplot.xlabel('ENGINESIZE')
# pyplot.ylabel('CO2EMISSIONS')
# pyplot.show()
#
# pyplot.scatter(normalized_data['CYLINDERS'],normalized_data['CO2EMISSIONS'],c='#fc3503')
# pyplot.xlabel('CYLINDERS')
# pyplot.show()
#
# pyplot.scatter(normalized_data['FUELCONSUMPTION_CITY'],normalized_data['CO2EMISSIONS'],c='#fc3503')
# pyplot.xlabel('FUELCONSUMPTION_CITY')
# pyplot.ylabel('CO2EMISSIONS')
# pyplot.show()
#
# pyplot.scatter(normalized_data['FUELCONSUMPTION_HWY'],normalized_data['CO2EMISSIONS'],c='#fc3503')
# pyplot.xlabel('FUELCONSUMPTION_HWY')
# pyplot.ylabel('CO2EMISSIONS')
# pyplot.show()
#
# pyplot.scatter(normalized_data['FUELCONSUMPTION_COMB'],normalized_data['CO2EMISSIONS'],c='#fc3503')
# pyplot.xlabel('FUELCONSUMPTION_COMB')
# pyplot.ylabel('CO2EMISSIONS')
# pyplot.show()
#
# pyplot.scatter(normalized_data['FUELCONSUMPTION_COMB_MPG'],normalized_data['CO2EMISSIONS'],c='#fc3503')
# pyplot.xlabel('FUELCONSUMPTION_COMB_MPG')
# pyplot.ylabel('CO2EMISSIONS')
# pyplot.show()

data = [initial_data['FUELCONSUMPTION_CITY'], initial_data['CO2EMISSIONS']]
header = ['FUELCONSUMPTION_CITY', 'CO2EMISSIONS']
linear_data = pandas.concat(data, axis=1, keys=header)
# print(linear_data.to_string())

# from sklearn.linear_model import LinearRegression
#
# print(linear_data.values)
# x_train = linear_data['FUELCONSUMPTION_CITY'].values
# x_train = x_train.reshape(len(x_train),1)
# y_train = linear_data['CO2EMISSIONS'].values
#
# lr = LinearRegression()
#
# lr.fit(x_train, y_train)
# LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)
#
# nan_data['CO2EMISSIONS'] = lr.predict(nan_data['FUELCONSUMPTION_CITY'].values.reshape((-1,1)))
#
# print(nan_data.to_string())

# pyplot.scatter(linear_data['FUELCONSUMPTION_CITY'],linear_data['CO2EMISSIONS'])
# print(x_train)
# print("#########################################################################################################")
# print(y_train)
# b = numpy.linalg.inv(x_train).dot(y_train)
# print(b)

X, y = linear_data.values[:,0], linear_data.values[:,1]
X = X.reshape((len(X), 1))
# calculate coefficients
b = numpy.linalg.pinv(X).dot(y)
print(b)
# predict using coefficients
yhat = X.dot(b)
# plot data and predictions
pyplot.scatter(X, y)
pyplot.plot(X, yhat, color='red')
pyplot.show()
m = (X[0]-X[1])/(yhat[0]-yhat[1])
print(m)
print(y[0]-(m*X[0]))

sum = 0
i = 0
for index,row in linear_data.iterrows():
    sum += (row['CO2EMISSIONS']-yhat[i]) ** 2
    i += 1
print(sum/i)