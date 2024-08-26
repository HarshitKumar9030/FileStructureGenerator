import argparse
from generate_structure import generate_structure
from ignore_config import get_ignore_files

def main():
    parser = argparse.ArgumentParser(description="Generate a file structure of a project with sophisticated options.")
    parser.add_argument("--source", required=True, help="Path to the source directory.")
    parser.add_argument("--type", required=True, choices=get_ignore_files().keys(), help="Type of the project (e.g., python, nextjs, nodejs, etc.).")
    parser.add_argument("--depth", type=int, default=-1, help="Specify the depth to show the structure (e.g., --depth=2). Default is unlimited.")

    args = parser.parse_args()

    ignore_files = get_ignore_files().get(args.type, [])

    print(f"📁 {os.path.basename(args.source)}")

    generate_structure(args.source, ignore_files, max_depth=args.depth)

if __name__ == "__main__":
    main()
