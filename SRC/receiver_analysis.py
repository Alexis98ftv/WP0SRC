#!/usr/bin/env python

## Copyright (C) GNSS ACADEMY 
##
## Name          : receiver_analysis.py
## Purpose       : WP0 Takss: Plot Receiver SPP Analyses
## Project       : WP0-JSNP
## Component     : 
## Author        : GNSS Academy - Alexis
## Creation date : 2021
## File Version  : 1.0
##

import sys, os

# Add path to find all modules
Common = os.path.dirname(os.path.dirname(
    os.path.abspath(sys.argv[0]))) + '/COMMON'
sys.path.insert(0, Common)

from collections import OrderedDict
from interfaces import LOS_IDX
from interfaces import POS_IDX
from pandas import read_csv
from yaml import dump
import SatFunctions
import AtmFunctions
import MsrFunctions
import PosFunctions

#######################################################
# INTERNAL FUNCTIONS 
#######################################################

def displayUsage():
    sys.stderr.write("ERROR: Please provide path to SCENARIO as a unique \nargument\n")

def readConf(CfgFile):
    Conf = OrderedDict({})
    with open(CfgFile, 'r') as f:
        # Read file
        Lines = f.readlines()

        # Read each configuration parameter which is compound of a key and a value
        for Line in Lines:
            if "#" in Line or Line.isspace(): continue
            LineSplit = Line.split('=')
            try:
                LineSplit = list(filter(None, LineSplit))
                Conf[LineSplit[0].strip()] = LineSplit[1].strip()

            except:
                sys.stderr.write("ERROR: Bad line in conf: %s\n" % Line)

    return Conf

#######################################################
# MAIN PROCESSING
#######################################################

print( '-----------------------------')
print( 'RUNNING RECEIVER ANALYSES ...')
print( '-----------------------------')

if len(sys.argv) != 2:
    displayUsage()
    sys.exit()

# Take the arguments
Scen = sys.argv[1]

# Path to conf
CfgFile = Scen + '/CFG/receiver_analysis.cfg'

# Read conf file
Conf = readConf(CfgFile)

# Print 
print('Reading Configuration file',CfgFile)

#print(dump(Conf))

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#>>>>> LOS FILE ANALYSES
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Get LOS file full path
LosFile = Scen + '/OUT/LOS/' + Conf["LOS_FILE"]

#-----------------------------------------------------------------------
# PLOT SATELLITE ANALYSES
#-----------------------------------------------------------------------

# Plot Satellite Visibility figures
if(Conf["PLOT_SATVIS"] == '1'):
    # Read the cols we need from LOS file
    LosData = read_csv(LosFile, delim_whitespace=True, skiprows=1, header=None,\
    usecols=[LOS_IDX["SOD"],LOS_IDX["PRN"],LOS_IDX["ELEV"]])
    
    print( 'Plot Satellite Visibility Periods ...')

    # Configure plot and call plot generation function
    SatFunctions.plotSatVisibility(LosData)

# Plot Satellite Geometrical Ranges figures
if(Conf["PLOT_SATRNG"] == '1'):
    # Read the cols we need from LOS file
    LosData = read_csv(LosFile, delim_whitespace=True, skiprows=1, header=None,\
    usecols=[LOS_IDX["SOD"],LOS_IDX["RANGE[m]"],LOS_IDX["ELEV"]])

    print( 'Plot Satellite Geometrical Ranges ...')
    
    # Configure plot and call plot generation function
    SatFunctions.plotSatGeomRnge(LosData)

# Plot Satellite Tracks figures
if(Conf["PLOT_SATTRK"] == '1'):
    # Read the cols we need from LOS file
    LosData = read_csv(LosFile, delim_whitespace=True, skiprows=1, header=None,\
    usecols=[LOS_IDX["SOD"],
    LOS_IDX["SAT-X[m]"],
    LOS_IDX["SAT-Y[m]"],
    LOS_IDX["SAT-Z[m]"],
    LOS_IDX["ELEV"]])
    
    print( 'Plot Satellite Tracks ...')

    # Configure plot and call plot generation function
    SatFunctions.plotSatTracks(LosData)

