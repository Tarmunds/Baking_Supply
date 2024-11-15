import bpy
import os

class BAKINGSUPPLY_ExportHigh(bpy.types.Operator):
    bl_idname = "object.export_selected_operator_high"
    bl_label = "Export Selected High"

    def execute(self, context):
        scene = context.scene
        selected_objects = []

        # Store the original selection state
        original_selection = [obj for obj in bpy.data.objects if obj.select_get()]

        # Select objects with "_high" in their names
        for obj in bpy.data.objects:
            if obj.select_get() and "high" in obj.name:
                selected_objects.append(obj)
            else:
                obj.select_set(False)

        if not selected_objects:
            self.report({'WARNING'}, "No objects selected with 'high' in their names.")
            return {'CANCELLED'}

        # Ensure the appellation property is set
        if not scene.appelation.strip():
            self.report({'ERROR'}, "Appellation cannot be empty. Please provide a name.")
            return {'CANCELLED'}

        # Determine the export path
        if len(scene.mesh_path.strip()) == 0:
            # If mesh_path is not set, use the blend file directory
            blend_filepath = bpy.data.filepath
            blend_dir = os.path.dirname(blend_filepath)
            export_filename = scene.appelation + "_high.fbx"
            export_path = os.path.join(blend_dir, export_filename)
        else:
            # Use the specified mesh_path
            export_path = os.path.join(scene.mesh_path, scene.appelation + "_high.fbx")

        # Check if the directory exists
        export_dir = os.path.dirname(export_path)
        if not os.path.exists(export_dir):
            self.report({'ERROR'}, f"Directory does not exist: {export_dir}")
            return {'CANCELLED'}

        # Export to FBX
        try:
            bpy.ops.export_scene.fbx(filepath=export_path, use_selection=True)
        except PermissionError:
            self.report({'ERROR'}, f"Permission denied: Unable to write to {export_path}. Please check the file path.")
            return {'CANCELLED'}

        # Restore the original selection state
        for obj in bpy.data.objects:
            obj.select_set(obj in original_selection)

        self.report({'INFO'}, f"Exported successfully to: {export_path}")
        return {'FINISHED'}

class BAKINGSUPPLY_ExportLow(bpy.types.Operator):
    bl_idname = "object.export_selected_operator_low"
    bl_label = "Export Selected Low"

    def execute(self, context):
        scene = context.scene
        selected_objects = []

        # Store the original selection state
        original_selection = [obj for obj in bpy.data.objects if obj.select_get()]

        # Select objects with "_low" in their names
        for obj in bpy.data.objects:
            if obj.select_get() and "low" in obj.name:
                selected_objects.append(obj)
            else:
                obj.select_set(False)

        if not selected_objects:
            self.report({'WARNING'}, "No objects selected with 'low' in their names.")
            return {'CANCELLED'}

        # Ensure the appellation property is set
        if not scene.appelation.strip():
            self.report({'ERROR'}, "Appellation cannot be empty. Please provide a name.")
            return {'CANCELLED'}

        # Determine the export path
        if len(scene.mesh_path.strip()) == 0:
            # If mesh_path is not set, use the blend file directory
            blend_filepath = bpy.data.filepath
            blend_dir = os.path.dirname(blend_filepath)
            export_filename = scene.appelation + "_low.fbx"
            export_path = os.path.join(blend_dir, export_filename)
        else:
            # Use the specified mesh_path
            export_path = os.path.join(scene.mesh_path, scene.appelation + "_low.fbx")

        # Check if the directory exists
        export_dir = os.path.dirname(export_path)
        if not os.path.exists(export_dir):
            self.report({'ERROR'}, f"Directory does not exist: {export_dir}")
            return {'CANCELLED'}

        # Export to FBX
        try:
            bpy.ops.export_scene.fbx(filepath=export_path, use_selection=True)
        except PermissionError:
            self.report({'ERROR'}, f"Permission denied: Unable to write to {export_path}. Please check the file path.")
            return {'CANCELLED'}

        # Restore the original selection state
        for obj in bpy.data.objects:
            obj.select_set(obj in original_selection)

        self.report({'INFO'}, f"Exported successfully to: {export_path}")
        return {'FINISHED'}

Classes = (
    BAKINGSUPPLY_ExportLow,
    BAKINGSUPPLY_ExportHigh,
)

def register():
    for c in Classes:
        bpy.utils.register_class(c)

def unregister():
    for c in reversed(Classes):
        bpy.utils.unregister_class(c)

if __name__ == "__main__":
    register()
