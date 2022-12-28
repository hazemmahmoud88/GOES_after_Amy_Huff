# -*- coding: utf-8 -*-
"""
Created on Aug 26 2022

This file contains functions to support the Jupyter Notebook files (.ipynb)
written for the CT DEEP specialized training on Sep 13-14, 2022. These functions
were moved to this file to make the training Notebooks cleaner.

@author: Dr. Amy Huff (IMSG at NOAA/NESDIS/STAR), amy.huff@noaa.gov

**Please acknowledge the NOAA/NESDIS/STAR Aerosols and Atmospheric Composition 
Science Team if using any of this code in your work/research!**
"""

# Module for manipulating dates and times
import datetime

# Module to set filesystem paths appropriate for user's operating system
from pathlib import Path

# Library to perform array operations
import numpy as np


# Function used in "abi_level2_download_aws"
# Get observation start and end times as datetime.time objects
# Used to check user-specified observation start/end times for errors
def check_times(start_hour, start_min, end_hour, end_min):
    start = datetime.time(int(start_hour), int(start_min))
    end = datetime.time(int(end_hour), int(end_min))
        
    return start, end


# Function used in "abi_level2_download_aws"
# Get observation date and today's date as datetime.date objects
# Used to check user-specified observation date for errors
def check_future(year_name, month_name, day_name):
    observation_date = datetime.date(year_name, month_name, day_name)
    today = datetime.date.today()
        
    return observation_date, today


# Function used in "abi_level2_download_aws"
# Function used in "abi_aod_process_visualize"
# Used to check user-entered directory paths for errors
def check_directory(directory_path_name):
    try:
        Path(directory_path_name).exists()
        if Path(directory_path_name).exists() == False:
            error_message = 1  # Directory doesn't exist on user's computer
        elif len(directory_path_name) < 1:
            error_message = 2  # User forgot to enter a directory name
        else:
            error_message = 0
    except:
            error_message = 3  # Syntax error in entered directory name

    return error_message


# Function used in "abi_aod_process_visualize"
# Used to create list of floats for lat/lon tick marks to pass to Matplotlib
# NumPy's "arange" function generates array of floats; can't convert directly to a list b/c floats do funny things w/precision
# NumPy's "format_float_positional" function used to return string of float w/correct precision, then appended to list as a float
def generate_ticks(start, stop, increment):
    ticks_array = np.arange(start, stop+increment, increment, dtype=float)
    ticks_list = []
    for tick in ticks_array: 
        ticks_list.append(float(np.format_float_positional(np.float16(tick), unique=False, precision=1)))
    
    return ticks_list

