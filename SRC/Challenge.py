## Copyright (C) GNSS ACADEMY 
##
## Name          : Challenge.py
## Purpose       : CHALLENGE WP0
## Project       : WP0-JSNP
## Component     : 
## Author        : Alexis
## Creation date : 2023
## File Version  : 1.0
## Version date  : 
##


import sys, os
from pandas import unique
from interfaces import LOS_IDX
sys.path.append(os.getcwd() + '/' + \
    os.path.dirname(sys.argv[0]) + '/' + 'COMMON')
from COMMON.Plots import generatePlot
import numpy as np

# # Plot Satellite Polar VIEW
def plotSatPolarView(LosData):
    PlotConf = {}

    PlotConf["Type"] = "Lines"

    PlotConf["Title"] = "Satellite Polar View from TLSA on Year 2015"\
        " DoY 006"

    PlotConf["Grid"] = 1

    PlotConf["Marker"] = '.'
    PlotConf["LineWidth"] = 1.5

#-----------------------------------------------------------------------
# CODE START
#-----------------------------------------------------------------------
    PlotConf["FigSize"] = (8.4,7.6) 

    azim = LosData[LOS_IDX["AZIM"]]
    elev = LosData[LOS_IDX["ELEV"]]
    
    theta_azim_rad = np.radians(azim)
    # To plot the high elevation in the center of polar view (0)
    r_elev = 90 - elev

    PlotConf["Polar"] = True
    '''
    Se podría pasar por PlotConf los parametros de:
    ax.set_rlim()
    ax.set_thetagrid()
    ax.set_rgrids()
    '''
#-----------------------------------------------------------------------
# CODE FINISH
#-----------------------------------------------------------------------
    Ticks1range = list(range(1,8))
    Ticks2range = list(range(9,26))
    Ticks3range = list(range(27,33))
    ColorBarTicks = Ticks1range + Ticks2range + Ticks3range

    PlotConf["ColorBar"] = "gnuplot"
    PlotConf["ColorBarLabel"] = "GPS-PRN"
    PlotConf["ColorBarTicks"] = ColorBarTicks
    
    PlotConf["xData"] = {}
    PlotConf["yData"] = {}
    PlotConf["zData"] = {}
    Label = 0
    PlotConf["xData"][Label] = theta_azim_rad
    PlotConf["yData"][Label] = r_elev
    PlotConf["zData"][Label] = LosData[LOS_IDX["PRN"]]

    PlotConf["Path"] = sys.argv[1] + '/OUT/CHALLENGE/' + 'SAT_POLAR_VIEW_TLSA_D006Y15.png'

    # Call generatePlot from Plots library
    generatePlot(PlotConf)
