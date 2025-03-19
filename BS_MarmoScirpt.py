import mset

# Create new scene and baking project
mset.newScene()
baker = mset.BakerObject()

# Load high and low models
ModelLow = r"{low_fbx_safe}"
ModelHigh = r"{high_fbx_safe}"
baker.importModel(ModelHigh)
baker.importModel(ModelLow)

# Configure baking settings
baker.outputPath = r"{scene.appelation.strip()}.{scene.BS_FileFormat}"
baker.outputBits = 8
baker.outputSamples = {scene.BS_Sample}
baker.edgePadding = "Moderate"
baker.outputSoften = 0
baker.useHiddenMeshes = True
baker.ignoreTransforms = False
baker.smoothCage = True
baker.ignoreBackfaces = True
baker.tileMode = 0
baker.outputSinglePsd = {scene.BS_SinglePSD}

# Set texture resolution
baker.outputWidth = {scene.BS_ResX}
baker.outputHeight = {scene.BS_ResY}

# Apply preset
if scene.BS_Preset == "ASSETS":
    baker.loadPreset("Tarmunds_Asset.tbbake")
elif scene.BS_Preset == "TILEABLE":
    baker.loadPreset("Tarmunds_Tileable.tbbake")

print("Marmoset bake project created and models loaded.")