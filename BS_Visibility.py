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