# Plot Satellite Velocity figures
if(Conf["PLOT_SATVEL"] == '1'):
    # Read the cols we need from LOS file
    LosData = read_csv(LosFile, delim_whitespace=True, skiprows=1, header=None,\
    usecols=[LOS_IDX["SOD"],
    LOS_IDX["VEL-X[m/s]"],
    LOS_IDX["VEL-Y[m/s]"],
    LOS_IDX["VEL-Z[m/s]"],
    LOS_IDX["ELEV"]])
    
    print( 'Plot Satellite Velocity ...')

    # Configure plot and call plot generation function
    SatFunctions.plotSatVelocity(LosData)

# Plot Satellite clock from NAV message of all the PRNs figures
if(Conf["PLOT_SATCLK_PRN"] == '1'):
    # Read the cols we need from LOS file
    LosData = read_csv(LosFile, delim_whitespace=True, skiprows=1, header=None,\
    usecols=[LOS_IDX["SOD"], 
    LOS_IDX["PRN"],
    LOS_IDX["SV-CLK[m]"]])
    
    print( 'Plot Satellite Clocks for each PRNs ...')

    # Configure plot and call plot generation function
    SatFunctions.plotClkNAV(LosData)
    SatFunctions.plotSatCLK_PRN_NAV(LosData)

# Plot the Satellite clock corrected by the relativistic /
# effect and the TGD for a mono-frequency user
if(Conf["PLOT_SATCLK"] == '1'):
    # Read the cols we need from LOS file
    LosData = read_csv(LosFile, delim_whitespace=True, skiprows=1, header=None,\
    usecols=[LOS_IDX["SOD"], 
    LOS_IDX["PRN"],
    LOS_IDX["SV-CLK[m]"],
    LOS_IDX["DTR[m]"],
    LOS_IDX["TGD[m]"]])
    
    print( 'Plot Satellite Clocks corrected ...')
    
    # Configure plot and call plot generation function
    SatFunctions.plotSatClkCorrected(LosData)

# Plot the Satellite clock Total or Timing Group /
# Delay P1P2 for all satellites
if(Conf["PLOT_SATTGD"] == '1'):
    # Read the cols we need from LOS file
    LosData = read_csv(LosFile, delim_whitespace=True, skiprows=1, header=None,\
    usecols=[LOS_IDX["SOD"], 
    LOS_IDX["PRN"],
    LOS_IDX["TGD[m]"]])
    
    print( 'Plot Satellite clock Total ...')
    
    # Configure plot and call plot generation function
    SatFunctions.plotSatTGD(LosData)

# Plot the Satellite clock relativistic effect (DTR)
if(Conf["PLOT_SATDTR"] == '1'):
    # Read the cols we need from LOS file
    LosData = read_csv(LosFile, delim_whitespace=True, skiprows=1, header=None,\
    usecols=[LOS_IDX["SOD"], 
    LOS_IDX["ELEV"],
    LOS_IDX["DTR[m]"]])
    
    print( 'Plot Satellite clock relativistic effect (DTR) ...')
    
    # Configure plot and call plot generation function
    SatFunctions.plotSatDTR(LosData)
    SatFunctions.plotSatDTR(LosData)


#-----------------------------------------------------------------------
# PLOT IONOSPHERE ANALYSES
#-----------------------------------------------------------------------

# Plot of slant ionospheric delays (STEC in meters) from Klobuchar
# model for all satellites as a function of the hour of the day
if(Conf["PLOT_ION_STEC_TIME"] == '1'):
    # Read the cols we need from LOS file
    LosData = read_csv(LosFile, delim_whitespace=True, skiprows=1, header=None,\
    usecols=[LOS_IDX["SOD"], 
    LOS_IDX["ELEV"],
    LOS_IDX["STEC[m]"]])
    
    print( 'Plot of slant ionospheric delays (STEC in meters) ...')
    
    # Configure plot and call plot generation function
    AtmFunctions.plotIonSTECvsTime(LosData)


