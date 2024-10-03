import os
import shutil
from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime

# Supported image and video formats
IMAGE_EXTENSIONS = ('.jpg', '.jpeg', '.png')
VIDEO_EXTENSIONS = ('.mp4', '.avi', '.mov', '.mkv', '.flv')

def extract_date_taken(file_path):
    """Extract the date a photo was taken using EXIF data."""
    try:
        img = Image.open(file_path)
        exif_data = img._getexif()
        
        if exif_data:
            for tag, value in exif_data.items():
                tag_name = TAGS.get(tag, tag)
                if tag_name == "DateTimeOriginal":
                    return datetime.strptime(value, "%Y:%m:%d %H:%M:%S")
    except Exception as e:
        print(f"Error reading EXIF data for {file_path}: {e}")
    
    return None

def fallback_to_file_date(file_path):
    """Fallback to file creation or last modification date if EXIF data is unavailable."""
    try:
        # Get the file's modification time
        file_time = os.path.getmtime(file_path)
        return datetime.fromtimestamp(file_time)
    except Exception as e:
        print(f"Error getting file date for {file_path}: {e}")
    return None

def organize_photos_and_videos_by_date(src_directory, dest_directory):
    """Organize photos and videos by date, including subdirectories."""
    if not os.path.exists(dest_directory):
        os.makedirs(dest_directory)

    # Walk through all subdirectories and files
    for root, dirs, files in os.walk(src_directory):
        for file in files:
            file_path = os.path.join(root, file)
            
            # Check if file is an image or video
            if file.lower().endswith(IMAGE_EXTENSIONS + VIDEO_EXTENSIONS):
                
                # Try to extract the date from EXIF (for images) or fallback to file date (for both images and videos)
                if file.lower().endswith(IMAGE_EXTENSIONS):
                    date_taken = extract_date_taken(file_path)
                else:
                    date_taken = None
                
                if not date_taken:
                    # Fallback to file creation/modification date if EXIF data is not available (applies to both images and videos)
                    date_taken = fallback_to_file_date(file_path)
                
                if date_taken:
                    # Create folder in YYYY-MM format based on date
                    folder_name = date_taken.strftime("%Y-%m")
                    new_folder_path = os.path.join(dest_directory, folder_name)
                    
                    # Ensure the destination folder exists
                    if not os.path.exists(new_folder_path):
                        os.makedirs(new_folder_path)
                    
                    # Move the file to the new directory
                    new_file_path = os.path.join(new_folder_path, file)
                    shutil.move(file_path, new_file_path)
                    print(f"Moved {file} to {new_folder_path}")
                else:
                    print(f"Could not extract or fallback to date for {file}")

if __name__ == "__main__":
    source_directory = r"C:\Users\hp\Desktop\PICS"  # Replace with the path to your photos directory
    destination_directory = r"C:\Users\hp\Desktop\Dist"  # Replace with where you want to organize them
    
    organize_photos_and_videos_by_date(source_directory, destination_directory)
