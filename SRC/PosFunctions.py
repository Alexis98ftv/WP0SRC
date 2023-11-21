## Copyright (C) GNSS ACADEMY 
##
## Name          : PosFunctions.py
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
from interfaces import POS_IDX
sys.path.append(os.getcwd() + '/' + \
    os.path.dirname(sys.argv[0]) + '/' + 'COMMON')
from COMMON import GnssConstants
from COMMON.Plots import generatePlot
import numpy as np
# from pyproj import Transformer
from COMMON.Coordinates import xyz2llh


# Plot the instantaneous number of satellites along the whole day
def plotPosSats(PosData):
    PlotConf = {}

    PlotConf["Type"] = "Lines"
    PlotConf["FigSize"] = (8.4,7.6)
    PlotConf["Title"] = "Residuals C1C vs Time for TLSA"

    PlotConf["xLabel"] = "Hour of DoY 006"
    PlotConf["xTicks"] = range(0, 25)
    PlotConf["xLim"] = [0, 24]
    
    PlotConf["yLabel"] = "Number of satellites"
    PlotConf["yLim"] = [0, 15]

    PlotConf["Grid"] = 1

    PlotConf["Marker"] = '-'
    
    PlotConf["LineWidth"] = 1.5


    PlotConf["xData"] = {}
    PlotConf["yData"] = {}

    Label = 0

    PlotConf["Color"] = {}
    PlotConf["Color"][Label] = "orange"

    PlotConf["xData"][Label] = PosData[POS_IDX["SOD"]] / GnssConstants.S_IN_H
    PlotConf["yData"][Label] = PosData[POS_IDX["NSATS"]]

    PlotConf["Path"] = sys.argv[1] + '/OUT/POS/POS/' + 'POS_SATS_vs_TIME_TLSA_D006Y15.png'

    # Call generatePlot from Plots library
    generatePlot(PlotConf)

# Plot the PDOP, GDOP, TDOP
def plotPosDOP(PosData):
    PlotConf = {}

    PlotConf["Type"] = "Lines"
    PlotConf["FigSize"] = (8.4,7.6)
    PlotConf["Title"] = "Dilution Of Precision (DOP) from TLSA on Year 2015 DoY 006"

    PlotConf["xLabel"] = "Hour of DoY 006"
    PlotConf["xTicks"] = range(0, 25)
    PlotConf["xLim"] = [0, 24]
    
    PlotConf["yLabel"] = "DOP"

    PlotConf["Grid"] = 1

    PlotConf["Marker"] = '-'
    
    PlotConf["LineWidth"] = 1.5

    PlotConf["xData"] = {}
    PlotConf["yData"] = {}
    PlotConf["Color"] = {}
    PlotConf["Legend"] = True
    
    Label = ["GDOP", "PDOP", "TDOP"]
    colors = ["purple", "green", "blue"]
    
    for idx, label in enumerate(Label):
        DOP = PosData[POS_IDX[label]]

        PlotConf["Color"][label] = colors[idx]

        PlotConf["xData"][label] = PosData[POS_IDX["SOD"]] / GnssConstants.S_IN_H
        PlotConf["yData"][label] = DOP

    PlotConf["Path"] = sys.argv[1] + '/OUT/POS/POS/' + 'POS_DOP_vs_TIME_TLSA_D006Y15.png'

    # Call generatePlot from Plots library
    generatePlot(PlotConf)

# Plot the HDOP and VDOP together with the number of satellites
def plotPosHVDOP(PosData):
    PlotConf = {}

    PlotConf["Type"] = "Lines"
    PlotConf["FigSize"] = (8.4,7.6)
    PlotConf["Title"] = "Dilution Of Precision (DOP) with Number of Satellites from TLSA on Year 2015 DoY 006"

    PlotConf["xLabel"] = "Hour of DoY 006"
    PlotConf["xTicks"] = range(0, 25)
    PlotConf["xLim"] = [0, 24]
    
    PlotConf["yLabel"] = "DOP"
    #PlotConf["yLim"] = [0.5, 3.0]

    #PlotConf["zLabel"] = "Number of Satellites"
    #PlotConf["zTicks"] = range(0, 13)
    #PlotConf["zLim"] = [1, 12]

    PlotConf["Grid"] = 1

    PlotConf["Marker"] = '-'
    
    PlotConf["LineWidth"] = 1.5

    PlotConf["xData"] = {}
    PlotConf["yData"] = {}
    PlotConf["zData"] = {}

    PlotConf["Color"] = {}
    PlotConf["Legend"] = True
    
    Label = ["HDOP", "VDOP", "NSATS"]
    colors = ["purple", "green", "orange"]
    
    for idx, label in enumerate(Label):
        DOP = PosData[POS_IDX[label]]

        PlotConf["Color"][label] = colors[idx]

        PlotConf["xData"][label] = PosData[POS_IDX["SOD"]] / GnssConstants.S_IN_H
        PlotConf["yData"][label] = DOP

    PlotConf["zData"][0] = PosData[POS_IDX["NSATS"]]
    PlotConf["Path"] = sys.argv[1] + '/OUT/POS/POS/' + 'POS_HVDOP_vs_TIME_TLSA_D006Y15.png'

    # Call generatePlot from Plots library
    generatePlot(PlotConf)

