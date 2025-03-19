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


if "bpy" in locals():
    import importlib
    importlib.reload(BS_Panel)
    importlib.reload(BS_Visibility)
    importlib.reload(BS_Exporter)
    importlib.reload(BS_Namer)
    importlib.reload(BS_Marmoset)

import bpy
from . import BS_Panel
from . import BS_Visibility
from . import BS_Exporter
from . import BS_Namer
from . import BS_Marmoset

bl_info = {
    "name": "Baking Supply",
    "author": "Tarmunds",
    "version": (3, 0),
    "blender": (4, 0, 0),
    "location": "View3D > Tool Shelf > Baking Supply",
    "description": "Tools to easily manage baking workflows between baking software and Blender",
    "wiki_url": "https://github.com/Tarmunds/Baking_Supply", 
    "tracker_url": "https://github.com/Tarmunds/Baking_Supply/issues",  
    "category": "Object",
}

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
    BS_Panel.BAKINGSUPPLY_Panel,
    BS_Marmoset.BAKINGSUPPLY_ExportAndLaunchMarmoset,
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
    bpy.types.Preferences.marmoset_path = bpy.props.StringProperty(
        name="Marmoset Toolbag Path",
        default=r"C:\Program Files\Marmoset\Toolbag 5\Toolbag.exe",
        subtype='FILE_PATH'
    )

    # Check if Marmoset exists at the default path
    if not os.path.exists(bpy.context.preferences.marmoset_path):
        print("WARNING: Marmoset Toolbag executable not found! Set the correct path in Preferences.")

def unregister():
    for c in reversed(classes):
        bpy.utils.unregister_class(c)

    del bpy.types.Scene.appelation
    del bpy.types.Scene.mesh_path
    del bpy.types.Scene.show_path_options
    del bpy.types.Preferences.marmoset_path

if __name__ == '__main__':
    register()
