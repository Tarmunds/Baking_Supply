import mset

mset.newScene()
baker = mset.BakerObject()

{f'baker.importModel(r"{low_fbx_safe}")' if low_selected else ''}
{f'baker.importModel(r"{high_fbx_safe}")' if high_selected else ''}

baker.outputPath = r"{output_path}"
baker.outputBits = {output_bits}
baker.outputSamples = {output_samples}
baker.edgePadding = "Moderate"
baker.outputSoften = 0
baker.useHiddenMeshes = True
baker.ignoreTransforms = False
baker.smoothCage = True
baker.ignoreBackfaces = True
baker.tileMode = 0
baker.outputSinglePsd = {output_single_psd}
baker.outputBits = {output_depth}

baker.outputWidth = {output_width}
baker.outputHeight = {output_height}

if {use_preset}:
    if "{preset}" == "ASSETS":
        baker.loadPreset(r"{asset_preset_safe}")
    elif "{preset}" == "TILEABLE":
        baker.loadPreset(r"{tileable_preset_safe}")
else:
    baker.loadPreset(r"%appdata%\Local\Marmoset Toolbag 5\baker\Default.tbbake")

normal_map = None
for map in baker.getAllMaps():
    if isinstance(map, mset.NormalBakerMap):  # Check class type instead of `type` attribute
        normal_map = map
        break

materials = mset.findNodes(type="Material")
# Find the material named "Default"
default_material = next((mat for mat in materials if mat.name == "Default"), None)


if normal_map:
    normal_map.flipY = {NormalDirection}
    if default_material:
        default_material.setProperty("normalFlipY", True)
        print("Flip Y for normals enabled on Default material.")
    else:
        print("Default material not found.")


print("Marmoset bake project created and models loaded.")

if {quickbake}:
    baker.bake()
    baker.applyPreviewMaterial()