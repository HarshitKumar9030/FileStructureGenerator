import os
import argparse

# Change this manually according to your needs!

ignore_map = {
    "python": ["__pycache__", ".venv", ".env", ".pytest_cache", ".mypy_cache", ".vscode", ".idea",  ".git"],
    "nextjs": ["node_modules", ".next", "out", ".env", ".vscode", ".idea", ".git"],
    "nodejs": ["node_modules", ".env", ".vscode", ".idea",  ".git"],
    "express": ["node_modules", ".env", ".vscode", ".idea"],
    "flutter": ["build", ".dart_tool", ".vscode", ".idea"],
    "django": ["__pycache__", "venv", ".env", "db.sqlite3", "staticfiles", ".vscode", ".idea"],
    "react": ["node_modules", ".env", "build", "dist", ".vscode", ".idea"],
    "angular": ["node_modules", "dist", ".env", ".vscode", ".idea"],
    "vue": ["node_modules", "dist", ".env", ".vscode", ".idea"],
    "ruby": [".bundle", "log", "tmp", "vendor/bundle", ".vscode", ".idea"],
    "java": ["target", ".idea", ".vscode", "bin", "out"],
    "springboot": ["target", ".idea", ".vscode", "bin", "out"],
    "php": ["vendor", "node_modules", ".env", ".vscode", ".idea"],
    "laravel": ["vendor", "node_modules", ".env", ".vscode", ".idea", "storage"],
    "go": ["vendor", ".vscode", ".idea"],
    "rust": ["target", ".vscode", ".idea"],
    "csharp": ["bin", "obj", ".vs", ".vscode", ".idea"],
    "cpp": ["build", ".vscode", ".idea"],
    "kotlin": ["build", ".gradle", ".idea", ".vscode"],
    "swift": ["build", ".vscode", ".idea"],
    "dotnet": ["bin", "obj", ".vs", ".vscode", ".idea"],
    "flutter": ["build", ".dart_tool", ".vscode", ".idea"],
    "svelte": ["node_modules", "public/build", ".vscode", ".idea"],
    "electron": ["node_modules", "dist", ".env", ".vscode", ".idea"],
}

def generate_structure(root_dir, ignore_files, indent="", max_depth=-1, current_depth=0):
    try:
        if max_depth != -1 and current_depth > max_depth:
            return

        items = sorted(os.listdir(root_dir))
        
        for index, item in enumerate(items):
            path = os.path.join(root_dir, item)

            if any(ignored in path for ignored in ignore_files):
                continue

            if os.path.isdir(path):
                print(f"{indent}📂 {item}")
                generate_structure(path, ignore_files, indent + "    ", max_depth, current_depth + 1)
            else:
                print(f"{indent}📄 {item}")
    except PermissionError:
        pass

def main():
    parser = argparse.ArgumentParser(description="Generate a file structure of a project with sophisticated options.")
    parser.add_argument("--source", required=True, help="Path to the source directory.")
    parser.add_argument("--type", required=True, choices=list(ignore_map.keys()), help="Type of the project (e.g., python, nextjs, nodejs, etc.).")
    parser.add_argument("--depth", type=int, default=-1, help="Specify the depth to show the structure (e.g., --depth=2). Default is unlimited.")
    
    args = parser.parse_args()

    ignore_files = ignore_map.get(args.type, [])

    print(f"📁 {os.path.basename(args.source)}")

    generate_structure(args.source, ignore_files, max_depth=args.depth)

if __name__ == "__main__":
    main()
