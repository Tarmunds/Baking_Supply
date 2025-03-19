import bpy
import os
import subprocess
import tempfile

class BAKINGSUPPLY_ExportAndLaunchMarmoset(bpy.types.Operator):
    """Exports High and Low, then launches Marmoset 5 and loads them"""
    bl_idname = "object.bs_export_and_launch_marmoset"
    bl_label = "Export & Launch Marmoset"

    def execute(self, context):
        scene = context.scene

        # Ensure the appellation property is set
        if not scene.appelation.strip():
            self.report({'ERROR'}, "Appellation cannot be empty. Please provide a name.")
            return {'CANCELLED'}

        # Get export paths
        export_dir = scene.mesh_path.strip() if scene.mesh_path.strip() else os.path.dirname(bpy.data.filepath)
        high_fbx = os.path.abspath(os.path.join(export_dir, f"{scene.appelation}_high.fbx"))
        low_fbx = os.path.abspath(os.path.join(export_dir, f"{scene.appelation}_low.fbx"))

        # Run Export Operators
        bpy.ops.object.export_selected_operator_high()
        bpy.ops.object.export_selected_operator_low()

        # Path to Marmoset Toolbag 5 Executable (Update if necessary)
        marmoset_path = r"C:\Program Files\Marmoset\Toolbag 5\Toolbag.exe"

        if not os.path.exists(marmoset_path):
            self.report({'ERROR'}, f"Marmoset Toolbag 5 not found at: {marmoset_path}")
            return {'CANCELLED'}

        # Ensure paths are properly escaped for Marmoset
        high_fbx_safe = high_fbx.replace("\\", "\\\\")
        low_fbx_safe = low_fbx.replace("\\", "\\\\")

        # Create a temporary Marmoset Python script
        marmoset_script = tempfile.NamedTemporaryFile(delete=False, suffix=".py").name

        with open(marmoset_script, "w") as script_file:
            script_file.write(f"""import mset

def main():
    # Create a new scene
    mset.newScene()

    # Create a bake project
    bake_project = mset.BakerObject()

    # Set the auto-load files
    ModelLow = "{low_fbx_safe}"
    ModelHigh = "{high_fbx_safe}"

    # Enable auto-load files based on naming
    # bake_project.setAutoLoad(True)

    # Set the paths for the quick loader
    bake_project.importModel(ModelHigh)
    bake_project.importModel(ModelLow)

    print("Marmoset bake project created with auto-load enabled.")

# Run the script
main()
""")

        # Launch Marmoset with the script
        subprocess.Popen([marmoset_path, "-py", marmoset_script], shell=True)

        self.report({'INFO'}, "Marmoset Toolbag 5 launched and setup.")
        return {'FINISHED'}

# Register the new operator
def register():
    bpy.utils.register_class(BAKINGSUPPLY_ExportAndLaunchMarmoset)

def unregister():
    bpy.utils.unregister_class(BAKINGSUPPLY_ExportAndLaunchMarmoset)

if __name__ == "__main__":
    register()
