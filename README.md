# Baking Supply Addon for Blender

Welcome to **Baking Supply**, a small but powerful Blender addon designed to streamline your baking workflow by simplifying the back-and-forth process between Blender and your baking software. 

This addon was designed with the use of the [Quick Loader feature of Marmoset Toolbag](https://docs.marmoset.co/docs/baking-attributes/), but can be use with any other baking software.
This addon is released under the GNU General Public License v3.

![Baking Supply Panel](https://github.com/Tarmunds/Baking_Supply/blob/main/Images/Panel.png)

### Features

- **Hide Low/High Meshes**: Automatically detect and hide all meshes with `_low` or `_high` in their names, depending on the button you click.
- **Show Low/High Meshes**: Easily bring back visibility for low or high meshes with a single click.
- **Switch Suffix (`_high` <> `_low`)**: Quickly switch between `_high` and `_low` suffixes for selected objects, making it easy to manage naming conventions during your workflow.
- **Add Suffix (`_high` or `_low`)**: Add a `_high` or `_low` suffix to selected mesh objects to ensure they follow the correct naming convention.
- **Transfer Names**: Transfer the name from an active `_high` object to other selected objects, replacing `_high` with `_low` for consistent naming.
- **Export Meshes**: Export all the selected meshes marked with `_high` or `_low` to the location of your Blender file (or other path if setup), using a name that you can set directly in the panel.
- **Custom Export Path**: You can also define a custom path for exporting. If left empty, the addon will export the files to the same location as your Blender file.


### How to Install
1. **Download the Addon**: Download the [latest stable version of the addon on Gumroad](https://tarmunds.gumroad.com/l/hfkqe)
2. **Open Blender**: Open Blender and go to `Edit > Preferences > Add-ons`.
3. **Install the Addon**: Click on `Install...`, navigate to the downloaded `.zip` file, and select it.
4. **Activate the Addon**: Once installed, find the `Baking Supply` addon in the list and check the box to activate it.
5. **Access the Panel**: You can find the addon panel in the 3D View under the `Tarmunds Addons` tab.

### How to Use
1. **Hide/Show Meshes**: Use the Hide/Show buttons to quickly adjust the visibility of high and low meshes for easier navigation and manipulation.
![Hide/Show High or Low](https://github.com/Tarmunds/Baking_Supply/blob/main/Images/Show_Hide.gif)
2. **Switch Suffix**: Select the objects you want to rename and use the `High <> Low` button to toggle between `_high` and `_low` suffixes.
3. **Add Suffix**: Select the objects and use the `Add _high` or `Add _low` buttons to add the respective suffix to the selected meshes.
4. **Transfer Names**: Select a `_high` object as the active object, along with other target objects, and use the `Transfer Name` button to give them consistent `_low` names.
![Name Operator](https://github.com/Tarmunds/Baking_Supply/blob/main/Images/Name_Operator.gif)
5. **Exporting Meshes**: Enter a name in the panel, then use the export buttons to save all visible high or low meshes. Specify a custom path if needed. After the export. This is super useful when you're itering with the lowpoly to go back and forth with Marmoset.
![Export](https://github.com/Tarmunds/Baking_Supply/blob/main/Images/Export.gif)

### Learn more about bakin ?
If you're interested i made a tutorial to get a correct bake using marmoset toolbag, you can find it [here on my website](https://www.tarmunds.com/post/how-to-get-a-clean-bake)
![How to get a clean bake](https://static.wixstatic.com/media/6f5aea_1e42e84277704eac95f69953f4f3add5~mv2.png/v1/fill/w_1110,h_624,al_c,q_90,usm_0.66_1.00_0.01,enc_auto/6f5aea_1e42e84277704eac95f69953f4f3add5~mv2.png)


### License
This addon is licensed under the [GNU General Public License v3](https://www.gnu.org/licenses/gpl-3.0.html), meaning it is free to use, modify, and distribute.
Concept of the dagger by Baldi Konjin, you can find it [here](https://www.artstation.com/artwork/Le2Dl0)

### Contributing and Feedback
We are always open to suggestions for new tools or modifications. Feel free to join our community on [Discord](https://discord.gg/h39W5s5ZbQ) to share your ideas and feedback.

Happy baking!

— Tarmunds

