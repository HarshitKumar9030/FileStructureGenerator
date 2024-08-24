
# FileStructureGenerator

A versatile and customizable command-line tool to generate file structures for various types of projects. This tool supports multiple languages and frameworks, allowing you to visualize your project's file tree while ignoring unnecessary directories like `node_modules`, `.env`, and others.

## Features

- **Multi-Language Support:** Handles file structure generation for Python, Next.js, Node.js, Express, React, Django, Angular, Flutter, and many more.
- **Sophisticated Ignore Logic:** Automatically skips directories and files that are typically ignored for each project type.
- **Depth Control:** Specify the depth of the file structure displayed.
- **Pretty Print:** Outputs the file structure with emojis for better readability.

## Supported Project Types

The following project types are supported:

- Python
- Next.js
- Node.js
- Express
- Flutter
- Django
- React
- Angular
- Vue.js
- Ruby
- Java
- Spring Boot
- PHP
- Laravel
- Go
- Rust
- C#
- C++
- Kotlin
- Swift
- .NET
- Svelte
- Electron

## Installation

Clone the repository:

\`\`\`bash
git clone https://github.com/HarshitKumar9030/FileStructureGenerator.git
cd FileStructureGenerator
\`\`\`

## Usage

To generate the file structure for a given project:

\`\`\`bash
python generate_file_structure.py --source=/path/to/your/project --type=nextjs --depth=3
\`\`\`

### Arguments

- \`--source\`: Path to the source directory (required).
- \`--type\`: Type of the project (required). Available options include: \`python\`, \`nextjs\`, \`nodejs\`, \`express\`, \`flutter\`, and many others.
- \`--depth\`: Maximum depth of the file structure (optional). Default is unlimited.

### Example Output

```bash
📁 my-react-app
    📂 src
        📂 components
            📄 Header.js
            📄 Footer.js
        📄 App.js
        📄 index.js
    📂 public
        📄 index.html
        📄 favicon.ico
    📄 package.json
    📄 README.md
```

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

1. Fork the repository
2. Create your feature branch (\`git checkout -b feature/your-feature\`)
3. Commit your changes (\`git commit -m 'Add some feature'\`)
4. Push to the branch (\`git push origin feature/your-feature\`)
5. Open a pull request

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
