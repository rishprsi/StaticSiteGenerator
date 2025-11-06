import os
import shutil

from textnode import TextNode
from markdown_to_htmlnode import markdown_to_htmlnode


def copy_files(source, destination):
    abs_source = os.path.abspath(source)
    abs_destination = os.path.abspath(destination)
    print(f"Current source: {abs_source}, Destination: {abs_destination}")

    if not os.path.exists(abs_source):
        raise ValueError("Source not valid or not present")

    if os.path.exists(abs_destination):
        shutil.rmtree(abs_destination)
    os.mkdir(abs_destination)

    files = os.listdir(abs_source)
    for file in files:
        abs_file = os.path.join(abs_source, file)
        dest_file = os.path.join(abs_destination, file)
        if os.path.isfile(abs_file):
            print(f"Copying from {abs_file} to {dest_file}")
            shutil.copy(abs_file, dest_file)
        elif os.path.isdir(abs_file):
            copy_files(abs_file, dest_file)


def extract_title(markdown):
    for line in markdown.split("\n"):
        if line.startswith("# "):
            return line[2:]
    raise Exception("Markdown doesn't have a title")


def generate_page_recursive(from_path, template_path, dest_path):
    abs_from = os.path.abspath(from_path)
    abs_template = os.path.abspath(template_path)
    abs_dest = os.path.abspath(dest_path)

    files = os.listdir(abs_from)
    for file in files:
        abs_read = os.path.join(abs_from, file)
        abs_write = os.path.join(abs_dest, file)
        print(f"Generating page from {abs_read} to {abs_write} using {template_path}")

        if os.path.isdir(abs_read):
            os.mkdir(abs_write)
            generate_page_recursive(abs_read, abs_template, abs_write)
            continue

        with open(abs_read, mode="r") as f:
            src_content = f.read()
            f.close()

        with open(abs_template, mode="r") as f:
            template_content = f.read()
            f.close()

        title = extract_title(src_content)
        html_node = markdown_to_htmlnode(src_content)
        html = html_node.to_html()

        template_content = template_content.replace("{{ Title }}", title)
        template_content = template_content.replace("{{ Content }}", html)

        abs_write = abs_write.replace(".md", ".html")
        with open(abs_write, mode="w") as f:
            f.write(template_content)
            f.close()


def main():
    copy_files("static", "public")
    generate_page_recursive("content", "template.html", "public")


if __name__ == "__main__":
    main()
