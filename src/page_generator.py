import os
from markdown_blocks import markdown_to_html_node, extract_title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    # Read the markdown file
    with open(from_path, 'r', encoding='utf-8') as markdown_file:
        markdown_content = markdown_file.read()
    
    # Read the template file
    with open(template_path, 'r', encoding='utf-8') as template_file:
        template_content = template_file.read()
    
    # Convert markdown to HTML
    html_node = markdown_to_html_node(markdown_content)  # Assume this returns an object with a .to_html() method
    html_content = html_node.to_html()
    
    # Extract the title
    try:
        title = extract_title(markdown_content)
        
    except ValueError as e:
        print(f"Error extracting title: {e}")
        return

    # Replace placeholders in the template
    page_content = template_content.replace("{{ Title }}", title)
    page_content = page_content.replace("{{ Content }}", html_content)
    print(f"Final page content length: {len(page_content)}")
    # Ensure destination directory exists
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    #  Write the generated HTML to the destination file
    with open(dest_path, 'w', encoding='utf-8') as output_file:
        output_file.write(page_content)
    
    print("Page generated successfully.")

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for root, _, files in os.walk(dir_path_content):
        # Calculate the relative path of the current directory
        relative_path = os.path.relpath(root, dir_path_content)
        # Determine the corresponding path in the destination directory
        dest_path = os.path.join(dest_dir_path, relative_path)
        
        # Ensure the destination subdirectory exists
        os.makedirs(dest_path, exist_ok=True)
        
        for file in files:
            if file.endswith(".md"):  # Process only markdown files
                # Full path to the current markdown file
                markdown_file = os.path.join(root, file)
                # Generate the corresponding .html file path
                html_file_name = os.path.splitext(file)[0] + ".html"
                html_file_path = os.path.join(dest_path, html_file_name)

                print(f"Generating page from {markdown_file} to {html_file_path}")
                
                # Generate the page using the template
                generate_page(markdown_file, template_path, html_file_path)

