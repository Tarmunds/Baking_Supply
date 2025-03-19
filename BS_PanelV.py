import bpy

class BAKINGSUPPLY_PanelGeneral(bpy.types.Panel):
    """Panel for the low and high mesh operations"""
    bl_label = "Baking Supply"
    bl_idname = "OBJECT_PT_low_mesh_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tarmunds Addons'  # Updated for consistency with the add-on name

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        box = self.layout.box()
        row = box.row()
        row.label(text="Visibility :")

        row1 = box.row()
        row1.operator("object.bs_hide_high_meshes", text="Hide High")
        row1.operator("object.bs_hide_low_meshes", text="Hide Low")

        sub_row = box.row()
        sub_row.operator("object.bs_show_high_meshes", text="Show High")
        sub_row.operator("object.bs_show_low_meshes", text="Show Low")

        # Separator
        self.layout.row().separator()

        col = layout.column(align=True)
        row = layout.row()
        row = col.row(align=True)
        row.operator("object.bs_add_suffix", text="Add _high").rename_type = "high"
        row.operator("object.bs_add_suffix", text="Add _low").rename_type = "low"

        col.operator("object.bs_switch_suffix", text="High <> Low")
        col.operator("object.bs_transfer_name_suffix", text="Transfer Name")


        # Separator
        self.layout.row().separator()
        
        row = layout.row()
        row.scale_y = 1
        # Display the "Appelation" variable
        row.label(text="Name for the files :")
        row.prop(scene, "appelation", text="")

        row = layout.row()
        row.scale_y = 1.5
        # Add the export buttons
        row.operator("object.export_selected_operator_high", text="Export High")
        row.operator("object.export_selected_operator_low", text="Export Low")


        # Separator
        self.layout.row().separator()
 
        # Preprocess and Unprocess Drop-down Menu
        col = self.layout.column()
        if not context.scene.show_path_options:
            row = col.row()
            row.prop(context.scene, "show_path_options", icon='TRIA_RIGHT', text="", emboss=False, toggle=True)
            row.label(text="Path Options")
        else:
            # Expanded box for Path Options
            box = layout.box()
            row = box.row()
            row.prop(context.scene, "show_path_options", icon='TRIA_DOWN', text="", emboss=False, toggle=True)
            row.label(text="Path Options")

            # Custom File Path inside the same box
            row1 = box.row()
            row1.scale_y = 1
            row1.label(text="Custom File Path:")
            
            row2 = box.row()
            row2.prop(scene, "mesh_path", text="")
        
        #marmoset export
        self.layout.row().separator()
        row = layout.row()
        row.scale_y = 2
        row.operator("object.bs_export_and_launch_marmoset", text="Export & Launch Marmoset", icon='MONKEY')


        col = layout.column()

        if not scene.BS_BakeProperities:
            # Collapsed state
            row = col.row()
            row.prop(scene, "BS_BakeProperities", icon='TRIA_RIGHT', text="", emboss=False, toggle=True)
            row.label(text="Bake Options")
            row.prop(scene, "BS_SendProperities", text="Send Properties", toggle=True)
        else:
            # Expanded state
            box = layout.box()
            row = box.row()
            row.prop(scene, "BS_BakeProperities", icon='TRIA_DOWN', text="", emboss=False, toggle=True)
            row.label(text="Bake Options")
            row.prop(scene, "BS_SendProperities", text="Send Properties", toggle=True)

            col = box.column()
            col.scale_y = 1.3
            col.prop(scene, "BS_ResX", text="Res X")
            col.prop(scene, "BS_ResY", text="Res Y")
            col.prop(scene, "BS_Sample", text="Sample")
            col.prop(scene, "BS_FileFormat", text="File Format")

            col = box.column(align=True)
            col.scale_y = 1
            col.prop(scene, "BS_SinglePSD", text="Single Layered PSD file")

            col = box.column()
            col.scale_y = 1.3
            col.prop(scene, "BS_NormalDirection", text="OpenGL", toggle=True, expand=True)

            col = box.column(align=True)
            col.prop(scene, "BS_PathBakeAsMeshes", text="Use same path as the mesh")

            col = box.column(align=True)
            col.enabled = not scene.BS_PathBakeAsMeshes
            col.prop(scene, "BS_BakePath", text="")

            col = box.column(align=True)
            col.scale_y = 1
            col.prop(scene, "BS_UsePreset", text="Use Tarmunds Map Preset")

            col = box.column(align=True)
            col.scale_y = 1.3
            col.enabled = scene.BS_UsePreset
            col.prop(scene, "BS_Preset", text="Map Preset")

            col = box.column(align=True)
            col.scale_y = 1.5
            col.prop(scene, "BS_DirectBake", text="Direct Bake", toggle=True)


"""


        self.layout.row().separator()
        col = layout.column(align=True)
        col.scale_y = 1.3
        col.prop(scene, "BS_ResX", text="Res X")
        col.prop(scene, "BS_ResY", text="Res Y")

        col.prop(scene, "BS_Sample", text="Sample")

        col.prop(scene, "BS_FileFormat", text="File Format")
        col = layout.column(align=True)
        col.scale_y = 1
        col.prop(scene, "BS_SinglePSD", text="Single Layered PSD file")

        self.layout.row().separator()
        col = layout.column(align=True)
        col.prop(scene, "BS_PathBakeAsMeshes", text="Use same path as the mesh") 

        col = layout.column(align=True)
        col.enabled = not scene.BS_PathBakeAsMeshes
        col.prop(scene, "BS_BakePath", text="")


        self.layout.row().separator()
        col = layout.column(align=True)
        col.scale_y = 1
        col.prop(scene, "BS_UsePreset", text="Use Tarmunds Map Preset")        
        col = layout.column(align=True)
        col.scale_y = 1.3
        col.enabled = scene.BS_UsePreset  # This disables the dropdown when BS_UsePreset is True
        col.prop(scene, "BS_Preset", text="Map Preset")

        self.layout.row().separator()
        col = layout.column(align=True)
        col.scale_y = 1
        col.prop(scene, "BS_DirectBake", text="Direct")

"""


classes = (
    BAKINGSUPPLY_PanelGeneral,
)

def register():
    for c in classes:
        bpy.utils.register_class(c)

def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)

if __name__ == "__main__":
    register()
