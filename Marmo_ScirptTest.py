import mset

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