#Plot  the  East/North/Up  Position  Error  (EPE,  NPE,  UPE)
def plotPosENUPE(PosData):
    PlotConf = {}

    PlotConf["Type"] = "Lines"
    PlotConf["FigSize"] = (8.4,7.6)
    PlotConf["Title"] = "ENU Position Error from TLSA on Year 2015 DoY 006"

    PlotConf["xLabel"] = "Hour of DoY 006"
    PlotConf["xTicks"] = range(0, 25)
    PlotConf["xLim"] = [0, 24]
    
    PlotConf["yLabel"] = "ENU-PE[m]"

    PlotConf["Grid"] = 1

    PlotConf["Marker"] = '-'
    
    PlotConf["LineWidth"] = 1.5

    PlotConf["xData"] = {}
    PlotConf["yData"] = {}
    PlotConf["Color"] = {}
    PlotConf["Legend"] = True

    Label = ["UPE[m]", "EPE[m]", "NPE[m]"]
    colors = ["purple", "green", "blue"]
    

    for idx, label in enumerate(Label):
        DATA = PosData[POS_IDX[label]]

        PlotConf["Color"][label] = colors[idx]

        PlotConf["xData"][label] = PosData[POS_IDX["SOD"]] / GnssConstants.S_IN_H
        PlotConf["yData"][label] = DATA

    PlotConf["Path"] = sys.argv[1] + '/OUT/POS/POS/' + 'POS_ENU_PE_vs_TIME_TLSA_D006Y15.png'

    # Call generatePlot from Plots library
    generatePlot(PlotConf)

#Plot the Horizontal and Vertical Position Error (HPE) and VPE
def plotPosHVPE(PosData):
    PlotConf = {}

    PlotConf["Type"] = "Lines"
    PlotConf["FigSize"] = (8.4,7.6)
    PlotConf["Title"] = "HPE-VPE Position Error from TLSA on Year 2015 DoY 006"

    PlotConf["xLabel"] = "Hour of DoY 006"
    PlotConf["xTicks"] = range(0, 25)
    PlotConf["xLim"] = [0, 24]
    
    PlotConf["yLabel"] = "HVPE[m]"
    #PlotConf["yLim"] = [0, 8]

    PlotConf["Grid"] = 1

    PlotConf["Marker"] = '-'
    
    PlotConf["LineWidth"] = 1.5

    PlotConf["xData"] = {}
    PlotConf["yData"] = {}

    PlotConf["Color"] = {}
    PlotConf["Legend"] = True

    # CALC HPE and VPE
    EPE = PosData[POS_IDX["EPE[m]"]]
    NPE = PosData[POS_IDX["NPE[m]"]]
    UPE = PosData[POS_IDX["UPE[m]"]]

    HPE = np.sqrt(EPE**2+NPE**2)
    VPE = abs(UPE)
    # PLOT confg
    LabelVPE = "VPE"
    LabelHPE = "HPE"
    
    # VPE
    PlotConf["xData"][LabelVPE] = PosData[POS_IDX["SOD"]] / GnssConstants.S_IN_H
    PlotConf["yData"][LabelVPE] = VPE
    PlotConf["Color"][LabelVPE] = "purple"
    # HPE
    PlotConf["xData"][LabelHPE] = PosData[POS_IDX["SOD"]] / GnssConstants.S_IN_H
    PlotConf["yData"][LabelHPE] = HPE
    PlotConf["Color"][LabelHPE] = "green"

    PlotConf["Path"] = sys.argv[1] + '/OUT/POS/POS/' + 'POS_HVPE_vs_TIME_TLSA_D006Y15.png'

    # Call generatePlot from Plots library
    generatePlot(PlotConf)

#Plot Horizontal Scatter plot with NPE vs. EPE (North Position Error
def plotPosNPEEPE(PosData):
    PlotConf = {}

    PlotConf["Type"] = "Lines"
    PlotConf["FigSize"] = (8.4,7.6)
    PlotConf["Title"] = "EPE vs NPE from TLSA on Year 2015 DoY 006"

    PlotConf["xLabel"] = "EPE[m]"

    PlotConf["yLabel"] = "NPE[m]"

    PlotConf["ColorBar"] = "gnuplot"
    PlotConf["ColorBarLabel"] = "HDOP"
    PlotConf["ColorBarMin"] = 0.6
    PlotConf["ColorBarMax"] = 2.2

    PlotConf["Grid"] = 1

    PlotConf["Marker"] = '.'
    
    PlotConf["LineWidth"] = 1.5

    PlotConf["xData"] = {}
    PlotConf["yData"] = {}
    PlotConf["zData"] = {}

    Label = "label"

    PlotConf["xData"][Label] = PosData[POS_IDX["EPE[m]"]]
    PlotConf["yData"][Label] = PosData[POS_IDX["NPE[m]"]]
    PlotConf["zData"][Label] = PosData[POS_IDX["HDOP"]]

    PlotConf["Path"] = sys.argv[1] + '/OUT/POS/POS/' + 'POS_NPE_vs_EPE_TLSA_D006Y15.png'

    # Call generatePlot from Plots library
    generatePlot(PlotConf)