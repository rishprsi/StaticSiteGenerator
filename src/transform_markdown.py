def extract_title(markdown):
    for line in markdown.split("\n"):
        if line.startswith("# "):
            return line[2:]
    raise Exception("Markdown doesn't have a title")


def generate_page(from_path, template_path, dest_path):
    pass
