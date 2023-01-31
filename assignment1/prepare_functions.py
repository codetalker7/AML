import numpy as np
import pandas as pd
import csv
from textblob import TextBlob
from sklearn.model_selection import train_test_split

def load_data(file_path, separator='\t'):
    """
    Load data from ``file_path`` as a dataframe.
    
    :param file_path: Path of the data file.
    """
    return pd.read_csv(file_path, sep=separator, names=["label" ,"message"])

def save_data(file_path, df):
    """
    Save ``df`` to the given ``file_path`` as a CSV file.
    
    :param file_path: Path of the file to be saved.
    :param df: Dataframe containing the data to be saved.
    """
    df.to_csv(file_path, index=False, header=False)
    
def prepare_train_validation_test_split(df, train_percent=0.7, test_percent=0.15, seed=None):
    """
    Create a randomized 70-15-15 train/validation/test split.
    
    :param df: Dataframe containing the data to be split.
    :param train_percent: Percentage allotted to training data.
    :param validate_percent: Percentage allotted to validation data.
    :param seed: Seed for random number generator.
    
    :returns: A tuple (data_train, data_validate, data_test)
    """
    data, data_test = train_test_split(df, test_size=test_percent, random_state=seed)
    data_train, data_validate = train_test_split(data, train_size=(train_percent)/(1 - test_percent), random_state=seed)
    return (data_train, data_validate, data_test)

def split_into_lemmas(message):
    message = message.lower()
    words = TextBlob(message).words
    # for each word, take its "base form" = lemma 
    return [word.lemma for word in words]