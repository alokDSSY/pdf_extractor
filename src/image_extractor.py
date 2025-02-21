import fitz
import os


def extract_images(pdf_path: str, output_dir: str = "image"):
    """
    Extracts images from a PDF and saves them to the specified output directory.

    Args:
        pdf_path (str): The path to the PDF file.
        output_dir (str): The directory where images will be saved.
    """
    pdf_path = r'Timeless-2021-Indoor-&-Outdoor-reduced.pdf'

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    document = fitz.open(pdf_path)
    for page_index in range(len(document)):
        page = document[page_index]
        image_list = page.get_images(full=True)
        if image_list:
            print(f"[+] Found {len(image_list)} images on page {page_index}")
        else:
            print(f"[!] No images found on page {page_index}")
        for image_index, img in enumerate(image_list, start=1):
            xref = img[0]
            base_image = document.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            image_filename = os.path.join(output_dir, f"image{page_index + 1}_{image_index}.{image_ext}")
            with open(image_filename, "wb") as image_file:
                image_file.write(image_bytes)
                print(f"[+] Saved image as {image_filename}")
    document.close()
