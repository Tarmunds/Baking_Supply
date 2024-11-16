import bpy

# Operator to replace "_high" with "_low" and vice versa
class BAKINGSUPPLY_SwitchSuffix(bpy.types.Operator):
    bl_idname = "object.switch_suffix"
    bl_label = "High <> Low"

    def execute(self, context):
        for obj in bpy.context.selected_objects:
            name = obj.name

            if "_high" in name.lower():
                if "_high" in name:
                    obj.name = name.replace("_high", "_low")
                elif "_High" in name:
                    obj.name = name.replace("_High", "_Low")
            elif "_low" in name.lower():
                if "_low" in name:
                    obj.name = name.replace("_low", "_high")
                elif "_Low" in name:
                    obj.name = name.replace("_Low", "_High")

        return {'FINISHED'}


# Operator to add "_high" or "_low" to object names
class BAKINGSUPPLY_AddSuffix(bpy.types.Operator):
    bl_idname = "object.add_suffix"
    bl_label = "Add Suffix"

    rename_type: bpy.props.StringProperty(name="Rename Type")

    def execute(self, context):
        rename_type = self.rename_type
        for obj in bpy.context.selected_objects:
            if obj.type == 'MESH':
                obj.name += f"_{rename_type}"

        return {'FINISHED'}
    
# Operator to transfer names from "_high" to "_low"
class BAKINGSUPPLY_TransferName(bpy.types.Operator):
    bl_idname = "object.transfer_name_suffix"
    bl_label = "Transfer Name"
    
    def execute(self, context):
        active_obj = context.active_object
        
        if not active_obj:
            self.report({'WARNING'}, "No active object selected")
            return {'CANCELLED'}
        
        if "_high" not in active_obj.name:
            self.report({'WARNING'}, "Active object's name does not contain '_high'")
            return {'CANCELLED'}
        
        new_name = active_obj.name.replace("_high", "_low")
        
        for obj in context.selected_objects:
            if obj != active_obj and obj.type == 'MESH':
                obj.name = new_name
        
        self.report({'INFO'}, "Names transferred successfully")
        return {'FINISHED'}




Classes = (
    BAKINGSUPPLY_SwitchSuffix,
    BAKINGSUPPLY_AddSuffix,
    BAKINGSUPPLY_TransferName
)

def register():
    for c in Classes:
        bpy.utils.register_class(c)

def unregister():
    for c in reversed(Classes):
        bpy.utils.unregister_class(c)

if __name__ == "__main__":
    register()