# Plot the satellite visibility periods  using
# STEC value as part of the color bar in order to see the STEC
# dependency during the satellite visibility pass.
if(Conf["PLOT_ION_STEC_PRN"] == '1'):
    # Read the cols we need from LOS file
    LosData = read_csv(LosFile, delim_whitespace=True, skiprows=1, header=None,\
    usecols=[LOS_IDX["SOD"], 
    LOS_IDX["PRN"],
    LOS_IDX["STEC[m]"]])
    
    print( 'Plot the satellite visibility periods (STEC depency) ...')
    
    # Configure plot and call plot generation function
    AtmFunctions.plotIonSTECvsPRN(LosData)

# Compute and plot VTEC in meters from STEC
# and the Klobuchar mapping function elevation dependent
# All satellites as a function of the hour of the day
if(Conf["PLOT_ION_VTEC_TIME"] == '1'):
    # Read the cols we need from LOS file
    LosData = read_csv(LosFile, delim_whitespace=True, skiprows=1, header=None,\
    usecols=[LOS_IDX["SOD"], 
    LOS_IDX["ELEV"],
    LOS_IDX["STEC[m]"],
    LOS_IDX["MPP[elev]"],
    LOS_IDX["VTEC[m]"]])
    
    print( 'Plot VTEC in meters from STEC ...')
    
    # Configure plot and call plot generation function
    AtmFunctions.plotIonVTECvsTime(LosData)

# Plot the satellite visibility periods using
# VTEC value as part of the color bar in order to see the effect of the
# Sun Activity on the VTEC during the day.
if(Conf["PLOT_ION_VTEC_PRN"] == '1'):
    # Read the cols we need from LOS file
    LosData = read_csv(LosFile, delim_whitespace=True, skiprows=1, header=None,\
    usecols=[LOS_IDX["SOD"], 
    LOS_IDX["PRN"],
    LOS_IDX["VTEC[m]"]])
    
    print( 'Plot the satellite visibility periods using VTEC value ...')
    
    # Configure plot and call plot generation function
    AtmFunctions.plotIonVTECvsPRN(LosData)

#-----------------------------------------------------------------------
# PLOT TROPOSPHERE ANALYSES
#-----------------------------------------------------------------------

# Plot of STD (Slant Tropospheric Delay) in meters from Tropo model
# for all satellites as a function of the hour of the day.
if(Conf["PLOT_TROPO_STD"] == '1'):
    # Read the cols we need from LOS file
    LosData = read_csv(LosFile, delim_whitespace=True, skiprows=1, header=None,\
    usecols=[LOS_IDX["SOD"], 
    LOS_IDX["ELEV"],
    LOS_IDX["TROPO[m]"]])
    
    print( 'Plot of STD (Slant Tropospheric Delay) ...')
    
    # Configure plot and call plot generation function
    AtmFunctions.plotTropoSTD(LosData)

# Compute the Zenith Tropo Delay (ZTD) by dividing the Slant Tropo
# Delay by the Tropo mapping function
if(Conf["PLOT_TROPO_ZTD"] == '1'):
    # Read the cols we need from LOS file
    LosData = read_csv(LosFile, delim_whitespace=True, skiprows=1, header=None,\
    usecols=[LOS_IDX["SOD"], 
    LOS_IDX["ELEV"],
    LOS_IDX["TROPO[m]"],
    LOS_IDX["MPP[elev]"]])
    
    print( 'Compute the Zenith Tropo Delay (ZTD) ...')
    
    # Configure plot and call plot generation function
    AtmFunctions.plotTropoZTD(LosData)


