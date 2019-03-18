PLUGINNAME = poiexport
PLUGINS = "$(HOME)"/AppData/Roaming/QGIS/QGIS3/profiles/default/python/plugins/$(PLUGINNAME)
PY_FILES = poiexportColorHash.py __init__.py poiExportColorHashDialog.py
EXTRAS = icon.png metadata.txt
UI_FILES = poiexportcolorhashdialog.ui

deploy: 
	mkdir -p $(PLUGINS)
	cp -vf $(PY_FILES) $(PLUGINS)
	cp -vf $(UI_FILES) $(PLUGINS)
	cp -vf $(EXTRAS) $(PLUGINS)
	cp -vfr doc $(PLUGINS)
	cp -vf helphead.html $(PLUGINS)/index.html
	python -m markdown -x markdown.extensions.headerid README.md >> $(PLUGINS)/index.html
	echo '</body>' >> $(PLUGINS)/index.html
