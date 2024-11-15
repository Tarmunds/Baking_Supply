import bpy



#show low
class BAKINGSUPPLY_ShowLow(bpy.types.Operator):
    """Operator to show or hide meshes with '_low' in their name"""
    bl_idname = "object.show_low_meshes"
    bl_label = "Show Low"
    
    def execute(self, context):
        for obj in bpy.data.objects:
            if "_low" in obj.name:
                obj.hide_set(False)
        return {'FINISHED'}


#Hide low
class BAKINGSUPPLY_HideLow(bpy.types.Operator):
    """Operator to hide meshes with '_low' in their name"""
    bl_idname = "object.hide_low_meshes"
    bl_label = "Hide Low"
    
    def execute(self, context):
        for obj in bpy.data.objects:
            if "_low" in obj.name:
                obj.hide_set(True)
        return {'FINISHED'}


#show High
class BAKINGSUPPLY_ShowHigh(bpy.types.Operator):
    """Operator to show or hide meshes with '_high' in their name"""
    bl_idname = "object.show_high_meshes"
    bl_label = "Show High"
    
    def execute(self, context):
        for obj in bpy.data.objects:
            if "_high" in obj.name:
                obj.hide_set(False)
        return {'FINISHED'}


#Hide high
class BAKINGSUPPLY_HideHigh(bpy.types.Operator):
    """Operator to hide meshes with '_high' in their name"""
    bl_idname = "object.hide_high_meshes"
    bl_label = "Hide High"
    
    def execute(self, context):
        for obj in bpy.data.objects:
            if "_high" in obj.name:
                obj.hide_set(True)
        return {'FINISHED'}

class BAKINGSUPPLY_Panel(bpy.types.Panel):
    """Panel for the low and high mesh operations"""
    bl_label = "Mesh Visibility"
    bl_idname = "OBJECT_PT_low_mesh_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Custom Addon'

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.operator("object.show_low_meshes", text="Show Low")
        row.operator("object.hide_low_meshes", text="Hide Low")

        row = layout.row()
        row.operator("object.show_high_meshes", text="Show High")
        row.operator("object.hide_high_meshes", text="Hide High")

Classes = (
    BAKINGSUPPLY_ShowLow,
    BAKINGSUPPLY_ShowHigh,
    BAKINGSUPPLY_HideLow,
    BAKINGSUPPLY_HideHigh
)

def register():
    for c in Classes:
        bpy.utils.register_class(c)

def unregister():
    for c in reversed(Classes):
        bpy.utils.unregister_class(c)

