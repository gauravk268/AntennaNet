import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.metrics import mean_squared_error, mean_absolute_error

def printLosses(y_pred, y_test):
  R2_SCORE = r2_score(y_test, y_pred)
  MSE = mean_squared_error(y_test, y_pred)
  MAE = mean_absolute_error(y_test, y_pred)
  RMSE = np.sqrt(mean_squared_error(y_test, y_pred))
  MAPE = mean_absolute_percentage_error(y_test, y_pred)
  RMSPE = (np.sqrt(np.mean(np.square((y_test - y_pred) / y_test)))) #* 100

  print("R2 Score on test set is : ", R2_SCORE)
  print("Mean Squared Error on test set is : ", MSE)
  print("Mean Absolute Error on test set is : ", MAE)
  print("Root Mean Squared Error on test set is : ", RMSE)
  print("Mean Absolute Percentage Error on test set is : ", MAPE)
  print("Root Mean Squared Percentage Error on test set is : ", RMSPE)

def generatePredictionPlot(y_pred, y_test, algo = "KNN"):
  filepath = f"plots/{algo}"
  plt.scatter(x=y_test, y=y_pred, c='red', alpha=0.6)
  plt.plot(y_test, y_test,color='navy')
  plt.title(f'{algo} - Predicted vs Actual values')
  plt.xlabel('Actual values')
  plt.ylabel('Predicted values')
  plt.savefig(filepath)
  plt.show()