from pathlib import Path

current_directory = Path.cwd()  # cwd = current working directory, it returns the path of the current working directory.

# __file__ is a special variable automatically created by Python when a script is executed.
current_file = Path(__file__).name  # __file__ = the file Python is currently running

print(f"Files in {current_directory}: ")

# Skips the python file
for filepath in current_directory.iterdir():
    if filepath.name == current_file:
        continue

    # Still in the loop!
    print(f" - {filepath.name}")
    if filepath.is_file():
        content = filepath.read_text(encoding="utf-8")
        print(f"Content: {content}")

