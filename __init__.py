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
    "version": (3, 5, ),
    "blender": (4, 2, 0),
    "location": "View3D > Tool Shelf > Baking Supply",
    "description": "Tools to easily manage baking workflows between Marmoset Toolbag and Blender",
    "wiki_url": "https://github.com/Tarmunds/Baking_Supply", 
    "tracker_url": "https://github.com/Tarmunds/Baking_Supply/issues",  
    "category": "Object",
}


def update_mesh_path(self, context):
    if self.mesh_path:
        self.mesh_path = os.path.abspath(bpy.path.abspath(self.mesh_path))

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


BS_ResX = [
    ("128", "128", "Description for option 1"),
    ("256", "256", "Description for option 1"),
    ("512", "512", "Description for option 1"),
    ("1024", "1024", "Description for option 1"),
    ("2048", "2048", "Description for option 1"),
    ("4096", "4096", "Description for option 1"),
    ("8192", "8192", "Description for option 1"),
]
BS_ResY = [
    ("128", "128", "Description for option 1"),
    ("256", "256", "Description for option 1"),
    ("512", "512", "Description for option 1"),
    ("1024", "1024", "Description for option 1"),
    ("2048", "2048", "Description for option 1"),
    ("4096", "4096", "Description for option 1"),
    ("8192", "8192", "Description for option 1"),
]
BS_Sample = [
    ("1", "1", "Description for option 1"),
    ("2", "2", "Description for option 1"),
    ("4", "4", "Description for option 1"),
    ("8", "8", "Description for option 1"),
    ("16", "16", "Description for option 1"),
    ("32", "32", "Description for option 1"),
    ("64", "64", "Description for option 1"),
]
BS_FileFormat = [
    ("png", "Png", "Description for option 1"),
    ("psd", "Psd", "Description for option 1"),
    ("targa", "Targa", "Description for option 1"),
]
BS_Preset = [
    ("ASSETS", "Assets", "Description for option 1"),
    ("TILEABLE", "Tileable", "Description for option 1"),
]




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
        name="appelation",
        default="",
        description="Name for FBX file"
    )
    bpy.types.Scene.mesh_path = bpy.props.StringProperty(
        name="Path", 
        default="", 
        maxlen=1024, 
        subtype='DIR_PATH',
        update=lambda self, context: setattr(
            self, "mesh_path", os.path.abspath(bpy.path.abspath(getattr(self, "mesh_path")))),
    )
    
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
    
    #enum register
    bpy.types.Scene.BS_ResX = bpy.props.EnumProperty(
        name="X resolution",
        description="Select the X resolution of the baked map",
        items=BS_ResX,
        default="2048"
    )
    bpy.types.Scene.BS_ResY = bpy.props.EnumProperty(
        name="Y resolution",
        description="Select the Y resolution of the baked map",
        items=BS_ResY,
        default="2048"
    )
    bpy.types.Scene.BS_Sample = bpy.props.EnumProperty(
        name="Sample Count",
        description="Set the sample count of the baker",
        items=BS_Sample,
        default="16"
    )
    bpy.types.Scene.BS_FileFormat = bpy.props.EnumProperty(
        name="File Format",
        description="Set the format of the output files, overide by the SIngle Layered PSD",
        items=BS_FileFormat,
        default="png"
    )
    bpy.types.Scene.BS_Preset = bpy.props.EnumProperty(
        name="Preset",
        description="Select the Tarmunds premade preset for the maps",
        items=BS_Preset,
        default="ASSETS"
    )

    bpy.types.Scene.BS_SinglePSD = bpy.props.BoolProperty(
        name="Single PSD",
        description="Toggle the output of a single layered PSD, with all the baked map within it",
        default=False
    )
    bpy.types.Scene.BS_UsePreset = bpy.props.BoolProperty(
        name="Use Tarmunds Preset",
        description="Toggle the option to push map preset made by Tarmunds",
        default=False
    )

    bpy.types.Scene.BS_PathBakeAsMeshes = bpy.props.BoolProperty(
        name="Use the same path as the mesh export one",
        description="Toggle to overide the bake path, to use the same as the exported meshes",
        default=False
    )
    bpy.types.Scene.BS_BakePath = bpy.props.StringProperty(
        name="Bake Path",
        default="",
        maxlen=1024,
        subtype='DIR_PATH',
        update=lambda self, context: setattr(
            self, "BS_BakePath", os.path.abspath(bpy.path.abspath(getattr(self, "BS_BakePath"))))
    )

    bpy.types.Scene.BS_DirectBake = bpy.props.BoolProperty(
        name="Bake Directly",
        description="Launch a Bake just after the import",
        default=False
    )
    bpy.types.Scene.BS_SendProperities = bpy.props.BoolProperty(
        name="Send Properities",
        description="Set baker properities",
        default=True
    )
    bpy.types.Scene.BS_BakeProperities = bpy.props.BoolProperty(
        name="Send Properities",
        description="Show Bake properities",
        default=False
    )
    bpy.types.Scene.BS_NormalDirection = bpy.props.EnumProperty(
    name="Normal Map Format",
    description="Choose between OpenGL and DirectX normal maps",
    items=[
        ("OPENGL", "OpenGL", "Use OpenGL normal map format"),
        ("DIRECTX", "DirectX", "Use DirectX normal map format"),
    ],
    default="OPENGL"
)


def unregister():
    for c in reversed(classes):
        bpy.utils.unregister_class(c)

    del bpy.types.Scene.appelation
    del bpy.types.Scene.mesh_path
    del bpy.types.Scene.show_path_options

    #enum unregister
    del bpy.types.Scene.BS_ResX
    del bpy.types.Scene.BS_ResY
    del bpy.types.Scene.BS_Sample
    del bpy.types.Scene.BS_FileFormat
    del bpy.types.Scene.BS_FileFormat
    del bpy.types.Scene.BS_Preset

    del bpy.types.Scene.BS_SinglePSD
    del bpy.types.Scene.BS_UsePreset
    del bpy.types.Scene.BS_PathBakeAsMeshes
    del bpy.types.Scene.BS_BakePath
    del bpy.types.Scene.BS_DirectBake
    del bpy.types.Scene.BS_SendProperities
    del bpy.types.Scene.BS_BakeProperities
    del bpy.types.Scene.BS_NormalDirection

if __name__ == '__main__':
    register()