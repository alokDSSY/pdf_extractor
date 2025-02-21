import fitz
import re
import pandas as pd
import json


class FurnitureDataExtractor:
    """
    A class to extract furniture product information from PDF documents.
    """

    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path
        self.products = []

    def extract_data(self):
        """
        Extracts product data from the PDF.

        Returns:
            A list of dictionaries, each containing product details.
        """
        document = fitz.open(self.pdf_path)
        for page in document:
            text = page.get_text("text")
            self._parse_page(text)
        document.close()
        return self.products

    def _parse_page(self, text: str):
        """
        Parses a single page of text to extract product details.
        """
        lines = text.split('\n')
        product = {}
        for line in lines:
            if self._is_product_name(line):
                if product:
                    self.products.append(product)
                    product = {}
                product['Product Name'] = line.strip()
            elif self._is_description(line):
                product['Description'] = line.strip()
            elif self._is_dimensions(line):
                product['Dimensions'] = line.strip()
            elif self._is_image_link(line):
                product['Image Link'] = line.strip()
        if product:
            self.products.append(product)

    def _is_product_name(self, line: str) -> bool:
        """
        Determines if the line represents a product name.
        """
        return line.isupper() or len(line.split()) < 5

    def _is_description(self, line: str) -> bool:
        """
        Determines if the line represents a product description.
        """
        return len(line) > 10 and any(c.islower() for c in line)

    def _is_dimensions(self, line: str) -> bool:
        """
        Determines if the line represents product dimensions.
        """
        return bool(re.search(r'\d+\s*x\s*\d+', line))

    def _is_image_link(self, line: str) -> bool:
        """
        Determines if the line contains an image link.
        """
        return 'http' in line or 'www' in line

    def save_to_json(self, output_path: str):
        """
        Saves extracted product data to a JSON file.
        """
        with open(output_path, 'w') as json_file:
            json.dump(self.products, json_file, indent=4)

    def save_to_csv(self, output_path: str):
        """
        Saves extracted product data to a CSV file.
        """
        df = pd.DataFrame(self.products)
        df.to_csv(output_path, index=False)
