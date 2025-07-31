import pcbnew

# The full footprint name including the library
# Format: "LibraryName:FootprintName"
TARGET_LIBRARY_NAME = "Diode_SMD"
TARGET_FOOTPRINT_ITEM_NAME = "D_0402_1005Metric_Pad0.77x0.64mm_HandSolder"

board = pcbnew.GetBoard()
selected_count = 0

print(f"Searching for footprint: {TARGET_LIBRARY_NAME}:{TARGET_FOOTPRINT_ITEM_NAME}")

for footprint in board.GetFootprints():
    # Get the library and item name for older KiCad versions
    # These often return wxString, so .wx_str() or .AsString() is needed
    try:
        # KiCad 6 often uses .AsUTF8() or .AsString()
        # KiCad 5 often uses .wx_str()
        lib_nickname = footprint.GetFPID().GetLibNickname().AsUTF8() # Try .AsString() or .wx_str() if this fails
        item_name = footprint.GetFPID().GetLibItemName().AsUTF8()   # Try .AsString() or .wx_str() if this fails
    except AttributeError:
        # Fallback for very old versions or if AsUTF8 isn't the one
        try:
            lib_nickname = footprint.GetFPID().GetLibNickname().wx_str()
            item_name = footprint.GetFPID().GetLibItemName().wx_str()
        except AttributeError:
            print("Error: Could not get library/item name. Your KiCad version might have a different API.")
            continue # Skip this footprint if we can't get its name

    if lib_nickname == TARGET_LIBRARY_NAME and item_name == TARGET_FOOTPRINT_ITEM_NAME:
        footprint.SetSelected()
        selected_count += 1
        # print(f"Selected: {footprint.GetReference()} ({lib_nickname}:{item_name})") # Optional

if selected_count > 0:
    print(f"Successfully selected {selected_count} instance(s) of '{TARGET_LIBRARY_NAME}:{TARGET_FOOTPRINT_ITEM_NAME}'.")
else:
    print(f"No instances of '{TARGET_LIBRARY_NAME}:{TARGET_FOOTPRINT_ITEM_NAME}' found on the board.")

# Refresh the Pcbnew display to show the selection
pcbnew.Refresh()