#-----------------------------------------------------------------------
# PLOT MEASUREMENTS ANALYSES
#-----------------------------------------------------------------------

# Plot Pseudo-ranges (Code Measurements C1) for all satellites as a
# function of the hour of the day.
if(Conf["PLOT_MSR_COD"] == '1'):
    # Read the cols we need from LOS file
    LosData = read_csv(LosFile, delim_whitespace=True, skiprows=1, header=None,\
    usecols=[LOS_IDX["SOD"], 
    LOS_IDX["ELEV"],
    LOS_IDX["MEAS[m]"]])
    
    print( 'Plot Pseudo-ranges (Code Measurements C1) for all satellites ...')
    
    # Configure plot and call plot generation function
    MsrFunctions.plotMsrCODES(LosData)

# Plot Tau = C1C/c for all satellites 
# as a function of the hour of the day
if(Conf["PLOT_MSR_TAU"] == '1'):
    # Read the cols we need from LOS file
    LosData = read_csv(LosFile, delim_whitespace=True, skiprows=1, header=None,\
    usecols=[LOS_IDX["SOD"], 
    LOS_IDX["ELEV"],
    LOS_IDX["MEAS[m]"]])
    
    print( 'Plot Tau ...')
    
    # Configure plot and call plot generation function
    MsrFunctions.plotMsrTAU(LosData)

# Plot Time of Flight (ToF) for all satellites as a function 
# of the hour of the day
if(Conf["PLOT_MSR_TOF"] == '1'):
    # Read the cols we need from LOS file
    LosData = read_csv(LosFile, delim_whitespace=True, skiprows=1, header=None,\
    usecols=[LOS_IDX["SOD"], 
    LOS_IDX["ELEV"],
    LOS_IDX["TOF[ms]"]])
    
    print( 'Plot ToF ...')
    
    # Configure plot and call plot generation function
    MsrFunctions.plotMsrToF(LosData)

# Build and Plot the Doppler Frequency in KHz 
if(Conf["PLOT_MSR_DOP"] == '1'):
    # Read the cols we need from LOS file
    LosData = read_csv(LosFile, delim_whitespace=True, skiprows=1, header=None,\
    usecols=[LOS_IDX["SOD"], 
    LOS_IDX["ELEV"],
    LOS_IDX["VEL-X[m/s]"],
    LOS_IDX["VEL-Y[m/s]"],
    LOS_IDX["VEL-Z[m/s]"],
    LOS_IDX["SAT-X[m]"],
    LOS_IDX["SAT-Y[m]"],
    LOS_IDX["SAT-Z[m]"]])
    
    print( 'Plot the Doppler Frequency in KHz ...')
    
    # Configure plot and call plot generation function
    MsrFunctions.plotMsrDOP(LosData)

# Build and Plot the PVT filter residuals by correcting the code
# measurements from all the known information from Navigation
# message and models
if(Conf["PLOT_MSR_RESIDUAL"] == '1'):
    # Read the cols we need from LOS file
    LosData = read_csv(LosFile, delim_whitespace=True, skiprows=1, header=None,\
    usecols=[LOS_IDX["SOD"], 
    LOS_IDX["PRN"],
    LOS_IDX["SV-CLK[m]"],
    LOS_IDX["DTR[m]"],
    LOS_IDX["TGD[m]"],
    LOS_IDX["RANGE[m]"],
    LOS_IDX["MEAS[m]"],
    LOS_IDX["TROPO[m]"],
    LOS_IDX["STEC[m]"]])

    print( 'Build and Plot the PVT filter residuals ...')
    
    # Configure plot and call plot generation function
    MsrFunctions.plotMsrResiduals(LosData)


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#>>>>> POS FILE ANALYSES
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Get POS file full path
PosFile = Scen + '/OUT/POS/' + Conf["POS_FILE"]

#-----------------------------------------------------------------------
# PLOT POSITION ANALYSES
#-----------------------------------------------------------------------

