#
# OGMA_Area.py
#
# Author:  XXX
# Date:    XXX
# Version: ArcGIS 10.0
# Purpose: Performs a very simple analysis which seeks to determine the area of OGMA beneath
#          a cutblock feature (or features).  It buffers the clearing(s) by 100m, then intersects
#          the resulting buffers with the OGMA polygons.  The result is then summarized to
#          show the area of OGMA which is encroached upon.
#
#          Parameters:
#               1) Clearings feature layer
#               2) Output summary table
#               3) OGMA feature layer
#
#***************************************************************************************
#

import arcpy

# Script/tool arguments
Clearings = arcpy.GetParameterAsText(0)
Output_Table = arcpy.GetParameterAsText(1)
OGMA = arcpy.GetParameterAsText(2)

# allow us to use the same output name several times, particularly for intermediate results (e.g, buffer)
arcpy.env.overwriteOutput = True

# Process: Buffer
Buffered_Clearings = arcpy.Buffer_analysis(Clearings, "Buffered_Clearings", "100 Meters", "FULL", "ROUND", "ALL", "")

# set up a list for the feature classes to be intersected
InputFCs = [Buffered_Clearings, OGMA]

# Process: Intersect
Impacted_OGMA = arcpy.Intersect_analysis(InputFCs, "Impacted_OGMA", "ALL", "", "INPUT")

# Process: Summary Statistics
arcpy.Statistics_analysis(Impacted_OGMA, Output_Table, "Shape_Area SUM", "OGMA_Identifier")

