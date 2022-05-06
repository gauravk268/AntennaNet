# Adjacent Coaxial Line Fed CDRA Optimization using ML Algorithms

![Antenna Model](https://raw.githubusercontent.com/gauravk268/AntennaNet/flask-app/static/antenna.png)

## Introduction
This project has been done in the partial fulfillment of the requirement for the award of Bachelor of Technology in Electronics and Communication Engineering to the Electronics and Communication Engineering Department, Motilal Nehru National Institute of Technology, Allahabad.

<b>This project uses the Machine Learning algorithm to compute the S11 parameter of a cylindrical dielectric resonator antenna. Compared to the conventional methods, it takes much less time to generate the results with comparable accuracy. It gives the S11 value by inputting the height[9mm-11mm], radius[7mm-9mm], and frequency[4GHz-12GHz] for the same type of antenna.</b>

The antenna design of the cylindrical DRA used for this project is shown above. Cylindrical-substrate in the antenna is made of Al2O3 ceramic. A conductive metal ground plane is placed over the cylindrical DRA. Excitation is provided through a coaxial supplied line located near the cylindrical resonator. The probe is positioned on the z-axis.

## Machine Learning Algorithms Used
- Linear Regression
- KNN (K-Nearest Neighbors)
- SVM (Support Vector Machine)
- Decision Tree
- Random Forest
- XG Boost
- Deep Neural Network

## Website
We have deployed the best model that is open for anyone to use and generate results for their own same type of antenna. </br>
[AntennaNet](https://antenna-net.herokuapp.com/)

## Results

#### Below table shows the results obtained on test dataset.
<table>
  <tr>
    <th> Algorithm </th>
    <th> R2 Score  </th>
    <th> MSE       </th>
    <th> MAE       </th>
    <th> RMSE      </th>
    <th> MAPE      </th>
  </tr>
  
  <tr>
    <td> Linear Regression </td>
    <td> 0.014 </td>
    <td> 19.14 </td>
    <td> 3.35 </td>
    <td> 4.37 </td>
    <td> 1.13 </td>
  </tr>
  
  <tr>
    <td> SVR </td>
    <td> 0.20 </td>
    <td> 15.41 </td>
    <td> 2.36 </td>
    <td> 3.92 </td>
    <td> 0.84 </td>
  </tr>
  
  <tr>
    <td> KNN (N = 5) </td>
    <td> 0.96 </td>
    <td> 0.72 </td>
    <td> 0.28 </td>
    <td> 0.85 </td>
    <td> 0.06 </td>
  </tr>
  
  <tr>
    <td> KNN (N = 3) </td>
    <td> 0.97 </td>
    <td> 0.54 </td>
    <td> 0.24 </td>
    <td> 0.73 </td>
    <td> 0.04 </td>
  </tr>
  
  <tr>
    <td> Decision Tree </td>
    <td> 0.93 </td>
    <td> 1.34 </td>
    <td> 0.37 </td>
    <td> 1.15 </td>
    <td> 0.12 </td>
  </tr>
  
  <tr>
    <td> Random Forest </td>
    <td> 0.96 </td>
    <td> 0.73 </td>
    <td> 0.27 </td>
    <td> 0.85 </td>
    <td> 0.06 </td>
  </tr>
  
  <tr>
    <td> XGBoost </td>
    <td> 0.73 </td>
    <td> 5.25 </td>
    <td> 1.27 </td>
    <td> 2.29 </td>
    <td> 0.44 </td>
  </tr>
  
  <tr>
    <td> DNN </td>
    <td> 0.96 </td>
    <td> 0.68 </td>
    <td> 0.36 </td>
    <td> 0.82 </td>
    <td> 0.11 </td>
  </tr>
</table>

Check plots related to all algorithms [here](https://github.com/gauravk268/AntennaNet/tree/master/Machine_Learning_Codes#readme)

#### S11 vs Freq Chart
Below graph shows the S11 vs. Freq comparison chart at height = 8mm & radius = 10mm for KNN (N = 3), Random Forest, and DNN with the HFSS result.

![S11 vs Freq](https://raw.githubusercontent.com/gauravk268/AntennaNet/master/Machine_Learning_Codes/plots/S11_vs_Freq.png)

## Contributors
- [Vivek Rai](https://github.com/Blazer-007)
- [Gaurav Kumar](https://github.com/gauravk268)
- [Ankit Kr. Kushwaha](https://github.com/ankitenf)

## Report Issue
If you find any issue in code, please raise [here](https://github.com/gauravk268/AntennaNet/issues)
