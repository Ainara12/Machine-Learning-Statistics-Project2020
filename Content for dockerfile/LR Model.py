
#This is the code to create and run the LR model that I am using to Predict power output values from
#entered wind speed values:
#Process followed and instructions in commens below:


#First we import the modules we are going to use
from sklearn.linear_model import LinearRegression #import linear regression model
from sklearn.model_selection import train_test_split #to divide data

#loading the dataset we are going to work with

Powerdataset=pd.read_csv('Powerproduction dataset.csv', delimiter=',')


x=Powerdataset['speed']
y=Powerdataset['power']

#plotting dataset to see its distribution

Powerdataset.plot(kind='scatter', x= 'speed', y='power')

plt.show()

#Let's create our linear regression model

#doing test train split

X_train, X_test, y_train, y_test= train_test_split(Powerdataset.speed, Powerdataset.power)


#Plotting the data spplit done in cell above.
#Train data shows in green while test data is in red

plt.scatter(X_train, y_train, label='Training Data', color='g', alpha=.7)
plt.scatter(X_test, y_test, label='Test Data', color= 'r', alpha=.7)
plt.legend()

plt.title('Test train split')

plt.show()

#Model creation
#naming model LR as Linear Regression
LR=LinearRegression()
LR.fit(X_train.values.reshape(-1,1), y_train.values)#Adding x_train and y_train values and reshaping X_train values as they need to be in
#a 1d shape for this to work

# Predicting power values using this model we created

prediction=LR.predict(X_test.values.reshape(-1,1))

#Plotting X_test against prediction results in same plot
plt.plot(X_test, prediction, label='Linear Regression', color='r')
plt.scatter(X_test, y_test, label='Actual Test Data', color='b', alpha=.7)
plt.legend()

plt.show()


#Making predictions for specific values
#using command predict we enter a sample wind speed:

print('This is the power generated considering your input: ')
LR.predict(np.array([[25.00]]))[0]


#score function to determine whether the model is accurate. Maximum punctuation is 1.0 .

LR.score(X_test.values.reshape(-1,1),y_test.values)



