import pcbnew

DIODE_PREFIX = "D"
SWITCH_PREFIX = "SW"
MAX_NUMBER = 82

board = pcbnew.GetBoard()
switch_positions = {} # Dictionary to store SW positions: {number: position_vector}
diodes_moved_count = 0
switches_found_count = 0
diodes_processed_count = 0

print("Starting script to align diodes with switches...")

# --- Pass 1: Collect positions of all relevant switches (SW1 to SW82) ---
print(f"\n--- Pass 1: Finding switch positions ({SWITCH_PREFIX}1 to {SWITCH_PREFIX}{MAX_NUMBER}) ---")
for footprint in board.GetFootprints():
    ref = footprint.GetReference()
    if ref.startswith(SWITCH_PREFIX):
        try:
            # Extract the number from the designator (e.g., "SW1" -> 1)
            number_str = ref[len(SWITCH_PREFIX):]
            if number_str.isdigit():
                number = int(number_str)
                if 1 <= number <= MAX_NUMBER:
                    switch_positions[number] = footprint.GetPosition()
                    switches_found_count += 1
                    # print(f"Found switch: {ref} at {footprint.GetPosition()}") # Optional debug
        except ValueError:
            print(f"Warning: Could not parse number for switch: {ref}")
            continue

print(f"Found {switches_found_count} switch footprints matching the criteria.")

if not switch_positions:
    print("Error: No switch footprints found matching the criteria. Aborting.")
else:
    # --- Pass 2: Iterate through diodes (D1 to D82) and move them ---
    print(f"\n--- Pass 2: Moving diodes ({DIODE_PREFIX}1 to {DIODE_PREFIX}{MAX_NUMBER}) ---")
    for footprint in board.GetFootprints():
        ref = footprint.GetReference()
        if ref.startswith(DIODE_PREFIX):
            diodes_processed_count += 1
            try:
                # Extract the number from the designator (e.g., "D1" -> 1)
                number_str = ref[len(DIODE_PREFIX):]
                if number_str.isdigit():
                    number = int(number_str)
                    if 1 <= number <= MAX_NUMBER:
                        if number in switch_positions:
                            target_position = switch_positions[number]
                            current_position = footprint.GetPosition()
                            if current_position != target_position:
                                footprint.SetPosition(target_position)
                                diodes_moved_count += 1
                                print(f"Moved {ref} from {current_position} to {target_position} (center of {SWITCH_PREFIX}{number}).")
                            else:
                                print(f"{ref} is already at the correct position for {SWITCH_PREFIX}{number}.")
                        else:
                            print(f"Warning: Diode {ref} found, but corresponding switch {SWITCH_PREFIX}{number} not found. Skipping.")
            except ValueError:
                print(f"Warning: Could not parse number for diode: {ref}")
                continue

    print("\n--- Script Finished ---")
    print(f"Total diodes processed (D1-D{MAX_NUMBER}): {diodes_processed_count}")
    print(f"Total diodes moved: {diodes_moved_count}")

# Refresh the Pcbnew display to show the changes
pcbnew.Refresh()