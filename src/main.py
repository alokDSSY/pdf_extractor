import argparse
import os
from extractor import FurnitureDataExtractor
from image_extractor import extract_images


def main():
    # Determine repository root (parent directory of src)
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    data_dir = os.path.join(BASE_DIR, "data")
    image_dir = os.path.join(BASE_DIR, "image")

    # Create data and image directories if they don't exist
    os.makedirs(data_dir, exist_ok=True)
    os.makedirs(image_dir, exist_ok=True)

    parser = argparse.ArgumentParser(
        description="Extract furniture product data and images from a PDF."
    )
    parser.add_argument(
        "pdf_file",
        nargs="?",
        default="Timeless-2021-Indoor-&-Outdoor-reduced.pdf",
        help="Path to the PDF file to process. Default: Timeless-2021-Indoor-&-Outdoor-reduced.pdf"
    )
    parser.add_argument(
        "--output-json",
        default=os.path.join(data_dir, "furniture_data.json"),
        help="Output JSON file for product data (default: data/furniture_data.json)."
    )
    parser.add_argument(
        "--output-csv",
        default=os.path.join(data_dir, "furniture_data.csv"),
        help="Output CSV file for product data (default: data/furniture_data.csv)."
    )
    parser.add_argument(
        "--images-dir",
        default=image_dir,
        help="Directory to save extracted images (default: image)."
    )

    args = parser.parse_args()

    # Extract product data from the PDF
    extractor = FurnitureDataExtractor(args.pdf_file)
    products = extractor.extract_data()
    extractor.save_to_json(args.output_json)
    extractor.save_to_csv(args.output_csv)
    print(f"Data extraction complete. Files saved as '{args.output_json}' and '{args.output_csv}'.")

    # Always extract images from the PDF
    extract_images(args.pdf_file, args.images_dir)
    print(f"Image extraction complete. Images saved in '{args.images_dir}'.")


if __name__ == "__main__":
    main()
