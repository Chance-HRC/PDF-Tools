# --------------------------------------------------------------------------------
# Imports
import streamlit as st
from PyPDF2 import PdfReader, PdfWriter
import io

# --------------------------------------------------------------------------------
#sidebar
st.sidebar.title("IF THERE ARE ANY BUGS PLEASE CONTACT")
st.sidebar.markdown("@ChanceDehar@hotmail.com")
st.image("airport.png")
# --------------------------------------------------------------------------------
# Definitions

# Function to process the page range input
def page_selection(selection, total_pages):
    pages = []
    for part in selection.split(","):
        if "-" in part:
            start, end = map(int, part.split("-"))
            if start > total_pages or end > total_pages:
                raise ValueError("Page range exceeds the total number of pages.")
            pages.extend(range(start - 1, end))
        else:
            page = int(part) - 1
            if page >= total_pages:
                raise ValueError("Page number exceeds the total number of pages.")
            pages.append(page)
    return sorted(set(p for p in pages if 0 <= p < total_pages))


# Function to combine selected pages from multiple PDFs into one
def combine_pdfs(pdf_files, page_ranges):
    writer = PdfWriter()
    for pdf, ranges in zip(pdf_files, page_ranges):
        reader = PdfReader(pdf)
        for page in ranges:
            writer.add_page(reader.pages[page])
    output = io.BytesIO()
    writer.write(output)
    output.seek(0)
    return output


# --------------------------------------------------------------------------------
st.title("PDF Combine Tool")
st.divider()
st.write("This tool is used to combine different PDF files")
st.write("It can do multiple files and specific pages")
st.divider()
pdf_files = st.file_uploader("Upload PDF files", type="pdf", accept_multiple_files=True)
st.divider()

if pdf_files:
    set_all_ranges = st.text_input("Set all page ranges (e.g., 1-3,5):", "")
    page_ranges = []
    valid_input = True
    error_message = ""

    for pdf in pdf_files:
        total_pages = len(PdfReader(pdf).pages)
        default_range = set_all_ranges if set_all_ranges else f"1-{total_pages}"
        ranges = st.text_input(f"Pages for {pdf.name} (e.g., 1-3,5):", default_range)

        try:
            selected_pages = page_selection(ranges, total_pages)
            page_ranges.append(selected_pages)
        except ValueError as e:
            valid_input = False
            error_message = f"Error for {pdf.name}: {e}"
            st.error(error_message)
            break
    # --------------------------------------------------------------------------------
    # combine and download button
    st.divider()
    if valid_input and st.button("Combine PDFs"):
        combined_pdf = combine_pdfs(pdf_files, page_ranges)
        st.success("PDF combine completed successfully!")
        st.divider()
        st.download_button("Download Combined PDF", data=combined_pdf, file_name="combined.pdf", mime="application/pdf")
# --------------------------------------------------------------------------------