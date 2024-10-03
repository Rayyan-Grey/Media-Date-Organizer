# Media Date Organizer

A Python-based automation tool that organizes photos and videos into directories based on their capture or modification date. It supports various image and video formats, including `.jpg`, `.jpeg`, `.png`, `.mp4`, `.avi`, `.mov`, and more.

## Features

- Organizes images by extracting the capture date from EXIF metadata (if available).
- For videos or files without EXIF data, uses file creation/modification dates.
- Recursively searches through subdirectories to organize all media files.
- Creates date-based directories in `YYYY-MM` format for better file organization.
- Supports common image formats like `.jpg`, `.jpeg`, `.png` and video formats like `.mp4`, `.avi`, `.mov`, `.mkv`.

## Requirements

- Python 3.x
- Pillow (Python Imaging Library)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Rayyan-Grey/media-date-organizer.git
2. Navigate to the project directory:
   ```bash
   cd media-date-organizer
3. Install the required dependencies:

## Usage
- Open organize.py and modify the following lines to set the source and destination directories:
  ```bash
  if __name__ == "__main__":
    source_directory = "/path/to/your/source/folder"  # Replace with the path to your photos/videos folder
    destination_directory = "/path/to/your/destination/folder"  # Replace with the destination folder path
    
    organize_photos_and_videos_by_date(source_directory, destination_directory)

- Run the script:
  ```bash
  python organize.py
- The script will organize all media files into folders in the destination directory by date (e.g., 2024-09, 2024-08).

## Example

- Before running the tool:
  ```bash
  /source-folder/
  ├── photo1.jpg
  ├── video1.mp4
  ├── folder1/
  │   └── photo2.jpg

- After running the tool:
  ```bash
  /destination-folder/
  ├── 2024-09/
  │   ├── photo1.jpg
  │   └── video1.mp4
  ├── 2024-08/
  │   └── photo2.jpg

## Contributing

- Feel free to fork this repository and submit pull requests for improvements or additional features.
