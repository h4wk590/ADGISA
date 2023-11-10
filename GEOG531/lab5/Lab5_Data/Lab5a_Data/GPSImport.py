#
# GPSImport.py
#
# Author:  XXXX
# Date:    XXXX
# Version: ArcGIS 10.0
# Purpose: Appends a Shapefile of GPS points collected in the field to a
#          Master geodatabase Feature Class of Corners points.  It retains
#          the Corners attribute from the incoming file, and uses static
#          values for the CUTB_SEQ_NBR and BLOCK_NAME attributes.
#
#          Parameters:
#               1) Input Shapefile (Point)
#               2) Field in the incoming Shapefile which holds the Corner (text)
#               3) Output geodatabase feature class (Point)
#               4) Static value for CUTB_SEQ_NBR for all new points (double)
#               5) Static value for BLOCK_NAME for all new points (string)
#
#***************************************************************************************
#
import arcpy

# input GPS shapefile
InSHP = arcpy.GetParameterAsText(0)
# FALLING_CORNER recorded in field
InField = arcpy.GetParameterAsText(1)
# destination output geodatabase feature class
OutFC = arcpy.GetParameterAsText(2)
# value to be propogated to CUTB_SEQ_NBR; double data type
InSeq = arcpy.GetParameterAsText(3)
# value to be propogated to BLOCK_NAME; string data type
InBlock = arcpy.GetParameterAsText(4)

# Temporarily add the new fields to the source shapefile
# We do this because we don't know if these fields are already in the SHP, and don't want to
# alter the values stored there if so.  This way we just add the values we want temporarily
# and drop them later.
arcpy.AddField_management(InSHP, "TempCUTB", "Double")
arcpy.CalculateField_management(InSHP,"TempCUTB", InSeq, "PYTHON")
arcpy.AddField_management(InSHP, "TempBLK", "TEXT","#","#","20","#","NON_NULLABLE","NON_REQUIRED","#")
arcpy.CalculateField_management(InSHP,"TempBLK", "'" + InBlock + "'", "PYTHON")

# now set up the field mappings, to take attributes from the new source file into the master
fieldmappings = arcpy.FieldMappings()
fieldmappings.addTable(InSHP)
fieldmappings.addTable(OutFC)

# set up the mapping from the input SHP to the Corner attribute in master
fieldmap = fieldmappings.getFieldMap(fieldmappings.findFieldMapIndex("CORNER"))
fieldmap.addInputField(InSHP, InField)
fieldmappings.replaceFieldMap(fieldmappings.findFieldMapIndex("CORNER"), fieldmap)

# map from our temporary CUTB_SEQ_NBR to the real one in master
fieldmap = fieldmappings.getFieldMap(fieldmappings.findFieldMapIndex("CUTB_SEQ_NBR"))
fieldmap.addInputField(InSHP, "TempCUTB")
fieldmappings.replaceFieldMap(fieldmappings.findFieldMapIndex("CUTB_SEQ_NBR"), fieldmap)

# map from our temporary BLOCK_NAME to the real one in master
fieldmap = fieldmappings.getFieldMap(fieldmappings.findFieldMapIndex("BLOCK_NAME"))
fieldmap.addInputField(InSHP, "TempBLK")
fieldmappings.replaceFieldMap(fieldmappings.findFieldMapIndex("BLOCK_NAME"), fieldmap)

# do the append - bring the new shapefile points into the master Corners feature class
arcpy.Append_management(InSHP, OutFC, "NO_TEST", fieldmappings)

# clean up: remove the two temporary fields from the incoming shapefile
dropFields = ["TempBLK", "TempCUTB"]
arcpy.DeleteField_management(InSHP, dropFields)
