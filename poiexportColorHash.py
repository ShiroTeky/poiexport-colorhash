# -*- coding: utf-8 -*-
"""
/***************************************************************************
 POIExport
    A QIGS plugin for exporting GPS Points of Interest
                              -------------------
        begin                : 2016-08-29
        copyright            : (C) 2016 by
                               C. Hamilton
        email                : adenaculture@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction

import os
from .poiExportColorHashDialog import POIExportColorHashDialog

class POIExportColorHash:
    def __init__(self, iface):
        self.iface = iface
        self.poiDialog = None

    def initGui(self):
        """Create the menu & tool bar items within QGIS"""
        icon = QIcon(os.path.dirname(__file__) + "/icon.png")
        self.poiAction = QAction(icon, "POI Exporter ColorHash", self.iface.mainWindow())
        self.poiAction.triggered.connect(self.showPOIDialog)
        self.poiAction.setCheckable(False)
        self.iface.addToolBarIcon(self.poiAction)
        self.iface.addPluginToVectorMenu("GPS", self.poiAction)

    def unload(self):
        """Remove the plugin menu item and icon from QGIS GUI."""
        self.iface.removePluginVectorMenu("GPS", self.poiAction)
        self.iface.removeToolBarIcon(self.poiAction)
    
    def showPOIDialog(self):
        """Display the POI Dialog window."""
        if not self.poiDialog:
            self.poiDialog = POIExportColorHashDialog(self.iface)
        self.poiDialog.show()
        self.poiDialog.raise_()
        self.poiDialog.activateWindow()
        
        
