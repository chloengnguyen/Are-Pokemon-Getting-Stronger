# Detect outliers 
import numpy as np
import pandas as pd
from scipy import stats

def detect_outlier(data):
    '''
    A function that identify an outlier in a sample using 3 std.
    +++++
    INPUT:

        data (lst)
    +++++
    OUTPUT:

        outliers (int)
    '''
    outliers = []
    threshold = 3.5
    mean_1 = np.mean(data)
    std_1 =np.std(data)
    
    
    for y in data:
        z_score = (y - mean_1)/std_1 
        if np.abs(z_score) > threshold:
            outliers.append(y)
    return outliers


def p_value(df1, df2, col_list):
    '''
    A function that returns p value for hypothesis testing of 2 samples
    +++++
    INPUT:

        df1 (object) : a DataFrame of pokemon from older generations
        df2 (object) : a DataFrame of pokemon from newer generations
        col_list (lst) : a list of the stat categories
    +++++ 
    OUTPUT: 

        p_val_lst (lst) : a list of int 
        dof_lst (lst) : a list of int
    '''
    p_val_lst = []
    dof_lst = []
    for col in col_list:
        old = list(df1[col])
        new = list(df2[col])
        outlier_1 = detect_outlier(old)
        outlier_2 = detect_outlier(new)
        if len(outlier_1) >= 1:
            for elements in outlier_1:
                old.remove(elements)
                
        else:
            pass
        if len(outlier_2) >= 1:
            for elements in outlier_2:
                new.remove(elements)
                
        else:
            pass
        degree_of_freedom = welch_df(old, new)
        test_statistic = welch_test_statistic(old, new)
        students = stats.t(degree_of_freedom)
        p_val = students.cdf(test_statistic) + (1 - students.cdf(-test_statistic))
        p_val_lst.append(p_val)
        dof_lst.append(degree_of_freedom )
    return p_val_lst, dof_lst