# Plot the instantaneous number of satellites used by TLSA receiver
# in PVT solution along the whole day as a function of the hour of the day
if(Conf["PLOT_POS_SATS"] == '1'):
    # Read the cols we need from LOS file
    PosData = read_csv(PosFile, delim_whitespace=True, skiprows=1, header=None,\
    usecols=[POS_IDX["SOD"],
    POS_IDX["NSATS"]])

    print('Plot the instantaneous number of satellites along the whole day...')
    
    # Configure plot and call plot generation function
    PosFunctions.plotPosSats(PosData)

# Plot the PDOP, GDOP, TDOP in order to see the dependency of
# the satellite number used in PVT and the DOP
if(Conf["PLOT_POS_DOP"] == '1'):
    # Read the cols we need from LOS file
    PosData = read_csv(PosFile, delim_whitespace=True, skiprows=1, header=None,\
    usecols=[POS_IDX["SOD"],
    POS_IDX["GDOP"],
    POS_IDX["PDOP"],
    POS_IDX["TDOP"]])

    print('Plot the PDOP, GDOP, TDOP...')
    
    # Configure plot and call plot generation function
    PosFunctions.plotPosDOP(PosData)

# Plot the HDOP and VDOP together with the number of satellites
# used (second axis) in order to see the dependency of the satellite
# number and the DOP
if(Conf["PLOT_POS_HVDOP"] == '1'):
    # Read the cols we need from LOS file
    PosData = read_csv(PosFile, delim_whitespace=True, skiprows=1, header=None,\
    usecols=[POS_IDX["SOD"],
    POS_IDX["NSATS"],
    POS_IDX["HDOP"],
    POS_IDX["VDOP"]])

    print('Plot the HDOP and VDOP together with the number of satellites...')
    
    # Configure plot and call plot generation function
    PosFunctions.plotPosHVDOP(PosData)


# Plot  the  East/North/Up  Position  Error  (EPE,  NPE,  UPE)  as  a
# function of the hour of the day on the same graph
if(Conf["PLOT_POS_ENU_PE"] == '1'):
    # Read the cols we need from LOS file
    PosData = read_csv(PosFile, delim_whitespace=True, skiprows=1, header=None,\
    usecols=[POS_IDX["SOD"],
    POS_IDX["EPE[m]"],
    POS_IDX["NPE[m]"],
    POS_IDX["UPE[m]"]])

    print('Plot  the  East/North/Up  Position  Error  (EPE,  NPE,  UPE)...')
    
    # Configure plot and call plot generation function
    PosFunctions.plotPosENUPE(PosData)

# Plot the Horizontal and Vertical Position Error (HPE) and VPE as a
# function of time (hour of the day)
if(Conf["PLOT_POS_HPE_VPE"] == '1'):
    # Read the cols we need from LOS file
    PosData = read_csv(PosFile, delim_whitespace=True, skiprows=1, header=None,\
    usecols=[POS_IDX["SOD"],
    POS_IDX["EPE[m]"],
    POS_IDX["NPE[m]"],
    POS_IDX["UPE[m]"]])

    print('Plot the Horizontal and Vertical Position Error (HPE) and VPE...')
    
    # Configure plot and call plot generation function
    PosFunctions.plotPosHVPE(PosData)

# Plot Horizontal Scatter plot with NPE vs. EPE (North Position Error
# Y-axis and East Position Error X-axis)
if(Conf["PLOT_POS_NPE_EPE"] == '1'):
    # Read the cols we need from LOS file
    PosData = read_csv(PosFile, delim_whitespace=True, skiprows=1, header=None,\
    usecols=[POS_IDX["SOD"],
    POS_IDX["EPE[m]"],
    POS_IDX["NPE[m]"],
    POS_IDX["HDOP"]])

    print('Plot Horizontal Scatter plot with NPE vs. EPE (North Position Error...')
    
    # Configure plot and call plot generation function
    PosFunctions.plotPosNPEEPE(PosData)