import bpy
import os
import subprocess
import tempfile

class BAKINGSUPPLY_ExportAndLaunchMarmoset(bpy.types.Operator):
    """Exports High and Low, then launches Marmoset Toolbag and loads them"""
    bl_idname = "object.bs_export_and_launch_marmoset"
    bl_label = "Export & Launch Marmoset"

    def execute(self, context):
        scene = context.scene
        addon_prefs = bpy.context.preferences.addons.get(__package__)
        
        if not addon_prefs:
            self.report({'ERROR'}, "Failed to retrieve Baking Supply addon preferences.")
            return {'CANCELLED'}
        
        marmoset_path = addon_prefs.preferences.marmoset_path

        if not marmoset_path or not os.path.exists(marmoset_path):
            self.report({'ERROR'}, f"Marmoset Toolbag not found at: {marmoset_path}. Please set the correct path in Preferences.")
            return {'CANCELLED'}

        if not scene.appelation.strip():
            self.report({'ERROR'}, "Appellation cannot be empty. Please provide a name.")
            return {'CANCELLED'}

        export_dir = scene.mesh_path.strip() if scene.mesh_path.strip() else os.path.dirname(bpy.data.filepath)
        high_fbx = os.path.abspath(os.path.join(export_dir, f"{scene.appelation}_high.fbx"))
        low_fbx = os.path.abspath(os.path.join(export_dir, f"{scene.appelation}_low.fbx"))

        # Run Export Operators
        bpy.ops.object.export_selected_operator_high()
        bpy.ops.object.export_selected_operator_low()

        # Ensure paths are properly formatted
        high_fbx_safe = high_fbx.replace("\\", "\\\\")
        low_fbx_safe = low_fbx.replace("\\", "\\\\")

        # Create a temporary Marmoset Python script
        marmoset_script = tempfile.NamedTemporaryFile(delete=False, suffix=".py").name

        with open(marmoset_script, "w") as script_file:
            script_file.write(f"""import mset

def main():
    mset.newScene()
    bake_project = mset.BakerObject()
    ModelLow = "{low_fbx_safe}"
    ModelHigh = "{high_fbx_safe}"
    bake_project.importModel(ModelHigh)
    bake_project.importModel(ModelLow)
    print("Marmoset bake project created and models loaded.")

main()
""")

        subprocess.Popen([marmoset_path, "-py", marmoset_script], shell=True)

        self.report({'INFO'}, "Marmoset Toolbag launched and setup.")
        return {'FINISHED'}

# Register the new operator
def register():
    bpy.utils.register_class(BAKINGSUPPLY_ExportAndLaunchMarmoset)

def unregister():
    bpy.utils.unregister_class(BAKINGSUPPLY_ExportAndLaunchMarmoset)

if __name__ == "__main__":
    register()
