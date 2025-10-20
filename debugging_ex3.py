# Reduce a mess of a bug to minimum working example.

# This script loads and analyzes data from a star tracking camera, which records
# the celestial coodinates and uncertainty of each image.

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


CSV_FILE = 'TIMcam.csv'
TEMP_LIMIT_DEGC = 15.5
EXPTIME_TARGET_SEC = 0.2


def filter_data(df):
    '''Apply conditions to DataFrame to analyze only data of interest'''
    sensor_cooled = df['CCDTEMP'] <= TEMP_LIMIT_DEGC
    well_exposed = df['EXPTIME'] >= EXPTIME_TARGET_SEC
    return df[sensor_cooled & well_exposed]


def report_stats(df):
    '''Report on statistics of the pointing in the data table.'''
    ras = df['RA']
    decs = df['RA']
    print(f'Right ascension limits: {np.min(ras):.6f}, {np.max(ras):.6f}')
    print(f'Declination limits: {np.min(decs):.6f}, {np.max(decs):.6f}')

    rmses = df['RMSE']
    rmse_mean = 0
    for rmse in rmses:
        rmse_mean += rmse
    rmse_mean /= len(rmses)
    print(f'Mean RMSE: {rmse_mean:.2f} arcsec')

    scales = df['SCALE']
    scale_mean = 0
    for scale in scales:
        scale_mean += scale
    scale_mean /= len(scales)
    print(f'Mean plate scale: {scale_mean:.2f} arcsec/pix')
    return rmse_mean, scale_mean


def do_plots(df):
    '''
    Plot the uncertainty history of the images, in arcseconds and camera
    pixels.
    '''
    rmse_mean, scale_mean = report_stats(df)

    fig, ax = plt.subplots(figsize=(7,6), nrows=2, sharex=True)

    ax[0].plot(df['TIMESTAMP'], df['RMSE'], marker='.')
    ax[0].axhline(rmse_mean, linestyle='--')
    ax[0].set_ylabel('Root mean squared error (arcsec)')

    ax[1].plot(df['TIMESTAMP'], df['RMSE'] / scale_mean, marker='.')
    ax[1].set_xlabel('Timestamp (UTC)')
    ax[1].set_ylabel('Root mean squared error (pixels)')

    fig.tight_layout()
    plt.show()


if __name__ == '__main__':
    df = pd.read_csv(CSV_FILE)
    df_filter = filter_data(df)
    do_plots(df_filter)