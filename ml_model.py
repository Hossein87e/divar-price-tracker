#!/usr/bin/env python
# coding: utf-8

# libary
#

# In[ ]:


import pickle
import pandas as pd
from sklearn.pipeline import Pipeline  #
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from database_manager import DatabaseManager

model_file = "price_model.pkl"


# تبدیل داده های دیتابیس به dataframe
#

# In[ ]:


def load_data(product_id):
    db = DatabaseManager()
    prices = db.get_prices_for_product(product_id)

    if len(prices) < 5:
        return None

    data = {"previous_price": [], "current_price": [], "weekday": []}

    for i in range(1, len(prices)):
        prev = prices[i - 1]
        curr = prices[i]

        data["previous_price"].append(prev.amount)
        data["current_price"].append(curr.amount)

        data["weekday"].append(curr.date.weekday())
    return pd.DataFrame(data)


# model learning
#

# In[ ]:


def train_model(product_id):
    df = load_data(product_id)
    if df is None:
        return None
    x = df[["previous_price", "weekday"]]
    y = df["current_price"]

    numeric_features = ["previous_price"]
    categorical_feauters = ["weekday"]

    numeric_pipeline = Pipeline(
        [("imputer", SimpleImputer(strategy="median")), ("scaler", StandardScaler())]
    )

    categorical_pipeline = Pipeline(
        [
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("encoder", OneHotEncoder(handle_unknown="ignore")),
        ]
    )

    preprocessor = ColumnTransformer(
        [
            ("num", numeric_pipeline, numeric_features),
            ("cat", categorical_pipeline, categorical_feauters),
        ]
    )

    model = Pipeline(
        [
            ("preprocess", preprocessor),
            ("regressor", RandomForestRegressor(n_estimators=100)),
        ]
    )
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2, random_state=42
    )
    model.fit(x_train, y_train)

    with open(model_file, "wb") as f:
        pickle.dump(model, f)
    return model


# load model
#

# In[ ]:


def load_model():
    try:
        with open(model_file, "rb") as f:
            return pickle.load(f)
    except:
        return None


# predict feauter price
#

# In[ ]:


def predict_future_price(product_id):
    model = load_model()

    if model is None:
        model = train_model(product_id)
        if model is None:
            return None
    df = load_data(product_id)
    if df is None:
        return None

    last_row = df.iloc[-1]

    x_new = pd.DataFrame(
        [{"previous_price": last_row["previous_price"], "weekday": last_row["weekday"]}]
    )

    predict = model.predict(x_new)[0]
    return int(predict)
