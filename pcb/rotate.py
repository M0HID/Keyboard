import pcbnew

TARGET_LIBRARY_NAME = "Keebio-Parts"
TARGET_FOOTPRINT_ITEM_NAME = "SK6812-MINI-E"
ROTATION_DEGREES =180

board = pcbnew.GetBoard()
rotated_count =0

designators_to_rotate = list(range(97,112)) + list(range(127,141)) + list(range(155,165))

print(f"Rotating {TARGET_LIBRARY_NAME}:{TARGET_FOOTPRINT_ITEM_NAME} footprints by {ROTATION_DEGREES} degrees around their centers...")

for footprint in board.GetFootprints():
    lib_nickname = footprint.GetFPID().GetLibNickname().wx_str() 
    item_name = footprint.GetFPID().GetLibItemName().wx_str() 
    print(f"Processing footprint: {footprint.GetReference()}")
    if lib_nickname == TARGET_LIBRARY_NAME and item_name == TARGET_FOOTPRINT_ITEM_NAME:
        ref = footprint.GetReference()                                 
        try:
            ref_number = int(ref[1:]) # Convert designator to number
            print(f"  Designator number: {ref_number}")
            if ref_number in designators_to_rotate:
                print(f"  Rotating footprint: {footprint.GetReference()}")
                footprint.SetOrientationDegrees(footprint.GetOrientationDegrees() + ROTATION_DEGREES)
                rotated_count +=1
        except ValueError:
            print(f"  Skipped {ref} (invalid designator).")

print(f"Rotated {rotated_count} instances of '{TARGET_LIBRARY_NAME}:{TARGET_FOOTPRINT_ITEM_NAME}' by {ROTATION_DEGREES} degrees.")

pcbnew.Refresh()