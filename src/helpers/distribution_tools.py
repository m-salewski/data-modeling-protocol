#!/usr/bin/env python
# coding: utf-8

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

def get_smooth_ids(df, identifier, target, peaks, bin_width, verbose=False):
    
    """ Return a pd.DF with the fill rates of columns in a data frame
    
    Compute the fill rates of a given DF and export the DF 
    with colunms above a given threshold.
    
    Args:    
        df   (pd.DataFrame): input DF
        identifier    (str): unique identifer to filter and return
        target        (str): target feature for the distirubtion
        peaks    (np.array): array of known peaks
        bin_width   (float): bin width of the histgram
        verbose      (bool): for diagnostics
        
        
    Returns: 
        list: list of filtered identifiers
        (when above the threshold)

    Raises:
        None

    Examples:
        >>> df.shape
        1000,1000
        >>> df_fill_rates = get_fill_rates(df, 0.10)
        >>> df_fill_rates
        
    """       
    df_cp = df.copy()
    
    target_bin = target + "_bin"
    
    df_cp[target_bin] = df_cp[target].apply(lambda x: x-x%bin_width)
    
    # The the counts of the nearby bins, then average for a sample from the outlier bin
    avg_counts = []
    for z in peaks:

        lo = df_cp[(df_cp[target_bin]==z-bin_width)][target].count()
        sp = df_cp[(df_cp[target]==z)][target].count()
        hi = df_cp[(df_cp[target_bin]==z+bin_width)][target].count()  

        avg = 0.5*(lo+hi)

        if verbose: print(z,'\t',lo,'\t', sp,'\t', hi, '\t', avg)    

        avg_counts.append(avg)

    # 1. Sample from the outlier bin
    # 2. remove the outlier bin
    # 3. replace the outlier bin with a subsample
    # NOTE: Either we sample 
    #   1. from the bin, or 
    #   2. from a specific outlying value ==> target_bin = target    
    target_bin = target
    if verbose: print('\nStarting with:', df_cp.shape)
    for n,z in enumerate(peaks):

        samp_size = int(avg_counts[n])
        if verbose: print(f'{z}:', int(samp_size))

        # See NOTE above
        #df_samp = df_cp[df_cp[target_bin]==z]            
        df_samp = df_cp[df_cp[target_bin]==z]
        
        if verbose: print('1',df_cp.shape, df_samp.shape)   
            
        # There might not be enough rows to properly sample from
        alt_samp_size = df_samp.shape[0]
        df_samp = df_samp.sample(min(samp_size, alt_samp_size))
        if verbose: print('1',df_samp.shape)    

        df_cp.where(df_cp[target_bin]!=z, inplace=True)
        df_cp.dropna(inplace=True)
        if verbose: print('2',df_cp.shape)

        df_cp = pd.concat([df_cp, df_samp])
        if verbose: print('3',df_cp.shape)

        if verbose: print()

    if verbose: print('Ending with:', df_cp.shape)    
    
    # Finally remove the dropped rows
    id_list = df_cp.dropna()[identifier].tolist()
    
    return id_list

'''
NOTES

v1: discrete value comparison (a target value is adjusted with neighboring discrete values)
* best modeling error but distribution had gaps

        lo = df_cp[(df_cp[target]==z-bin_width)][target].count()
        sp = df_cp[(df_cp[target]==z)][target].count()
        hi = df_cp[(df_cp[target]==z+bin_width)][target].count()  
        
        and part II with target_bin = target

        
v2: aggregated comparision (a target range is adjusted with neighboring ranges)
* worst modeling error but smoothest distribution
* not sure why this was

        lo = df_cp[(df_cp[target_bin]==z-bin_width)][target].count()
        sp = df_cp[(df_cp[target_bin]==z)][target].count()
        hi = df_cp[(df_cp[target_bin]==z+bin_width)][target].count()      

        and part II with target_bin = target_bin

v3: semi-discrete comparision (only the target value is adjusted with neighboring ranges)
* good compromise: big spikes removed, but not too much

        lo = df_cp[(df_cp[target_bin]==z-bin_width)][target].count()
        sp = df_cp[(df_cp[target]==z)][target].count()
        hi = df_cp[(df_cp[target_bin]==z+bin_width)][target].count() 
        
        and part II with target_bin = target
     
'''