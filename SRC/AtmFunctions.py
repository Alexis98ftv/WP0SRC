## Copyright (C) GNSS ACADEMY 
##
## Name          : AtmFunctions.py
## Purpose       : Satellite Analyses functions
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
from COMMON import GnssConstants
from COMMON.Plots import generatePlot
import numpy as np
# from pyproj import Transformer
from COMMON.Coordinates import xyz2llh


# Plot of slant ionospheric delays (STEC in meters) Figure
def plotIonSTECvsTime(LosData):
    PlotConf = {}

    PlotConf["Type"] = "Lines"
    PlotConf["FigSize"] = (8.4,7.6)
    PlotConf["Title"] = "Ionospheric Klobuchar Delays (STEC) from TLSA on Year 2015"\
        " DoY 006"

    PlotConf["xLabel"] = "Hour of DoY 006"
    PlotConf["xTicks"] = range(0, 25)
    PlotConf["xLim"] = [0, 24]
    
    
    PlotConf["yLabel"] = "STEC[m]"

    PlotConf["Grid"] = 1

    PlotConf["Marker"] = '.'
    PlotConf["LineWidth"] = 1.5

    PlotConf["ColorBar"] = "gnuplot"
    PlotConf["ColorBarLabel"] = "Elevation [deg]"
    PlotConf["ColorBarMin"] = 0.
    PlotConf["ColorBarMax"] = 90.

    PlotConf["xData"] = {}
    PlotConf["yData"] = {}
    PlotConf["zData"] = {}
    Label = 0
    PlotConf["xData"][Label] = LosData[LOS_IDX["SOD"]] / GnssConstants.S_IN_H
    PlotConf["yData"][Label] = LosData[LOS_IDX["STEC[m]"]]
    PlotConf["zData"][Label] = LosData[LOS_IDX["ELEV"]]

    PlotConf["Path"] = sys.argv[1] + '/OUT/LOS/ION/' + 'IONO_STEC_vs_TIME_TLSA_D006Y15.png'

    # Call generatePlot from Plots library
    generatePlot(PlotConf)

# Plot of slant ionospheric delays (STEC in meters) Figure
def plotIonSTECvsPRN(LosData):
    PlotConf = {}

    PlotConf["Type"] = "Lines"
    PlotConf["FigSize"] = (8.4,7.6)
    PlotConf["Title"] = "Satellite Visibility vs STEC from TLSA on Year 2015"\
        " DoY 006"

    PlotConf["xLabel"] = "Hour of DoY 006"
    PlotConf["xTicks"] = range(0, 25)
    PlotConf["xLim"] = [0, 24]
    
    PlotConf["yLabel"] = "GPS-PRN"
    PlotConf["yTicks"] = range(1, 33)
    PlotConf["yLim"] = [0, 33]

    PlotConf["Grid"] = 1

    PlotConf["Marker"] = '.'
    PlotConf["LineWidth"] = 10

    PlotConf["ColorBar"] = "gnuplot"
    PlotConf["ColorBarLabel"] = "STEC [m]"

    PlotConf["xData"] = {}
    PlotConf["yData"] = {}
    PlotConf["zData"] = {}
    Label = 0
    PlotConf["xData"][Label] = LosData[LOS_IDX["SOD"]] / GnssConstants.S_IN_H
    PlotConf["yData"][Label] = LosData[LOS_IDX["PRN"]]
    PlotConf["zData"][Label] = LosData[LOS_IDX["STEC[m]"]]

    PlotConf["Path"] = sys.argv[1] + '/OUT/LOS/ION/' + 'IONO_STEC_vs_PRN_TLSA_D006Y15.png'

    # Call generatePlot from Plots library
    generatePlot(PlotConf)

# Plot VTEC in meters from STEC Figure
def plotIonVTECvsTime(LosData):
    PlotConf = {}

    PlotConf["Type"] = "Lines"
    PlotConf["FigSize"] = (8.4,7.6)
    PlotConf["Title"] = "Ionospheric Klobuchar Delays (VTEC) from TLSA on Year 2015"\
        " DoY 006"

    PlotConf["xLabel"] = "Hour of DoY 006"
    PlotConf["xTicks"] = range(0, 25)
    PlotConf["xLim"] = [0, 24]
    
    PlotConf["yLabel"] = "VTEC[m]"
    # VTEC PROCESS
    #VTEC = LosData[LOS_IDX["VTEC[m]"]]
    #MAPP = LosData[LOS_IDX["MPP[elev]"]]
    h = GnssConstants.Height_IONO_layer_km * GnssConstants.M_IN_KM
    Re = GnssConstants.Earth_R_km * GnssConstants.M_IN_KM
    
    STEC = LosData[LOS_IDX["STEC[m]"]]
    elev_rad = (np.array(LosData[LOS_IDX["ELEV"]]) * np.pi) / 180

    mapp_calc = np.array((1 - (Re/(Re+h) * np.cos(elev_rad))**2) ** (-1/2))

    VTEC_calc = STEC / mapp_calc

    PlotConf["Grid"] = 1

    PlotConf["Marker"] = '.'
    PlotConf["LineWidth"] = 1.5

    PlotConf["ColorBar"] = "gnuplot"
    PlotConf["ColorBarLabel"] = "Elevation [deg]"
    PlotConf["ColorBarMin"] = 0.
    PlotConf["ColorBarMax"] = 90.

    PlotConf["xData"] = {}
    PlotConf["yData"] = {}
    PlotConf["zData"] = {}
    Label = 0
    PlotConf["xData"][Label] = LosData[LOS_IDX["SOD"]] / GnssConstants.S_IN_H
    PlotConf["yData"][Label] = VTEC_calc
    PlotConf["zData"][Label] = LosData[LOS_IDX["ELEV"]]

    PlotConf["Path"] = sys.argv[1] + '/OUT/LOS/ION/' + 'IONO_VTEC_vs_TIME_TLSA_D006Y15.png'

    # Call generatePlot from Plots library
    generatePlot(PlotConf)

