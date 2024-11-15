import bpy

class BAKINGSUPPLY_Panel(bpy.types.Panel):
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
        row1.operator("object.show_low_meshes", text="Show Low")
        row1.operator("object.hide_low_meshes", text="Hide Low")

        sub_row = box.row()
        sub_row.operator("object.show_high_meshes", text="Show High")
        sub_row.operator("object.hide_high_meshes", text="Hide High")

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
            box = self.layout.box()
            row = box.row()
            row.prop(context.scene, "show_path_options", icon='TRIA_DOWN', text="", emboss=False, toggle=True)
            row.label(text="Path Options")

            row = box.row()
            row.scale_y = 1
            row = layout.row()
            row.label(text="Custom File Path:")
            row = layout.row()
            row.prop(scene, "mesh_path", text="")

classes = (
    BAKINGSUPPLY_Panel,
)

def register():
    for c in classes:
        bpy.utils.register_class(c)

def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)

if __name__ == "__main__":
    register()
