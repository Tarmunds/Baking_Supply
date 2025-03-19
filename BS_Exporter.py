import bpy
import os

class BAKINGSUPPLY_ExportHigh(bpy.types.Operator):
    """Export only selected objects containing '_high' in their name"""
    bl_idname = "object.export_selected_operator_high"
    bl_label = "Export Selected High"

    def execute(self, context):
        scene = context.scene
        selected_objects = [obj for obj in context.selected_objects if "_high" in obj.name]

        if not selected_objects:
            self.report({'WARNING'}, "No selected objects with '_high' in their names.")
            return {'CANCELLED'}

        if not scene.appelation.strip():
            self.report({'ERROR'}, "Appellation cannot be empty. Please provide a name.")
            return {'CANCELLED'}

        export_path = os.path.join(scene.mesh_path.strip() or os.path.dirname(bpy.data.filepath), f"{scene.appelation}_high.fbx")

        if not os.path.exists(os.path.dirname(export_path)):
            self.report({'ERROR'}, f"Directory does not exist: {os.path.dirname(export_path)}")
            return {'CANCELLED'}

        # Store the original selection
        original_selection = bpy.context.selected_objects
        bpy.ops.object.select_all(action='DESELECT')

        # Select only '_high' objects
        for obj in selected_objects:
            obj.select_set(True)

        try:
            bpy.ops.export_scene.fbx(filepath=export_path, use_selection=True)
        except PermissionError:
            self.report({'ERROR'}, f"Permission denied: Unable to write to {export_path}.")
            return {'CANCELLED'}
        finally:
            # Restore original selection
            bpy.ops.object.select_all(action='DESELECT')
            for obj in original_selection:
                obj.select_set(True)

        self.report({'INFO'}, f"Exported successfully to: {export_path}")
        return {'FINISHED'}


class BAKINGSUPPLY_ExportLow(bpy.types.Operator):
    """Export only selected objects containing '_low' in their name"""
    bl_idname = "object.export_selected_operator_low"
    bl_label = "Export Selected Low"

    def execute(self, context):
        scene = context.scene
        selected_objects = [obj for obj in context.selected_objects if "_low" in obj.name]

        if not selected_objects:
            self.report({'WARNING'}, "No selected objects with '_low' in their names.")
            return {'CANCELLED'}

        if not scene.appelation.strip():
            self.report({'ERROR'}, "Appellation cannot be empty. Please provide a name.")
            return {'CANCELLED'}

        export_path = os.path.join(scene.mesh_path.strip() or os.path.dirname(bpy.data.filepath), f"{scene.appelation}_low.fbx")

        if not os.path.exists(os.path.dirname(export_path)):
            self.report({'ERROR'}, f"Directory does not exist: {os.path.dirname(export_path)}")
            return {'CANCELLED'}

        # Store the original selection
        original_selection = bpy.context.selected_objects
        bpy.ops.object.select_all(action='DESELECT')

        # Select only '_low' objects
        for obj in selected_objects:
            obj.select_set(True)

        try:
            bpy.ops.export_scene.fbx(filepath=export_path, use_selection=True)
        except PermissionError:
            self.report({'ERROR'}, f"Permission denied: Unable to write to {export_path}.")
            return {'CANCELLED'}
        finally:
            # Restore original selection
            bpy.ops.object.select_all(action='DESELECT')
            for obj in original_selection:
                obj.select_set(True)

        self.report({'INFO'}, f"Exported successfully to: {export_path}")
        return {'FINISHED'}


Classes = (
    BAKINGSUPPLY_ExportHigh,
    BAKINGSUPPLY_ExportLow,
)

def register():
    for c in Classes:
        bpy.utils.register_class(c)

def unregister():
    for c in reversed(Classes):
        bpy.utils.unregister_class(c)

if __name__ == "__main__":
    register()
