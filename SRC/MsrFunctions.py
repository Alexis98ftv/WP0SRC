## Copyright (C) GNSS ACADEMY 
##
## Name          : MsrFunctions.py
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


# Plot Pseudo-ranges (Code Measurements C1) for all satellites
def plotMsrCODES(LosData):
    PlotConf = {}

    PlotConf["Type"] = "Lines"
    PlotConf["FigSize"] = (8.4,7.6)
    PlotConf["Title"] = "Pseudo-range C1C vs TIME for TLSA"

    PlotConf["xLabel"] = "Hour of DoY 006"
    PlotConf["xTicks"] = range(0, 25)
    PlotConf["xLim"] = [0, 24]
    
    PlotConf["yLabel"] = "Pseudo-range[km]"
    
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
    PlotConf["yData"][Label] = LosData[LOS_IDX["MEAS[m]"]] / GnssConstants.M_IN_KM
    PlotConf["zData"][Label] = LosData[LOS_IDX["ELEV"]]

    PlotConf["Path"] = sys.argv[1] + '/OUT/LOS/MSR/' + 'MEAS_CODES_vs_TIME_TLSA_D006Y15.png'

    # Call generatePlot from Plots library
    generatePlot(PlotConf)

# Plot Tau = C1C/c for all satellites
def plotMsrTAU(LosData):
    PlotConf = {}

    PlotConf["Type"] = "Lines"
    PlotConf["FigSize"] = (8.4,7.6)
    PlotConf["Title"] = "Tau=Rho/c from TLSA on Year 2015 Doy 006"

    PlotConf["xLabel"] = "Hour of DoY 006"
    PlotConf["xTicks"] = range(0, 25)
    PlotConf["xLim"] = [0, 24]
    
    PlotConf["yLabel"] = "Tau [ms]"
    
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
    PlotConf["yData"][Label] = (LosData[LOS_IDX["MEAS[m]"]] / GnssConstants.LIGHT_SPEED_M_S) * GnssConstants.MS_IN_S
    PlotConf["zData"][Label] = LosData[LOS_IDX["ELEV"]]

    PlotConf["Path"] = sys.argv[1] + '/OUT/LOS/MSR/' + 'TAU_vs_TIME_TLSA_D006Y15.png'

    # Call generatePlot from Plots library
    generatePlot(PlotConf)

# Plot Time of Flight (ToF) for all satellites
def plotMsrToF(LosData):
    PlotConf = {}

    PlotConf["Type"] = "Lines"
    PlotConf["FigSize"] = (8.4,7.6)
    PlotConf["Title"] = "Time of Flight (ToF) from TLSA on Year 2015 Doy 006"

    PlotConf["xLabel"] = "Hour of DoY 006"
    PlotConf["xTicks"] = range(0, 25)
    PlotConf["xLim"] = [0, 24]
    
    PlotConf["yLabel"] = "ToF [ms]"
    
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
    PlotConf["yData"][Label] = LosData[LOS_IDX["TOF[ms]"]]
    PlotConf["zData"][Label] = LosData[LOS_IDX["ELEV"]]

    PlotConf["Path"] = sys.argv[1] + '/OUT/LOS/MSR/' + 'TOF_vs_TIME_TLSA_D006Y15.png'

    # Call generatePlot from Plots library
    generatePlot(PlotConf)