# Plot the satellite visibility periods using VTEC
def plotIonVTECvsPRN(LosData):
    PlotConf = {}

    PlotConf["Type"] = "Lines"
    PlotConf["FigSize"] = (8.4,7.6)
    PlotConf["Title"] = "Satellite Visibility vs VTEC from TLSA on Year 2015"\
        " DoY 006"

    PlotConf["xLabel"] = "Hour of DoY 006"
    PlotConf["xTicks"] = range(0, 25)
    PlotConf["xLim"] = [0, 24]
    
    PlotConf["yLabel"] = "GPS-PRN"
    PlotConf["yTicks"] = range(1, 33)
    PlotConf["yLim"] = [0, 33]

    PlotConf["Grid"] = 1

    PlotConf["Marker"] = '.'
    PlotConf["LineWidth"] = 10

    PlotConf["ColorBar"] = "gnuplot"
    PlotConf["ColorBarLabel"] = "VTEC[m]"

    PlotConf["xData"] = {}
    PlotConf["yData"] = {}
    PlotConf["zData"] = {}
    Label = 0
    PlotConf["xData"][Label] = LosData[LOS_IDX["SOD"]] / GnssConstants.S_IN_H
    PlotConf["yData"][Label] = LosData[LOS_IDX["PRN"]]
    PlotConf["zData"][Label] = LosData[LOS_IDX["VTEC[m]"]]

    PlotConf["Path"] = sys.argv[1] + '/OUT/LOS/ION/' + 'IONO_VTEC_vs_PRN_TLSA_D006Y15.png'

    # Call generatePlot from Plots library
    generatePlot(PlotConf)

# Plot of STD (Slant Tropospheric Delay)
def plotTropoSTD(LosData):
    PlotConf = {}

    PlotConf["Type"] = "Lines"
    PlotConf["FigSize"] = (8.4,7.6)
    PlotConf["Title"] = "Slant Tropospheric Delay (STD) in meters from TLSA on Year 2015"\
        " DoY 006"

    PlotConf["xLabel"] = "Hour of DoY 006"
    PlotConf["xTicks"] = range(0, 25)
    PlotConf["xLim"] = [0, 24]
    
    PlotConf["yLabel"] = "STD[m]"

    PlotConf["Grid"] = 1

    PlotConf["Marker"] = '.'
    PlotConf["LineWidth"] = 1.5

    PlotConf["ColorBar"] = "gnuplot"
    PlotConf["ColorBarLabel"] = "Elevation [deg]"
    PlotConf["ColorBarMin"] = 0.
    PlotConf["ColorBarMax"] = 90.

    PlotConf["xData"] = {}
    PlotConf["yData"] = {}
    PlotConf["zData"] = {}
    Label = 0
    PlotConf["xData"][Label] = LosData[LOS_IDX["SOD"]] / GnssConstants.S_IN_H
    PlotConf["yData"][Label] = LosData[LOS_IDX["TROPO[m]"]]
    PlotConf["zData"][Label] = LosData[LOS_IDX["ELEV"]]

    PlotConf["Path"] = sys.argv[1] + '/OUT/LOS/TRO/' + 'TROPO_STD_vs_TIME_TLSA_D006Y15.png'

    # Call generatePlot from Plots library
    generatePlot(PlotConf)

# Plot of STD (Slant Tropospheric Delay)
def plotTropoZTD(LosData):
    PlotConf = {}

    PlotConf["Type"] = "Lines"
    PlotConf["FigSize"] = (8.4,7.6)
    PlotConf["Title"] = "Zenith Tropospheric Delays (ZTD) from TLSA on Year 2015"\
        " DoY 006"

    PlotConf["xLabel"] = "Hour of DoY 006"
    PlotConf["xTicks"] = range(0, 25)
    PlotConf["xLim"] = [0, 24]
    
    PlotConf["yLabel"] = "ZTD[m]"
    PlotConf["yLim"] = [2.3150, 2.3180]
    # ZTD calc
    STD = np.array(LosData[LOS_IDX["TROPO[m]"]])
    
    elev_rad = (np.array(LosData[LOS_IDX["ELEV"]]) * np.pi) / 180
    mpp_calc = np.array(1.001/np.sqrt(0.002001 + np.sin(elev_rad)**2))

    ZTD = STD/mpp_calc
    
    PlotConf["Grid"] = 1

    PlotConf["Marker"] = '.'
    PlotConf["LineWidth"] = 1.5

    PlotConf["ColorBar"] = "gnuplot"
    PlotConf["ColorBarLabel"] = "Elevation [deg]"
    PlotConf["ColorBarMin"] = 0.
    PlotConf["ColorBarMax"] = 90.

    PlotConf["xData"] = {}
    PlotConf["yData"] = {}
    PlotConf["zData"] = {}
    Label = 0
    PlotConf["xData"][Label] = LosData[LOS_IDX["SOD"]] / GnssConstants.S_IN_H
    PlotConf["yData"][Label] = ZTD
    PlotConf["zData"][Label] = LosData[LOS_IDX["ELEV"]]

    PlotConf["Path"] = sys.argv[1] + '/OUT/LOS/TRO/' + 'TROPO_ZTD_vs_TIME_TLSA_D006Y15.png'

    # Call generatePlot from Plots library
    generatePlot(PlotConf)
