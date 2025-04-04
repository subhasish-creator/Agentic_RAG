import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')
project_name='Agentic_RAG'

list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    "config/config.yaml",
    "param.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "code/trial.ipynb",
    "templates/index.html",
    "static/style.css",
    "test.py"

]
for file_path in list_of_files:
    # Create directories if they don't exist
    directory = os.path.dirname(file_path)
    if directory != "":
        os.makedirs(directory, exist_ok=True)

    # Create file with placeholder if not exist
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            content = f"# Auto-generated: {file_path}" if file_path.endswith(".py") else ""
            f.write(content)
        print(f"✅ Created: {file_path}")
    else:
        print(f"⚠️ Already exists: {file_path}")
        

