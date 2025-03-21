import bpy
import re

# Operator to replace "_high" with "_low" and vice versa
class BAKINGSUPPLY_SwitchSuffix(bpy.types.Operator):
    bl_idname = "object.bs_switch_suffix"
    bl_label = "High <> Low"

    def execute(self, context):
        pattern = re.compile(r'(_high|_low)', re.IGNORECASE)

        def replace_case(match):
            text = match.group(1).lower()
            return '_low' if text == '_high' else '_high'

        for obj in bpy.context.selected_objects:
            obj.name = pattern.sub(replace_case, obj.name)

        return {'FINISHED'}

# Operator to add "_high" or "_low" to object names, preventing duplicate suffixes
class BAKINGSUPPLY_AddSuffix(bpy.types.Operator):
    bl_idname = "object.bs_add_suffix"
    bl_label = "Add Suffix"

    rename_type: bpy.props.StringProperty(name="Rename Type")

    def execute(self, context):
        rename_type = self.rename_type.lower()
        for obj in bpy.context.selected_objects:
            if obj.type == 'MESH':
                name = obj.name.rstrip("_high_low")  # Remove existing suffix if present
                obj.name = f"{name}_{rename_type}"
        
        return {'FINISHED'}
    
# Operator to transfer names between _high and _low meshes with indexing
class BAKINGSUPPLY_TransferName(bpy.types.Operator):
    bl_idname = "object.bs_transfer_name_suffix"
    bl_label = "Transfer Name"

    def execute(self, context):
        active_obj = context.active_object

        if not active_obj:
            self.report({'WARNING'}, "No active object selected")
            return {'CANCELLED'}

        name = active_obj.name
        base_name = None

        if "_high" in name:
            base_name = name.replace("_high", "_low")
        elif "_low" in name:
            base_name = name.replace("_low", "_high")

        if not base_name:
            self.report({'WARNING'}, "Active object's name does not contain '_high' or '_low'")
            return {'CANCELLED'}

        existing_names = {obj.name for obj in bpy.data.objects}  # Collect existing names
        count = 1

        for obj in context.selected_objects:
            if obj != active_obj and obj.type == 'MESH':
                new_name = base_name
                while new_name in existing_names:
                    new_name = f"{base_name}_{count}"
                    count += 1
                obj.name = new_name
                existing_names.add(new_name)

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
