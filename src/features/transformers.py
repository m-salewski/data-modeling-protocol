import pandas as pd
import numpy as np

### Missing values ###
# TODO make a class to group all the methods below: get cols, explore missing, drop cols

def explore_missing_values(df, fraction_threshold):
    """ Returns a pandas dataframe with column name and fraction of rows with missing values """
    missing = [(col, df[col].isna().mean()) for col in df]
    df_missing = pd.DataFrame(missing, columns=["column_name", "fraction_missing"])
    df_missing = missing[missing.percent_missing > fraction_threshold]
    return df_missing

def get_cols_to_drop(df, fraction_threshold):
    return [col for col in df if (df[col].isna().mean() > fraction_threshold)]

### Drop features based on correlation ###

def get_corr_feature_drop(df, threshold=0.95):
    # from https://chrisalbon.com/machine_learning/feature_selection/drop_highly_correlated_features/
    # also seen in https://stackoverflow.com/questions/29294983/how-to-calculate-correlation-between-all-columns-and-remove-highly-correlated-on
    """
    Basic, minimal feature drop function: 
    blindly selects correlations to drop based on correlation
    """
    # Create correlation matrix, with abs since interested only in magnitude
    corr_matrix = df.corr().abs()

    # Select upper triangle of correlation matrix
    upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(np.bool))

    # Find index of feature columns with correlation greater than threshold
    to_drop = [column for column in upper.columns if any(upper[column] > threshold)]

    return to_drop

def feature_selector():
    pass

def feature_separator():
    # Separates numerical from categorical features
    pass

def corr_based_feature_selector():
    # Drops features if they are highly correlated
    pass

def ordinal_encoder():
    # Ordinal encoder of categorical features
    pass

def one_hot_encoder():
    # One-hot encoder of categorical features
    pass
