import bpy
import os


class BAKINGSUPPLY_ExportHigh(bpy.types.Operator):
    bl_idname = "object.export_selected_operator_high"
    bl_label = "Export Selected high"

    def execute(self, context):
        scene = context.scene
        selected_objects = []

        for obj in bpy.data.objects:
            if obj.select_get() and "high" in obj.name:
                selected_objects.append(obj)
            else:
                obj.select_set(False)

        if not selected_objects:
            self.report({'WARNING'}, "No objects selected with 'high' in their names.")
            return {'CANCELLED'}

        blend_filepath = bpy.data.filepath
        blend_dir = os.path.dirname(blend_filepath)

        export_filename = scene.appelation + "_high.fbx"
        export_path = os.path.join(blend_dir, export_filename)

        bpy.ops.export_scene.fbx(filepath=export_path, use_selection=True)

        return {'FINISHED'}
    
class BAKINGSUPPLY_ExportLow(bpy.types.Operator):
    bl_idname = "object.export_selected_operator_low"
    bl_label = "Export Selected low"

    def execute(self, context):
        scene = context.scene
        selected_objects = []

        for obj in bpy.data.objects:
            if obj.select_get() and "low" in obj.name:
                selected_objects.append(obj)
            else:
                obj.select_set(False)

        if not selected_objects:
            self.report({'WARNING'}, "No objects selected with 'low' in their names.")
            return {'CANCELLED'}

        blend_filepath = bpy.data.filepath
        blend_dir = os.path.dirname(blend_filepath)

        export_filename = scene.appelation + "_low.fbx"
        export_path = os.path.join(blend_dir, export_filename)

        bpy.ops.export_scene.fbx(filepath=export_path, use_selection=True)

        return {'FINISHED'}
 


class CustomPanel(bpy.types.Panel):
    bl_label = "High and Low exporter"
    bl_idname = "OBJECT_PT_custom_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Custom Addon'

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        # Display the "Appelation" variable
        layout.prop(scene, "appelation")



        # Add the export button
        layout.operator("object.export_selected_operator_high", text="Export High")
        layout.operator("object.export_selected_operator_low", text="Export low")



Classes = (
    BAKINGSUPPLY_ExportLow,
    BAKINGSUPPLY_ExportHigh
)

def register():
    for c in Classes:
        bpy.utils.register_class(c)


def unregister():
    for c in reversed(Classes):
        bpy.utils.unregister_class(c)
