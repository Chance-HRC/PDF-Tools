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
st.title("PDF Compression Tool")
st.divider()
st.write("Compress your PDF files to reduce their size")
st.divider()
uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")
st.divider()

if uploaded_file:
    compress_button = st.button("Compress PDF")

    if compress_button:
        try:
            pdf_reader = PdfReader(uploaded_file)
            pdf_writer = PdfWriter()

            for page in pdf_reader.pages:
                pdf_writer.add_page(page)

            pdf_writer._info.get_object().update({})

            compressed_pdf_io = io.BytesIO()
            pdf_writer.write(compressed_pdf_io)
            compressed_pdf_io.seek(0)

            st.success("PDF compression completed successfully!")
            st.divider()
            st.download_button(
                label="Download Compressed PDF",
                data=compressed_pdf_io,
                file_name="compressed_file.pdf",
                mime="application/pdf",
            )



        except Exception as e:
            st.error(f"An error occurred while compressing the PDF: {e}")
# --------------------------------------------------------------------------------