#  ***** GPL LICENSE BLOCK *****
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#  All rights reserved.
#  ***** GPL LICENSE BLOCK *****

# <pep8 compliant>
import os
import bpy

from . import BS_PanelV
from . import BS_Visibility
from . import BS_Exporter
from . import BS_Namer
from . import BS_Marmoset

bl_info = {
    "name": "Baking Supply",
    "author": "Tarmunds",
    "version": (3, 0, 1),
    "blender": (4, 0, 0),
    "location": "View3D > Tool Shelf > Baking Supply",
    "description": "Tools to easily manage baking workflows between baking software and Blender",
    "wiki_url": "https://github.com/Tarmunds/Baking_Supply", 
    "tracker_url": "https://github.com/Tarmunds/Baking_Supply/issues",  
    "category": "Object",
}

class BAKINGSUPPLY_Preferences(bpy.types.AddonPreferences):
    """Preferences panel for Baking Supply addon."""
    bl_idname = __package__

    marmoset_path: bpy.props.StringProperty(
        name="Marmoset Toolbag Path",
        default=r"C:\\Program Files\\Marmoset\\Toolbag 5\\Toolbag.exe",
        subtype='FILE_PATH'
    )

    def draw(self, context):
        layout = self.layout
        layout.label(text="Marmoset Toolbag Path:")
        layout.prop(self, "marmoset_path", text="")

classes = (
    BS_Visibility.BAKINGSUPPLY_ShowLow,
    BS_Visibility.BAKINGSUPPLY_ShowHigh,
    BS_Visibility.BAKINGSUPPLY_HideLow,
    BS_Visibility.BAKINGSUPPLY_HideHigh,
    BS_Exporter.BAKINGSUPPLY_ExportLow,
    BS_Exporter.BAKINGSUPPLY_ExportHigh,
    BS_Namer.BAKINGSUPPLY_SwitchSuffix,
    BS_Namer.BAKINGSUPPLY_AddSuffix,
    BS_Namer.BAKINGSUPPLY_TransferName,
    BS_PanelV.BAKINGSUPPLY_PanelGeneral,
    BS_Marmoset.BAKINGSUPPLY_ExportAndLaunchMarmoset,
    BAKINGSUPPLY_Preferences,
)

def register():
    for c in classes:
        bpy.utils.register_class(c)

    bpy.types.Scene.appelation = bpy.props.StringProperty(
        name="",
        default="",
        description="Name for FBX file"
    )
    bpy.types.Scene.mesh_path = bpy.props.StringProperty(name="Path", default="", maxlen=1024, subtype='DIR_PATH')
    bpy.types.Scene.show_path_options = bpy.props.BoolProperty(
        name="Show Path Options",
        description="Toggle the display of export path options",
        default=False
    )
    
    # Ensure preferences are loaded correctly
    addon_prefs = bpy.context.preferences.addons.get(__package__)
    if addon_prefs:
        marmoset_path = addon_prefs.preferences.marmoset_path
        if not os.path.exists(marmoset_path):
            print(f"WARNING: Marmoset Toolbag executable not found at {marmoset_path}! Set the correct path in Preferences.")
    else:
        print("WARNING: Baking Supply addon preferences not found.")

def unregister():
    for c in reversed(classes):
        bpy.utils.unregister_class(c)

    del bpy.types.Scene.appelation
    del bpy.types.Scene.mesh_path
    del bpy.types.Scene.show_path_options

if __name__ == '__main__':
    register()