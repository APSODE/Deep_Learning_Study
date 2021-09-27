import pandas as PD
from tensorflow.keras import metrics

Y_DATA_LIST = None
X_DATA_LIST = []

USE_DATA = PD.read_csv("gpascore.csv")
# print(USE_DATA.isnull().sum())
# USE_DATA.isnull().sum() #빈칸이나 공백을 찾아서 몇개인지 표시
USE_DATA = USE_DATA.dropna() #빈칸이나 공백을 찾아서 지워줌
# Y_DATA_LIST = [[VALUE] for VALUE in USE_DATA["admit"].values]
Y_DATA_LIST = USE_DATA["admit"].values
# print(Y_DATA_LIST)

for COUNT, ROW in USE_DATA.iterrows():
    PROCESSING_X_DATA = [ROW["gre"], ROW["gpa"], ROW["rank"]]
    # print(f"COUNT == {COUNT}\nVALUE == {PROCESSING_X_DATA}")
    X_DATA_LIST.append(PROCESSING_X_DATA)
# print(X_DATA_LIST)

# 
# exit()

import tensorflow.keras as TFKE
import tensorflow as TF
import numpy as NP



MODEL = TFKE.models.Sequential([
    TFKE.layers.Dense(64, activation = "relu"),
    TFKE.layers.Dense(128, activation = "relu"),
    TFKE.layers.Dense(1, activation = "sigmoid")
])
# .compile(optimizer = "adam", loss = "binary_crossentropy", metrics = ["accuracy"])


MODEL.compile(
    optimizer = "adam",
    loss = "binary_crossentropy",
    metrics = ["accuracy"]
    # optimizer = TFKE.optimizers.Adam(0.001), 
    # loss = TFKE.losses.BinaryCrossentropy(), 
    # metrics = TFKE.metrics.CategoricalAccuracy()
    # metrics = [TFKE.metrics.BinaryAccuracy()] 
    # loss = TFKE.losses.CategoricalCrossentropy()
)
# MODEL.compile(optimizer = "")
MODEL.fit(NP.array(X_DATA_LIST), NP.array(Y_DATA_LIST), batch_size = 2048, epochs = 50000)
# MODEL.fit(NP.array(X_DATA_LIST), NP.array(Y_DATA_LIST), epochs = 1500)

print(MODEL.predict([[740, 3.25, 3]]))




