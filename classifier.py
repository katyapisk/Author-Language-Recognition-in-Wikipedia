import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
from sklearn import svm

X = np.array([[6,8,29,8,3,6,30,15,9],
             [6,13,13,8,3,6,30,15,9],
             [6,15,20,8,3,6,30,15,9],
             [6,12,15,8,3,6,30,15,9],
             [5,17,25,8,3,6,30,15,9],
             [5,9,22,8,3,6,30,15,9],
             [6,7,18,8,3,6,30,15,9],
             [6,13,16,8,3,6,30,15,9],
             [6,8,18,8,3,6,30,15,9],
             [6,14,18,8,3,6,30,15,9],
             [6,14,19,8,3,6,30,15,9],
             [6,12,10,8,3,6,30,15,9],
             [6,11,12,8,3,6,30,15,9],
             [5,14,27,8,3,6,30,15,9],
             [6,17,8,8,3,6,30,15,9],
             [6,9,10,8,3,6,30,15,9],
             [6,14,11,8,3,6,30,15,9],
             [6,11,15,8,3,6,30,15,9],
             [5,12,15,8,3,6,30,15,9],
             [6,11,17,8,3,6,30,15,9],
             [5,13,13,8,3,6,30,15,9],
             [5,4,19,8,3,6,30,15,9],
             [6,12,17,8,3,6,30,15,9],
             [6,12,13,8,3,6,30,15,9],
             [5,8,15,8,3,6,30,15,9],
             [6,11,19,8,3,6,30,15,9],
             [6,11,14,8,3,6,30,15,9],
             [5,15,18,8,3,6,30,15,9],
             [5,18,17,8,3,6,30,15,9],
             [5,9,18,8,3,6,30,15,9],
             [6,17,18,8,3,6,30,15,9],
             [6,15,16,8,3,6,30,15,9],
             [5,23,14,8,3,6,30,15,9],
             [5,15,24,8,3,6,30,15,9],
             [6,15,13,8,3,6,30,15,9],
             [5,16,16,8,3,6,30,15,9],
             [6,11,8,8,3,6,30,15,9],
             [6,11,15,8,3,6,30,15,9],
             [6,10,16,8,3,6,30,15,9],
             [6,8,18,8,3,6,30,15,9],
             [6,12,21,8,3,6,30,15,9],
             [4,34,12,8,3,6,30,15,9],
             [5,11,20,8,3,6,30,15,9],
             [6,10,19,8,3,6,30,15,9],
             [6,10,17,8,3,6,30,15,9],
             [5,9,17,8,3,6,30,15,9],
             [6,16,12,8,3,6,30,15,9],
             [6,13,18,8,3,6,30,15,9],
             [6,11,19,8,3,6,30,15,9],
             [6,18,22,8,3,6,30,15,9],
             [6,15,23,8,3,6,30,15,9],
             [6,9,14,8,3,6,30,15,9],
             [5,14,6,8,3,6,30,15,9],
             [5,17,23,8,3,6,30,15,9],
             [5,5,6,8,3,6,30,15,9],
             [6,13,14,8,3,6,30,15,9],
             [5,7,18,8,3,6,30,15,9],
             [6,9,17,8,3,6,30,15,9],
             [6,14,16,8,3,6,30,15,9],
             [6,11,18,8,3,6,30,15,9],
             [6,11,11,8,3,6,30,15,9],
             [6,10,15,8,3,6,30,15,9],
             [6,9,13,8,3,6,30,15,9],
             [6,7,17,8,3,6,30,15,9],
             [5,10,20,8,3,6,30,15,9],
             [5,7,23,8,3,6,30,15,9],
             [6,11,14,8,3,6,30,15,9],
             [6,10,18,8,3,6,30,15,9],
             [6,7,17,8,3,6,30,15,9],
             [6,7,12,8,3,6,30,15,9],
             [5,13,20,8,3,6,30,15,9],
             [6,14,20,8,3,6,30,15,9],
             [6,6,11,8,3,6,30,15,9],
             [6,7,13,8,3,6,30,15,9],
             [5,6,17,8,3,6,30,15,9],
             [5,13,16,8,3,6,30,15,9],
             [5,9,19,8,3,6,30,15,9],
             [6,14,20,8,3,6,30,15,9],
             [5,7,11,8,3,6,30,15,9],
             [6,9,8,8,3,6,30,15,9],
             [5,6,11,8,3,6,30,15,9],
             [5,8,9,8,3,6,30,15,9],
             [5,9,5,8,3,6,30,15,9],
             [6,16,16,8,3,6,30,15,9],
             [5,23,7,8,3,6,30,15,9],
             [5,50,12,8,3,6,30,15,9],
             [5,10,20,8,3,6,30,15,9],
             [6,7,10,8,3,6,30,15,9],
             [6,10,15,8,3,6,30,15,9],
             [5,17,16,8,3,6,30,15,9],
             [6,10,7,8,3,6,30,15,9],
             [5,26,12,8,3,6,30,15,9],
             [6,9,18,8,3,6,30,15,9],
             [5,18,11,8,3,6,30,15,9],
             [5,17,19,8,3,6,30,15,9],
             [7,6,12,8,3,6,30,15,9],
             [6,21,21,8,3,6,30,15,9],
             [6,11,10,8,3,6,30,15,9],
             [5,13,19,8,3,6,30,15,9],
             [5,13,16,8,3,6,30,15,9],
             [6,4,12,8,3,6,30,15,9],
             [5,11,22,8,3,6,30,15,9],
             [5,14,14,8,3,6,30,15,9],
             [5,14,14,8,3,6,30,15,9],
             [6,13,22,8,3,6,30,15,9],
             [5,16,20,8,3,6,30,15,9],
             [7,16,16,8,3,6,30,15,9],
             [6,12,17,8,3,6,30,15,9],
             [5,21,18,8,3,6,30,15,9],
             [5,12,22,8,3,6,30,15,9],
             [5,13,25,8,3,6,30,15,9],
             [6,20,12,8,3,6,30,15,9],
             [6,11,15,8,3,6,30,15,9],
             [5,9,10,8,3,6,30,15,9],
             [7,11,4,8,3,6,30,15,9],
             [6,8,9,8,3,6,30,15,9],
             [5,9,12,8,3,6,30,15,9],
             [6,14,12,8,3,6,30,15,9],
             [6,9,13,8,3,6,30,15,9],
             [6,6,9,8,3,6,30,15,9],
             [5,5,4,8,3,6,30,15,9],
             [5,6,7,8,3,6,30,15,9],
             [6,9,11,8,3,6,30,15,9],
             [5,6,8,8,3,6,30,15,9],
             [5,5,10,8,3,6,30,15,9],
             [5,7,16,8,3,6,30,15,9],
             [6,9,14,8,3,6,30,15,9],
             [5,9,26,8,3,6,30,15,9],
             [6,6,7,8,3,6,30,15,9],
             [6,11,14,8,3,6,30,15,9],
             [6,6,8,8,3,6,30,15,9],
             [6,6,8,8,3,6,30,15,9],
             [6,6,8,8,3,6,30,15,9],
             [5,7,6,8,3,6,30,15,9],
             [6,7,9,8,3,6,30,15,9],
             [6,11,10,8,3,6,30,15,9],
             [5,5,10,8,3,6,30,15,9],
             [6,10,17,8,3,6,30,15,9],
             [6,6,10,8,3,6,30,15,9],
             [6,8,5,8,3,6,30,15,9],
             [5,5,6,8,3,6,30,15,9],
             [6,13,17,8,3,6,30,15,9],
             [5,5,10,8,3,6,30,15,9],
             [5,7,8,8,3,6,30,15,9],
             [5,5,10,8,3,6,30,15,9],
             [6,6,8,8,3,6,30,15,9],
             [6,7,3,8,3,6,30,15,9],
             [5,7,10,8,3,6,30,15,9],
             [5,6,12,8,3,6,30,15,9],
             [5,16,15,8,3,6,30,15,9],
             [6,13,11,8,3,6,30,15,9],
             [5,14,6,8,3,6,30,15,9],
             [5,11,22,8,3,6,30,15,9],
             [6,7,10,8,3,6,30,15,9],
             [5,6,10,8,3,6,30,15,9],
             [5,6,11,8,3,6,30,15,9],
             [5,9,14,8,3,6,30,15,9],
             [6,21,15,8,3,6,30,15,9],
             [5,12,13,8,3,6,30,15,9],
             [5,20,6,8,3,6,30,15,9],
             [6,8,12,8,3,6,30,15,9],
             [6,10,14,8,3,6,30,15,9],
             [5,21,9,8,3,6,30,15,9],
             [6,14,15,8,3,6,30,15,9],
             [6,11,18,8,3,6,30,15,9],
             [6,9,18,8,3,6,30,15,9],
             [5,9,11,8,3,6,30,15,9],
             [6,12,15,8,3,6,30,15,9],
             [5,9,11,8,3,6,30,15,9],
             [5,8,23,8,3,6,30,15,9],
             [7,11,9,8,3,6,30,15,9],
             [5,7,13,8,3,6,30,15,9],
             [6,8,14,8,3,6,30,15,9],
             [5,5,10,8,3,6,30,15,9],
             [6,5,10,8,3,6,30,15,9],
             [6,5,10,8,3,6,30,15,9],
             [6,5,10,8,3,6,30,15,9],
             [6,5,10,8,3,6,30,15,9],
             [6,6,8,8,3,6,30,15,9],
             [6,6,6,8,3,6,30,15,9],
             [6,8,11,8,3,6,30,15,9],
             [6,5,10,8,3,6,30,15,9],
             [5,26,20,8,2,8,28,6,10],
             [6,15,19,8,2,8,28,6,10],
             [6,12,20,8,2,8,28,6,10],
             [6,13,24,8,2,8,28,6,10],
             [6,8,22,8,2,8,28,6,10],
             [6,11,25,8,2,8,28,6,10],
             [6,11,24,8,2,8,28,6,10],
             [6,7,14,8,2,8,28,6,10],
             [5,18,21,8,2,8,28,6,10],
             [5,9,24,8,2,8,28,6,10],
             [6,20,25,8,2,8,28,6,10],
             [7,10,19,8,2,8,28,6,10],
             [6,7,22,8,2,8,28,6,10],
             [6,13,22,8,2,8,28,6,10],
             [6,12,16,8,2,8,28,6,10],
             [5,3,26,8,2,8,28,6,10],
             [5,3,17,8,2,8,28,6,10],
             [6,12,22,8,2,8,28,6,10],
             [6,10,20,8,2,8,28,6,10],
             [6,11,18,8,2,8,28,6,10],
             [6,15,16,8,2,8,28,6,10],
             [6,6,22,8,2,8,28,6,10],
             [6,20,24,8,2,8,28,6,10],
             [4,10,7,8,2,8,28,6,10],
             [6,21,12,8,2,8,28,6,10],
             [6,6,17,8,2,8,28,6,10],
             [6,7,17,8,2,8,28,6,10],
             [5,13,19,8,2,8,28,6,10],
             [6,8,21,8,2,8,28,6,10],
             [6,13,17,8,2,8,28,6,10],
             [6,16,25,8,2,8,28,6,10],
             [6,11,20,8,2,8,28,6,10],
             [5,30,14,8,2,8,28,6,10],
             [5,14,19,8,2,8,28,6,10],
             [6,3,17,8,2,8,28,6,10],
             [5,6,8,8,2,8,28,6,10],
             [6,7,18,8,2,8,28,6,10],
             [5,7,12,8,2,8,28,6,10],
             [6,11,22,8,2,8,28,6,10],
             [6,9,17,8,2,8,28,6,10],
             [6,8,17,8,2,8,28,6,10],
             [5,10,22,8,2,8,28,6,10],
             [5,16,24,8,2,8,28,6,10],
             [5,12,21,8,2,8,28,6,10],
             [5,10,24,8,2,8,28,6,10],
             [6,10,22,8,2,8,28,6,10],
             [5,10,9,8,2,8,28,6,10],
             [5,8,19,8,2,8,28,6,10],
             [5,8,19,8,2,8,28,6,10],
             [4,15,11,8,2,8,28,6,10],
             [5,13,17,8,2,8,28,6,10],
             [5,9,16,8,2,8,28,6,10],
             [7,15,21,8,2,8,28,6,10],
             [5,7,25,8,2,8,28,6,10],
             [6,13,23,8,2,8,28,6,10],
             [5,18,9,8,2,8,28,6,10],
             [6,8,14,8,2,8,28,6,10],
             [5,14,27,8,2,8,28,6,10],
             [5,17,16,8,2,8,28,6,10],
             [5,17,24,8,2,8,28,6,10],
             [6,9,20,8,2,8,28,6,10],
             [5,14,9,8,2,8,28,6,10],
             [6,9,21,8,2,8,28,6,10],
             [5,17,17,8,2,8,28,6,10],
             [6,19,22,8,2,8,28,6,10],
             [5,16,27,8,2,8,28,6,10],
             [6,12,22,8,2,8,28,6,10],
             [6,10,21,8,2,8,28,6,10],
             [5,16,17,8,2,8,28,6,10],
             [6,11,24,8,2,8,28,6,10],
             [6,12,17,8,2,8,28,6,10],
             [6,14,21,8,2,8,28,6,10],
             [5,18,19,8,2,8,28,6,10],
             [4,23,5,8,2,8,28,6,10],
             [6,7,15,8,2,8,28,6,10],
             [5,15,14,8,2,8,28,6,10],
             [6,8,22,8,2,8,28,6,10],
             [5,7,32,8,2,8,28,6,10],
             [5,26,16,8,2,8,28,6,10],
             [6,7,15,8,2,8,28,6,10],
             [5,16,22,8,2,8,28,6,10],
             [5,8,24,8,2,8,28,6,10],
             [5,12,28,8,2,8,28,6,10],
             [5,12,24,8,2,8,28,6,10],
             [5,16,15,8,2,8,28,6,10],
             [5,14,18,8,2,8,28,6,10],
             [6,9,26,8,2,8,28,6,10],
             [6,14,20,8,2,8,28,6,10],
             [6,10,27,8,2,8,28,6,10],
             [5,13,9,8,2,8,28,6,10],
             [6,7,10,8,2,8,28,6,10],
             [6,5,14,8,2,8,28,6,10],
             [6,12,20,8,2,8,28,6,10],
             [7,12,19,8,2,8,28,6,10],
             [6,19,21,8,2,8,28,6,10],
             [6,16,26,8,2,8,28,6,10],
             [6,11,26,8,2,8,28,6,10],
             [6,9,13,8,2,8,28,6,10],
             [6,8,12,8,2,8,28,6,10],
             [6,8,13,8,2,8,28,6,10],
             [6,9,12,8,2,8,28,6,10],
             [6,9,12,8,2,8,28,6,10],
             [6,12,16,8,2,8,28,6,10],
             [6,11,16,8,2,8,28,6,10],
             [5,10,22,8,2,8,28,6,10],
             [5,7,18,8,2,8,28,6,10],
             [5,6,12,8,2,8,28,6,10],
             [5,6,12,8,2,8,28,6,10],
             [5,7,19,8,2,8,28,6,10],
             [5,6,14,8,2,8,28,6,10],
             [6,6,10,8,2,8,28,6,10],
             [5,7,16,8,2,8,28,6,10],
             [5,6,13,8,2,8,28,6,10],
             [5,7,14,8,2,8,28,6,10],
             [5,12,16,8,2,8,28,6,10],
             [5,9,20,8,2,8,28,6,10],
             [6,15,16,8,2,8,28,6,10],
             [6,11,17,8,2,8,28,6,10],
             [5,14,33,8,2,8,28,6,10],
             [6,12,14,8,2,8,28,6,10],
             [5,6,17,8,2,8,28,6,10],
             [6,13,23,8,2,8,28,6,10],
             [5,11,27,8,2,8,28,6,10],
             [6,17,17,8,2,8,28,6,10],
             [5,15,24,8,2,8,28,6,10],
             [5,10,19,8,2,8,28,6,10],
             [5,9,19,8,2,8,28,6,10],
             [6,7,15,8,2,8,28,6,10],
             [6,7,14,8,2,8,28,6,10],
             [6,6,17,8,2,8,28,6,10],
             [6,8,19,8,2,8,28,6,10],
             [6,6,26,8,2,8,28,6,10],
             [6,14,24,8,2,8,28,6,10],
             [6,13,24,8,2,8,28,6,10],
             [6,11,23,8,2,8,28,6,10],
             [6,7,22,8,2,8,28,6,10],
             [6,8,19,8,2,8,28,6,10],
             [6,10,20,8,2,8,28,6,10],
             [6,15,21,8,2,8,28,6,10],
             [6,9,22,8,2,8,28,6,10],
             [6,8,13,8,2,8,28,6,10],
             [6,7,12,8,2,8,28,6,10],
             [6,10,19,8,2,8,28,6,10],
             [6,5,10,8,2,8,28,6,10],
             [7,14,16,8,2,8,28,6,10],
             [6,13,22,8,2,8,28,6,10],
             [6,11,20,8,2,8,28,6,10],
             [6,12,24,8,2,8,28,6,10],
             [6,9,19,8,2,8,28,6,10],
             [6,12,15,8,2,8,28,6,10],
             [5,11,14,8,2,8,28,6,10],
             [6,15,19,8,2,8,28,6,10],
             [4,18,25,8,2,8,28,6,10],
             [5,7,22,8,2,8,28,6,10],
             [5,13,18,8,2,8,28,6,10],
             [5,8,19,8,2,8,28,6,10],
             [6,14,16,8,2,8,28,6,10],
             [6,7,10,8,2,8,28,6,10],
             [7,9,16,8,2,8,28,6,10],
             [6,14,15,8,2,8,28,6,10],
             [6,9,10,8,2,8,28,6,10],
             [6,16,14,8,2,8,28,6,10],
             [6,9,12,8,2,8,28,6,10],
             [6,8,12,8,2,8,28,6,10],
             [7,9,12,8,2,8,28,6,10],
             [6,9,12,8,2,8,28,6,10],
             [6,9,12,8,2,8,28,6,10],
             [6,10,15,8,2,8,28,6,10],
             [6,8,14,8,2,8,28,6,10],
             [6,8,13,8,2,8,28,6,10],
             [7,9,14,8,2,8,28,6,10],
             [6,14,20,8,2,8,28,6,10],
             [6,12,16,8,2,8,28,6,10],
             [7,9,22,8,2,8,28,6,10],
             [6,11,16,8,2,8,28,6,10],
             [5,7,22,8,2,8,28,6,10],
             [6,9,21,8,2,8,28,6,10],
             [6,9,20,8,2,8,28,6,10],
             [6,15,24,8,2,8,28,6,10],
             [6,9,13,10,0.03,4,32,7,10],
             [6,19,21,10,0.03,4,32,7,10],
             [5,19,23,10,0.03,4,32,7,10],
             [6,21,19,10,0.03,4,32,7,10],
             [6,6,15,10,0.03,4,32,7,10],
             [6,12,16,10,0.03,4,32,7,10],
             [6,24,18,10,0.03,4,32,7,10],
             [6,16,19,10,0.03,4,32,7,10],
             [6,18,17,10,0.03,4,32,7,10],
             [6,22,24,10,0.03,4,32,7,10],
             [6,16,16,10,0.03,4,32,7,10],
             [7,14,16,10,0.03,4,32,7,10],
             [6,18,21,10,0.03,4,32,7,10],
             [6,15,17,10,0.03,4,32,7,10],
             [5,18,13,10,0.03,4,32,7,10],
             [6,24,19,10,0.03,4,32,7,10],
             [6,16,19,10,0.03,4,32,7,10],
             [6,26,19,10,0.03,4,32,7,10],
             [5,12,20,10,0.03,4,32,7,10],
             [6,14,12,10,0.03,4,32,7,10],
             [7,13,15,10,0.03,4,32,7,10],
             [6,19,17,10,0.03,4,32,7,10],
             [6,18,17,10,0.03,4,32,7,10],
             [6,18,18,10,0.03,4,32,7,10],
             [6,19,17,10,0.03,4,32,7,10],
             [6,7,18,10,0.03,4,32,7,10],
             [6,19,18,10,0.03,4,32,7,10],
             [6,14,14,10,0.03,4,32,7,10],
             [6,24,17,10,0.03,4,32,7,10],
             [7,13,19,10,0.03,4,32,7,10],
             [6,14,15,10,0.03,4,32,7,10],
             [7,9,14,10,0.03,4,32,7,10],
             [5,11,22,10,0.03,4,32,7,10],
             [5,22,14,10,0.03,4,32,7,10],
             [6,27,20,10,0.03,4,32,7,10],
             [6,16,19,10,0.03,4,32,7,10],
             [5,23,11,10,0.03,4,32,7,10],
             [6,21,22,10,0.03,4,32,7,10],
             [5,9,16,10,0.03,4,32,7,10],
             [6,14,20,10,0.03,4,32,7,10],
             [6,21,23,10,0.03,4,32,7,10],
             [6,12,14,10,0.03,4,32,7,10],
             [6,11,18,10,0.03,4,32,7,10],
             [6,18,18,10,0.03,4,32,7,10],
             [6,40,7,10,0.03,4,32,7,10],
             [5,17,22,10,0.03,4,32,7,10],
             [5,12,20,10,0.03,4,32,7,10],
             [6,18,21,10,0.03,4,32,7,10],
             [5,10,14,10,0.03,4,32,7,10],
             [6,13,19,10,0.03,4,32,7,10],
             [6,14,10,10,0.03,4,32,7,10],
             [6,15,19,10,0.03,4,32,7,10],
             [6,14,21,10,0.03,4,32,7,10],
             [6,16,15,10,0.03,4,32,7,10],
             [5,14,22,10,0.03,4,32,7,10],
             [5,15,20,10,0.03,4,32,7,10],
             [6,11,20,10,0.03,4,32,7,10],
             [5,17,22,10,0.03,4,32,7,10],
             [6,13,19,10,0.03,4,32,7,10],
             [6,9,13,10,0.03,4,32,7,10],
             [6,11,21,10,0.03,4,32,7,10],
             [6,23,22,10,0.03,4,32,7,10],
             [6,16,19,10,0.03,4,32,7,10],
             [7,11,20,10,0.03,4,32,7,10],
             [5,16,21,10,0.03,4,32,7,10],
             [5,12,21,10,0.03,4,32,7,10],
             [6,17,19,10,0.03,4,32,7,10],
             [6,18,20,10,0.03,4,32,7,10],
             [5,19,22,10,0.03,4,32,7,10],
             [6,18,23,10,0.03,4,32,7,10],
             [6,34,10,10,0.03,4,32,7,10],
             [6,15,20,10,0.03,4,32,7,10],
             [7,40,17,10,0.03,4,32,7,10],
             [6,19,23,10,0.03,4,32,7,10],
             [5,20,20,10,0.03,4,32,7,10],
             [6,18,23,10,0.03,4,32,7,10],
             [6,16,20,10,0.03,4,32,7,10],
             [6,14,17,10,0.03,4,32,7,10],
             [6,9,18,10,0.03,4,32,7,10],
             [6,13,22,10,0.03,4,32,7,10],
             [6,15,14,10,0.03,4,32,7,10],
             [6,23,24,10,0.03,4,32,7,10],
             [7,9,11,10,0.03,4,32,7,10],
             [5,11,20,10,0.03,4,32,7,10],
             [6,16,6,10,0.03,4,32,7,10],
             [5,13,19,10,0.03,4,32,7,10],
             [5,8,12,10,0.03,4,32,7,10],
             [5,8,8,10,0.03,4,32,7,10],
             [5,9,14,10,0.03,4,32,7,10],
             [6,11,18,10,0.03,4,32,7,10],
             [5,7,13,10,0.03,4,32,7,10],
             [5,8,11,10,0.03,4,32,7,10],
             [5,7,8,10,0.03,4,32,7,10],
             [5,8,11,10,0.03,4,32,7,10],
             [5,10,13,10,0.03,4,32,7,10],
             [6,8,12,10,0.03,4,32,7,10],
             [5,8,12,10,0.03,4,32,7,10],
             [6,7,10,10,0.03,4,32,7,10],
             [5,8,8,10,0.03,4,32,7,10],
             [6,10,10,10,0.03,4,32,7,10],
             [6,10,15,10,0.03,4,32,7,10],
             [6,8,3,10,0.03,4,32,7,10],
             [6,7,11,10,0.03,4,32,7,10],
             [6,10,12,10,0.03,4,32,7,10],
             [6,13,14,10,0.03,4,32,7,10],
             [5,18,22,10,0.03,4,32,7,10],
             [5,16,23,10,0.03,4,32,7,10],
             [5,13,15,10,0.03,4,32,7,10],
             [6,16,22,10,0.03,4,32,7,10],
             [5,11,20,10,0.03,4,32,7,10],
             [5,21,18,10,0.03,4,32,7,10],
             [5,16,21,10,0.03,4,32,7,10],
             [6,16,22,10,0.03,4,32,7,10],
             [5,15,19,10,0.03,4,32,7,10],
             [6,18,19,10,0.03,4,32,7,10],
             [6,17,19,10,0.03,4,32,7,10],
             [6,11,19,10,0.03,4,32,7,10],
             [5,18,21,10,0.03,4,32,7,10],
             [6,13,19,10,0.03,4,32,7,10],
             [6,20,23,10,0.03,4,32,7,10],
             [7,7,4,10,0.03,4,32,7,10],
             [6,23,21,10,0.03,4,32,7,10],
             [5,19,24,10,0.03,4,32,7,10],
             [6,16,21,10,0.03,4,32,7,10],
             [5,16,22,10,0.03,4,32,7,10],
             [5,12,25,10,0.03,4,32,7,10],
             [5,13,15,10,0.03,4,32,7,10],
             [6,13,14,10,0.03,4,32,7,10],
             [6,16,17,10,0.03,4,32,7,10],
             [6,16,17,10,0.03,4,32,7,10],
             [6,16,20,10,0.03,4,32,7,10],
             [5,14,18,10,0.03,4,32,7,10],
             [5,17,21,10,0.03,4,32,7,10],
             [6,15,13,10,0.03,4,32,7,10],
             [6,8,13,10,0.03,4,32,7,10],
             [6,9,9,10,0.03,4,32,7,10],
             [6,8,11,10,0.03,4,32,7,10],
             [7,17,13,10,0.03,4,32,7,10],
             [7,19,17,10,0.03,4,32,7,10],
             [7,18,16,10,0.03,4,32,7,10],
             [8,17,12,10,0.03,4,32,7,10],
             [8,18,12,10,0.03,4,32,7,10],
             [7,18,14,10,0.03,4,32,7,10],
             [7,20,11,10,0.03,4,32,7,10],
             [8,18,14,10,0.03,4,32,7,10],
             [8,20,9,10,0.03,4,32,7,10],
             [8,15,16,10,0.03,4,32,7,10],
             [7,16,14,10,0.03,4,32,7,10],
             [8,19,14,10,0.03,4,32,7,10],
             [7,17,14,10,0.03,4,32,7,10],
             [8,17,14,10,0.03,4,32,7,10],
             [7,17,13,10,0.03,4,32,7,10],
             [8,17,15,10,0.03,4,32,7,10],
             [7,17,13,10,0.03,4,32,7,10],
             [7,16,15,10,0.03,4,32,7,10],
             [7,16,14,10,0.03,4,32,7,10],
             [7,18,12,10,0.03,4,32,7,10],
             [6,15,18,10,0.03,4,32,7,10],
             [6,19,30,10,0.03,4,32,7,10],
             [6,17,16,10,0.03,4,32,7,10],
             [6,11,15,10,0.03,4,32,7,10],
             [6,11,22,10,0.03,4,32,7,10],
             [6,22,24,10,0.03,4,32,7,10],
             [6,17,19,10,0.03,4,32,7,10],
             [5,9,18,10,0.03,4,32,7,10],
             [4,16,11,10,0.03,4,32,7,10],
             [6,19,22,10,0.03,4,32,7,10],
             [6,19,22,10,0.03,4,32,7,10],
             [6,16,17,10,0.03,4,32,7,10],
             [7,12,22,10,0.03,4,32,7,10],
             [5,14,22,10,0.03,4,32,7,10],
             [6,13,14,10,0.03,4,32,7,10],
             [6,13,17,10,0.03,4,32,7,10],
             [6,12,18,10,0.03,4,32,7,10],
             [5,15,21,10,0.03,4,32,7,10],
             [6,21,21,10,0.03,4,32,7,10],
             [7,7,15,10,0.03,4,32,7,10],
             [5,6,8,10,0.03,4,32,7,10],
             [5,17,17,10,0.03,4,32,7,10],
             [6,9,18,10,0.03,4,32,7,10],
             [6,16,23,9,3,2,33,7,14],
             [6,18,23,9,3,2,33,7,14],
             [7,13,19,9,3,2,33,7,14],
             [6,15,22,9,3,2,33,7,14],
             [5,18,27,9,3,2,33,7,14],
             [6,13,20,9,3,2,33,7,14],
             [6,14,19,9,3,2,33,7,14],
             [6,16,23,9,3,2,33,7,14],
             [6,15,23,9,3,2,33,7,14],
             [6,16,22,9,3,2,33,7,14],
             [6,14,19,9,3,2,33,7,14],
             [6,16,23,9,3,2,33,7,14],
             [6,17,21,9,3,2,33,7,14],
             [6,17,21,9,3,2,33,7,14],
             [6,13,21,9,3,2,33,7,14],
             [6,12,19,9,3,2,33,7,14],
             [6,15,20,9,3,2,33,7,14],
             [6,12,20,9,3,2,33,7,14],
             [6,12,22,9,3,2,33,7,14],
             [5,16,21,9,3,2,33,7,14],
             [6,17,19,9,3,2,33,7,14],
             [6,15,21,9,3,2,33,7,14],
             [5,12,18,9,3,2,33,7,14],
             [6,18,21,9,3,2,33,7,14],
             [5,17,23,9,3,2,33,7,14],
             [6,16,19,9,3,2,33,7,14],
             [6,14,20,9,3,2,33,7,14],
             [6,16,20,9,3,2,33,7,14],
             [6,14,19,9,3,2,33,7,14],
             [6,15,20,9,3,2,33,7,14],
             [6,17,18,9,3,2,33,7,14],
             [5,14,21,9,3,2,33,7,14],
             [6,17,23,9,3,2,33,7,14],
             [6,15,20,9,3,2,33,7,14],
             [6,15,21,9,3,2,33,7,14],
             [5,12,23,9,3,2,33,7,14],
             [6,14,23,9,3,2,33,7,14],
             [7,12,18,9,3,2,33,7,14],
             [7,10,12,9,3,2,33,7,14],
             [6,18,23,9,3,2,33,7,14],
             [7,10,21,9,3,2,33,7,14],
             [6,15,22,9,3,2,33,7,14],
             [6,17,23,9,3,2,33,7,14],
             [6,16,19,9,3,2,33,7,14],
             [6,11,18,9,3,2,33,7,14],
             [6,17,24,9,3,2,33,7,14],
             [6,12,21,9,3,2,33,7,14],
             [7,21,19,9,3,2,33,7,14],
             [6,21,22,9,3,2,33,7,14],
             [6,21,21,9,3,2,33,7,14],
             [5,14,22,9,3,2,33,7,14],
             [6,15,18,9,3,2,33,7,14],
             [6,19,27,9,3,2,33,7,14],
             [6,15,21,9,3,2,33,7,14],
             [5,14,24,9,3,2,33,7,14],
             [6,15,21,9,3,2,33,7,14],
             [6,14,23,9,3,2,33,7,14],
             [6,14,22,9,3,2,33,7,14],
             [6,17,19,9,3,2,33,7,14],
             [6,17,19,9,3,2,33,7,14],
             [6,16,20,9,3,2,33,7,14],
             [6,14,21,9,3,2,33,7,14],
             [6,15,20,9,3,2,33,7,14],
             [6,20,24,9,3,2,33,7,14],
             [6,11,10,9,3,2,33,7,14],
             [6,16,16,9,3,2,33,7,14],
             [5,6,16,9,3,2,33,7,14],
             [6,15,21,9,3,2,33,7,14],
             [6,16,24,9,3,2,33,7,14],
             [6,18,24,9,3,2,33,7,14],
             [6,14,20,9,3,2,33,7,14],
             [6,15,22,9,3,2,33,7,14],
             [6,14,24,9,3,2,33,7,14],
             [6,15,21,9,3,2,33,7,14],
             [6,13,19,9,3,2,33,7,14],
             [5,15,20,9,3,2,33,7,14],
             [6,15,22,9,3,2,33,7,14],
             [6,9,15,9,3,2,33,7,14],
             [6,17,24,9,3,2,33,7,14],
             [7,19,21,9,3,2,33,7,14],
             [7,16,21,9,3,2,33,7,14],
             [6,14,20,9,3,2,33,7,14],
             [7,12,17,9,3,2,33,7,14],
             [7,14,22,9,3,2,33,7,14],
             [7,16,19,9,3,2,33,7,14],
             [6,16,24,9,3,2,33,7,14],
             [6,11,22,9,3,2,33,7,14],
             [6,15,27,9,3,2,33,7,14],
             [6,24,23,9,3,2,33,7,14],
             [6,15,18,9,3,2,33,7,14],
             [6,15,21,9,3,2,33,7,14],
             [6,17,22,9,3,2,33,7,14],
             [5,12,21,9,3,2,33,7,14],
             [5,12,20,9,3,2,33,7,14],
             [6,10,10,9,3,2,33,7,14],
             [6,14,25,9,3,2,33,7,14],
             [6,6,18,9,3,2,33,7,14],
             [6,12,18,9,3,2,33,7,14],
             [5,16,21,9,3,2,33,7,14],
             [5,15,25,9,3,2,33,7,14],
             [6,13,24,9,3,2,33,7,14],
             [5,16,22,9,3,2,33,7,14],
             [6,9,23,9,3,2,33,7,14],
             [6,11,14,9,3,2,33,7,14],
             [6,10,17,9,3,2,33,7,14],
             [6,12,19,9,3,2,33,7,14],
             [6,11,20,9,3,2,33,7,14],
             [5,15,21,9,3,2,33,7,14],
             [7,15,22,9,3,2,33,7,14],
             [5,15,21,9,3,2,33,7,14],
             [5,17,13,9,3,2,33,7,14],
             [5,6,26,9,3,2,33,7,14],
             [5,10,17,9,3,2,33,7,14],
             [5,9,23,9,3,2,33,7,14],
             [6,16,20,9,3,2,33,7,14],
             [5,13,22,9,3,2,33,7,14],
             [5,20,15,9,3,2,33,7,14],
             [5,4,21,9,3,2,33,7,14],
             [6,11,20,9,3,2,33,7,14],
             [5,13,18,9,3,2,33,7,14],
             [5,17,23,9,3,2,33,7,14],
             [6,20,8,9,3,2,33,7,14],
             [5,22,22,9,3,2,33,7,14],
             [6,20,23,9,3,2,33,7,14],
             [6,14,22,9,3,2,33,7,14],
             [6,12,20,9,3,2,33,7,14],
             [7,18,22,9,3,2,33,7,14],
             [6,13,16,9,3,2,33,7,14],
             [6,11,25,9,3,2,33,7,14],
             [5,17,22,9,3,2,33,7,14],
             [6,11,20,9,3,2,33,7,14],
             [5,10,16,9,3,2,33,7,14],
             [6,12,15,9,3,2,33,7,14],
             [6,13,18,9,3,2,33,7,14],
             [6,24,24,9,3,2,33,7,14],
             [6,15,22,9,3,2,33,7,14],
             [6,20,24,9,3,2,33,7,14],
             [6,18,24,9,3,2,33,7,14],
             [5,13,17,9,3,2,33,7,14],
             [6,9,17,9,3,2,33,7,14],
             [5,7,15,9,3,2,33,7,14],
             [5,11,30,9,3,2,33,7,14],
             [6,23,22,9,3,2,33,7,14],
             [6,12,26,9,3,2,33,7,14],
             [6,12,26,9,3,2,33,7,14],
             [5,20,19,9,3,2,33,7,14],
             [5,11,25,9,3,2,33,7,14],
             [6,15,8,9,3,2,33,7,14],
             [6,7,14,9,3,2,33,7,14],
             [6,12,22,9,3,2,33,7,14],
             [7,16,18,9,3,2,33,7,14],
             [5,8,20,9,3,2,33,7,14],
             [6,11,20,9,3,2,33,7,14],
             [5,15,21,9,3,2,33,7,14],
             [5,17,26,9,3,2,33,7,14],
             [6,13,18,9,3,2,33,7,14],
             [6,20,24,9,3,2,33,7,14],
             [5,13,26,9,3,2,33,7,14],
             [6,10,25,9,3,2,33,7,14],
             [5,15,25,9,3,2,33,7,14],
             [6,19,14,9,3,2,33,7,14],
             [6,11,25,9,3,2,33,7,14],
             [6,14,25,9,3,2,33,7,14],
             [6,15,22,9,3,2,33,7,14],
             [5,7,15,9,3,2,33,7,14],
             [5,8,16,9,3,2,33,7,14],
             [6,19,21,9,3,2,33,7,14],
             [5,14,30,9,3,2,33,7,14],
             [6,15,19,9,3,2,33,7,14],
             [6,8,17,9,3,2,33,7,14],
             [6,12,18,9,3,2,33,7,14],
             [6,25,20,9,3,2,33,7,14],
             [6,24,22,9,3,2,33,7,14],
             [6,15,24,9,3,2,33,7,14],
             [6,8,16,9,3,2,33,7,14],
             [7,9,15,9,3,2,33,7,14],
             [6,22,28,9,3,2,33,7,14],
             [6,18,24,9,3,2,33,7,14],
             [7,13,19,9,3,2,33,7,14],
             [6,15,22,9,3,2,33,7,14]])

y = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]

clf = svm.SVC(kernel='linear', C = 1.0)
clf.fit(X,y)
print ('1')
print(clf.predict([6,13,15,8,3,6,30,15,9]))
print ('2')
print(clf.predict([6,12,20,8,3,6,30,15,9]))
print ('3')
print(clf.predict([6,10,16,8,3,6,30,15,9]))
print ('4')
print(clf.predict([7,27,11,8,3,6,30,15,9]))
print ('5')
print(clf.predict([5,11,22,8,3,6,30,15,9]))
print ('6')
print(clf.predict([6,9,14,8,3,6,30,15,9]))
print ('7')
print(clf.predict([6,14,14,8,3,6,30,15,9]))
print ('8')
print(clf.predict([6,13,16,8,3,6,30,15,9]))
print ('9')
print(clf.predict([7,12,12,8,3,6,30,15,9]))
print ('10')
print(clf.predict([6,7,17,8,3,6,30,15,9]))
print ('11')
print(clf.predict([6,17,22,8,2,8,28,6,10]))
print ('12')
print(clf.predict([5,11,19,8,2,8,28,6,10]))
print ('13')
print(clf.predict([6,12,5,8,2,8,28,6,10]))
print ('14')
print(clf.predict([6,19,15,8,2,8,28,6,10]))
print ('15')
print(clf.predict([6,15,18,8,2,8,28,6,10]))
print ('16')
print(clf.predict([7,10,14,8,2,8,28,6,10]))
print ('17')
print(clf.predict([6,13,20,8,2,8,28,6,10]))
print ('18')
print(clf.predict([6,9,15,8,2,8,28,6,10]))
print ('19')
print(clf.predict([5,16,23,8,2,8,28,6,10]))
print ('20')
print(clf.predict([5,6,4,8,2,8,28,6,10]))
print ('21')
print(clf.predict([5,15,21,10,0.03,4,32,7,10]))
print ('22')
print(clf.predict([6,9,15,10,0.03,4,32,7,10]))
print ('23')
print(clf.predict([6,19,17,10,0.03,4,32,7,10]))
print ('24')
print(clf.predict([6,23,24,9,3,2,33,7,14]))
print ('25')
print(clf.predict([6,16,23,9,3,2,33,7,14]))
print ('26')
print(clf.predict([6,13,20,8,2,8,28,6,10]))
print ('27')
print(clf.predict([6,11,18,10,0.03,4,32,7,10]))
print ('28')
print(clf.predict([6,17,19,10,0.03,4,32,7,10]))
print ('29')
print(clf.predict([7,22,17,10,0.03,4,32,7,10]))
print ('30')
print(clf.predict([6,10,11,10,0.03,4,32,7,10]))
print ('31')
print(clf.predict([6,18,22,10,0.03,4,32,7,10]))
print ('32')
print(clf.predict([6,19,18,10,0.03,4,32,7,10]))
print ('33')
print(clf.predict([6,6,15,10,0.03,4,32,7,10]))
print ('34')
print(clf.predict([6,16,13,9,3,2,33,7,14]))
print ('35')
print(clf.predict([6,16,19,9,3,2,33,7,14]))
print ('36')
print(clf.predict([6,14,23,9,3,2,33,7,14]))
print ('37')
print(clf.predict([6,21,24,9,3,2,33,7,14]))
print ('38')
print(clf.predict([6,20,22,9,3,2,33,7,14]))
print ('39')
print(clf.predict([5,10,16,9,3,2,33,7,14]))
print ('40')
print(clf.predict([5,10,17,9,3,2,33,7,14]))
print ('41')
print(clf.predict([6,17,16,9,3,2,33,7,14]))
print ('42')
print(clf.predict([6,13,19,9,3,2,33,7,14]))
print ('43')
print(clf.predict([6,13,18,9,3,2,33,7,14]))
print ('44')
print(clf.predict([6,17,19,9,3,2,33,7,14]))
print ('45')
print(clf.predict([6,7,19,9,3,2,33,7,14]))
print ('46')
print(clf.predict([5,18,24,9,3,2,33,7,14]))
print ('47')
print(clf.predict([7,16,22,9,3,2,33,7,14]))
print ('48')
print(clf.predict([6,9,22,9,3,2,33,7,14]))
print ('49')
print(clf.predict([6,18,21,9,3,2,33,7,14]))
print ('50')
print(clf.predict([5,17,21,9,3,2,33,7,14]))
print ('51')
print(clf.predict([6,16,18,9,3,2,33,7,14]))
print ('52')
print(clf.predict([6,15,21,9,3,2,33,7,14]))
print ('53')
print(clf.predict([6,7,7,8,3,6,30,15,9]))
print ('54')
print(clf.predict([6,5,6,8,3,6,30,15,9]))
print ('55')
print(clf.predict([6,9,3,8,3,6,30,15,9]))
print ('56')
print(clf.predict([6,5,10,8,3,6,30,15,9]))
print ('57')
print(clf.predict([6,8,11,8,3,6,30,15,9]))
print ('58')
print(clf.predict([6,6,6,8,3,6,30,15,9]))
print ('59')
print(clf.predict([6,6,8,8,3,6,30,15,9]))
print ('61')
print(clf.predict([5,5,12,8,3,6,30,15,9]))
print ('62')
print(clf.predict([6,20,13,8,2,8,28,6,10]))
print ('63')
print(clf.predict([6,15,23,8,2,8,28,6,10]))
print ('64')
print(clf.predict([6,10,23,8,2,8,28,6,10]))
print ('65')
print(clf.predict([5,14,28,8,2,8,28,6,10]))
print ('66')
print(clf.predict([5,9,15,8,2,8,28,6,10]))
print ('67')
print(clf.predict([6,16,18,8,2,8,28,6,10]))
print ('68')
print(clf.predict([6,14,25,8,2,8,28,6,10]))
print ('69')
print(clf.predict([6,11,27,8,2,8,28,6,10]))
print ('70')
print(clf.predict([6,13,16,8,2,8,28,6,10]))
print ('71')
print(clf.predict([5,14,11,8,2,8,28,6,10]))
print ('72')
print(clf.predict([6,20,22,10,0.03,4,32,7,10]))
print ('73')
print(clf.predict([6,18,26,10,0.03,4,32,7,10]))
print ('74')
print(clf.predict([6,14,19,10,0.03,4,32,7,10]))
print ('75')
print(clf.predict([6,15,11,10,0.03,4,32,7,10]))
print ('76')
print(clf.predict([4,14,9,10,0.03,4,32,7,10]))
print ('77')
print(clf.predict([5,8,9,10,0.03,4,32,7,10]))
print ('78')
print(clf.predict([5,6,8,10,0.03,4,32,7,10]))
print ('79')
print(clf.predict([5,17,17,10,0.03,4,32,7,10]))
print ('80')
print(clf.predict([6,10,8,10,0.03,4,32,7,10]))
