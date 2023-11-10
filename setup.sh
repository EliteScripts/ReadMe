#!/bin/bash

cp tourbillon.desktop /usr/share/applications/tourbillon.desktop
cp tourbillon /usr/bin/tourbillon
cp tourbillon-512.png /usr/share/icons/hicolor/512x512/apps/tourbillon-512.png
cp tourbillon-16.png /usr/share/icons/hicolor/16x16/apps/tourbillon-16.png

chmod +x /usr/bin/tourbillon

echo "Setup OK"
