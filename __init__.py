import bpy
from . import BS_Panel
from . import BS_Visibility
from . import BS_Exporter

bl_info = {
    "name": "Baking Supply",
    "author": "Tarmunds",
    "version": (2, 0),
    "blender": (4, 0, 0),
    "location": "View3D > Tool Shelf > Baking Supply",
    "description": "Tools to easily manage baking workflows between baking software and Blender",
    "wiki_url": "https://github.com/Tarmunds/Baking_Supply",  # Update to your actual URL
    "tracker_url": "https://github.com/Tarmunds/Baking_Supply/issues",  # Update to your actual URL
    "category": "Object",
}

classes = (
    BS_Visibility.BAKINGSUPPLY_ShowLow,
    BS_Visibility.BAKINGSUPPLY_ShowHigh,
    BS_Visibility.BAKINGSUPPLY_HideLow,
    BS_Visibility.BAKINGSUPPLY_HideHigh,
    BS_Exporter.BAKINGSUPPLY_ExportLow,
    BS_Exporter.BAKINGSUPPLY_ExportHigh,
    BS_Panel.BAKINGSUPPLY_Panel,
)

def register():
    for c in classes:
        bpy.utils.register_class(c)
    bpy.types.Scene.appelation = bpy.props.StringProperty(
        name="",
        default="",
        description="Name for FBX file"
    )
    bpy.types.Scene.mesh_path = bpy.props.StringProperty(name="Path", default="")
    bpy.types.Scene.show_path_options = bpy.props.BoolProperty(
    name="Show Path Options",
    description="Toggle the display of export path options",
    default=False
    )

def unregister():
    for c in reversed(classes):
        bpy.utils.unregister_class(c)
    del bpy.types.Scene.appelation
    del bpy.types.Scene.mesh_path
    del bpy.types.Scene.show_path_options

if __name__ == '__main__':
    register()
