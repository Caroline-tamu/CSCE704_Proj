#!/bin/bash

# Define the folders
SOURCE_FOLDER="gw"
TARGET_FOLDER="evade.me"

# Maximum allowed file size in bytes (5MB = 5242880 bytes)
MAX_SIZE=5242880

# Detect the platform (Linux or macOS) for the `stat` command
if [[ "$(uname)" == "Darwin" ]]; then
    STAT_CMD="stat -f%z"  # macOS
else
    STAT_CMD="stat -c%s"  # Linux
fi

# Ensure both folders exist
if [[ ! -d "$SOURCE_FOLDER" || ! -d "$TARGET_FOLDER" ]]; then
    echo "Error: One or both folders do not exist."
    exit 1
fi

# Loop through all files in the target folder
for TARGET_FILE in "$TARGET_FOLDER"/*; do
    # Ensure it's a regular file
    if [[ -f "$TARGET_FILE" ]]; then
        # Get the current size of the target file
        TARGET_SIZE=$($STAT_CMD "$TARGET_FILE")

        # Loop through all files in the source folder
        for SOURCE_FILE in "$SOURCE_FOLDER"/*; do
            # Ensure it's a regular file
            if [[ -f "$SOURCE_FILE" ]]; then
                # Get the size of the source file
                SOURCE_SIZE=$($STAT_CMD "$SOURCE_FILE")

                # Calculate the new size if the source file is appended
                NEW_SIZE=$((TARGET_SIZE + SOURCE_SIZE))

                # Check if the new size would exceed the limit
                if (( NEW_SIZE <= MAX_SIZE )); then
                    # Append the source file content to the target file
                    cat "$SOURCE_FILE" >> "$TARGET_FILE"
                    TARGET_SIZE=$NEW_SIZE  # Update the target size
                    echo "Appended $SOURCE_FILE to $TARGET_FILE (New size: $TARGET_SIZE bytes)"
                else
                    echo "Skipping append of $SOURCE_FILE to $TARGET_FILE (Exceeds 5MB)"
                fi
            fi
        done

        # Final check: truncate if the file exceeds 5MB
        FINAL_SIZE=$($STAT_CMD "$TARGET_FILE")
        if (( FINAL_SIZE > MAX_SIZE )); then
            echo "Truncating $TARGET_FILE to 5MB"
            head -c $MAX_SIZE "$TARGET_FILE" > "${TARGET_FILE}.bin" && mv "${TARGET_FILE}.bin" "$TARGET_FILE"
        fi
    fi
done
