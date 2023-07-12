import os
import csv
from PyPDF2 import PdfReader


def process_pdfs(directory):
    # Create a CSV file for storing the extracted data
    output_csv = "pdf_data.csv"

    # Open the CSV file in write mode
    with open(output_csv, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Author", "Title", "Subject", "Content"])

        # Iterate through each PDF file in the directory
        for filename in os.listdir(directory):
            if filename.endswith(".pdf"):
                pdf_path = os.path.join(directory, filename)

                # Open the PDF file
                with open(pdf_path, "rb") as pdf_file:
                    try:
                        pdf = PdfReader(pdf_file)

                        # Extract metadata
                        author = pdf.metadata.author
                        title = pdf.metadata.title
                        subject = pdf.metadata.subject

                        # Extract content from each page
                        content = ""
                        for page_number in range(len(pdf.pages)):
                            content += pdf.pages[page_number].extract_text()

                        # Write the extracted data to the CSV file
                        writer.writerow([author, title, subject, content])

                        print(f"Processed {filename}")
                    except Exception as e:
                        print(f"Error processing {filename}: {str(e)}")

    print("Extraction complete. CSV file generated.")


if __name__ == '__main__':
    directory_path = "./documents"
    process_pdfs(directory_path)