# Plot the Doppler Frequency in KHz
def plotMsrDOP(LosData):
    PlotConf = {}

    PlotConf["Type"] = "Lines"
    PlotConf["FigSize"] = (8.4,7.6)
    PlotConf["Title"] = "Doppler Frequency from TLSA on Year 2015 Doy 006"

    PlotConf["xLabel"] = "Hour of DoY 006"
    PlotConf["xTicks"] = range(0, 25)
    PlotConf["xLim"] = [0, 24]
    
    PlotConf["yLabel"] = "Doppler Frequency [KHz]"

    # Doppler Frequency
    def doppler_frequency(vLOS):
        return - (vLOS/GnssConstants.LIGHT_SPEED_M_S) * GnssConstants.FREQ_L1_MHz * GnssConstants.KHz_IN_MHz
    
    # rLOS
    rx = LosData[LOS_IDX["SAT-X[m]"]] - GnssConstants.WGS84_REF_X
    ry = LosData[LOS_IDX["SAT-Y[m]"]] - GnssConstants.WGS84_REF_Y
    rz = LosData[LOS_IDX["SAT-Z[m]"]] - GnssConstants.WGS84_REF_Z
    rLOS = np.array([rx, ry, rz])

    # SAT velocity
    vSATX = LosData[LOS_IDX["VEL-X[m/s]"]]
    vSATY = LosData[LOS_IDX["VEL-Y[m/s]"]]
    vSATZ = LosData[LOS_IDX["VEL-Z[m/s]"]]
    vSAT = np.array([vSATX, vSATY, vSATZ])

    # Calc uLOS(unitary vector) and vLOS(velocity in uLOS direction)
    uLOS = rLOS / np.linalg.norm(rLOS, axis = 0)

    vLOS = uLOS * vSAT
    vLOS = np.sum(vLOS, axis=0)
    
    # CALL Doppler Function with vLOS
    fD = doppler_frequency(vLOS)

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
    PlotConf["yData"][Label] = fD
    PlotConf["zData"][Label] = LosData[LOS_IDX["ELEV"]]

    PlotConf["Path"] = sys.argv[1] + '/OUT/LOS/MSR/' + 'DOPPLER_FREQ_vs_TIME_TLSA_D006Y15.png'

    # Call generatePlot from Plots library
    generatePlot(PlotConf)

# Build and Plot the PVT filter residuals
def plotMsrResiduals(LosData):
    PlotConf = {}

    PlotConf["Type"] = "Lines"
    PlotConf["FigSize"] = (8.4,7.6)
    PlotConf["Title"] = "Residuals C1C vs Time for TLSA"

    PlotConf["xLabel"] = "Hour of DoY 006"
    PlotConf["xTicks"] = range(0, 25)
    PlotConf["xLim"] = [0, 24]
    
    PlotConf["yLabel"] = "Residuals [Km]"
    PlotConf["yLim"] = [2522.250, 2522.280]
    
    # Correct CLK process (Mono-Freq clock): CLK_P1 = CLK_P1P2 - TGD + DTR
    CLK_P1P2 = np.array(LosData[LOS_IDX["SV-CLK[m]"]])
    TGD = np.array(LosData[LOS_IDX["TGD[m]"]])
    DTR = np.array(LosData[LOS_IDX["DTR[m]"]])
    
    CLK_P1 = np.array(CLK_P1P2-TGD+DTR)

    # Build Residuals for Code Measurements C1
    PSR_C1 = np.array(LosData[LOS_IDX["MEAS[m]"]])
    RGE = np.array(LosData[LOS_IDX["RANGE[m]"]])
    IONO = np.array(LosData[LOS_IDX["STEC[m]"]])
    TROPO = np.array(LosData[LOS_IDX["TROPO[m]"]])

    # in meters
    RES_C1 = PSR_C1 - (RGE - CLK_P1 + IONO + TROPO)

    PlotConf["Grid"] = 1

    PlotConf["Marker"] = '.'
    PlotConf["LineWidth"] = 1.5

    PlotConf["ColorBar"] = "gnuplot"
    PlotConf["ColorBarLabel"] = "GPS-PRN"

    PlotConf["xData"] = {}
    PlotConf["yData"] = {}
    PlotConf["zData"] = {}
    Label = 0
    PlotConf["xData"][Label] = LosData[LOS_IDX["SOD"]] / GnssConstants.S_IN_H
    PlotConf["yData"][Label] = RES_C1 / GnssConstants.M_IN_KM
    PlotConf["zData"][Label] = LosData[LOS_IDX["PRN"]]

    PlotConf["Path"] = sys.argv[1] + '/OUT/LOS/MSR/' + 'MEAS_RESIDUALS_vs_TIME_TLSA_D006Y15.png'

    # Call generatePlot from Plots library
    generatePlot(PlotConf)



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
    #Lable = "GDOP"
    #for Label in ["",""]:
    #plt.legend

    PlotConf["Color"] = {}
    PlotConf["Color"][Label] = "yellow"

    PlotConf["xData"][Label] = PosData[POS_IDX["SOD"]] / GnssConstants.S_IN_H
    PlotConf["yData"][Label] = PosData[POS_IDX["NSATS"]]

    PlotConf["Path"] = sys.argv[1] + '/OUT/POS/POS/' + 'POS_SATS_vs_TIME_TLSA_D006Y15.png'

    # Call generatePlot from Plots library
    generatePlot(PlotConf)

