def process_file(input_file: str, output_file: str):
    try:
        
        with open(input_file, "r", encoding="utf-8") as f:
            content = f.read()

        processed_content = content.upper()

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(processed_content)

        print(f"Processing complete. Output saved to '{output_file}'")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    input_filename = "input.txt"
    output_filename = "output.txt"

    process_file(input_filename, output_filename)