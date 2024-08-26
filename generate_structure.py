import os

def generate_structure(root_dir, ignore_files, indent="", max_depth=-1, current_depth=0):
    try:
        if max_depth != -1 and current_depth > max_depth:
            return

        items = sorted(os.listdir(root_dir))
        total_items = len(items)
        
        for index, item in enumerate(items):
            path = os.path.join(root_dir, item)

            if any(ignored in path for ignored in ignore_files):
                continue

            is_last_item = index == total_items - 1
            connector = "└──" if is_last_item else "├──"

            if os.path.isdir(path):
                print(f"{indent}{connector} 📂 {item}")
                new_indent = indent + ("    " if is_last_item else "│   ")
                generate_structure(path, ignore_files, new_indent, max_depth, current_depth + 1)
            else:
                print(f"{indent}{connector} 📄 {item}")
    except PermissionError:
        print(f"{indent}[Permission Denied]")