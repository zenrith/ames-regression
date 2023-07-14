import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin


class Binariser(BaseEstimator, TransformerMixin):
    def __init__(self, variables):
        if not isinstance(variables, list):
            raise ValueError("Variables should be a list")

        self.variables = variables

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()
        for var in self.variables:
            X[var] = np.where(X[var] == 0, 0, 1)

        return X


class UseOtherColumnsImputer(BaseEstimator, TransformerMixin):
    def __init__(self, variables, references):
        if (not isinstance(variables, list)) or (not isinstance(references, list)):
            raise ValueError("Inputs should be a list")

        if len(variables) != len(references):
            raise ValueError("Length of both lists should be the same")

        self.variables = variables
        self.references = references

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()
        for i in range(len(self.variables)):
            X[self.variables[i]] = np.where(
                X[self.variables[i]].isnull(),
                X[self.references[i]],
                X[self.variables[i]],
            )
        return X


class FeatureCreator(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()

        # discrete
        X["TotBathrooms"] = (
            X["BsmtFullBath"]
            + X["BsmtHalfBath"] * 0.5
            + X["FullBath"]
            + X["HalfBath"] * 0.5
        )
        X["TotRms"] = X["TotBathrooms"] + X["TotRmsAbvGrd"]

        # continuous
        X["TotalSF"] = X["TotalBsmtSF"] + X["1stFlrSF"] + X["2ndFlrSF"]
        X["TotPorchSF"] = (
            X["OpenPorchSF"]
            + X["3SsnPorch"]
            + X["EnclosedPorch"]
            + X["ScreenPorch"]
            + X["WoodDeckSF"]
        )
        X["TotLivArea"] = X["GrLivArea"] + X["TotalBsmtSF"]

        # time diff
        year_vars = ["YearBuilt", "YearRemodAdd", "GarageYrBlt"]
        for var in year_vars:
            X[var] = X["YrSold"] - X[var]

        X["IsNew"] = np.where(X["YearRemodAdd"] == X["YearBuilt"], 0, 1)

        return X
