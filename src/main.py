import os
import shutil

from page_generator import generate_pages_recursive
from markdown_blocks import markdown_to_html_node

# source = static
# destination = public

def clear_directory(directory):
    # Deletes all contents of the given directory.
    if os.path.exists(directory):
        shutil.rmtree(directory)
    os.makedirs(directory)

def copy_directory(source, destination):
    # Copies all files and directories from source to destination.
    clear_directory(destination)

    for root, dirs, files in os.walk(source):
        relative_path = os.path.relpath(root, source)
        dest_path = os.path.join(destination, relative_path)

        os.makedirs(dest_path, exist_ok=True)

        for file in files:
            src_file = os.path.join(root, file)
            dest_file = os.path.join(dest_path, file)
            shutil.copy2(src_file, dest_file)
            print(f"Copied: {src_file} -> {dest_file}")

def main():
    # Define source and destination paths
    source_dir = "static"
    destination_dir = "public"
    markdown_file = "content/index.md"
    template_file = os.path.abspath("template.html")
    output_file = os.path.join(destination_dir, "index.html")

    clear_directory(destination_dir)
    copy_directory(source_dir, destination_dir)
    generate_pages_recursive("content", template_file, destination_dir)

    print(f"Template file path: {template_file}")

    print("Website generation completed.")

if __name__ == "__main__":
    main()


