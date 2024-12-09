# --------------------------------------------------------------------------------
# Imports
import streamlit as st
from PyPDF2 import PdfReader, PdfWriter
import io

# --------------------------------------------------------------------------------
# Sidebar portion
st.sidebar.title("IF THERE ARE ANY BUGS PLEASE CONTACT")
st.sidebar.markdown("@LUKE.FULLARD@HORIZONS.GOVT.NZ")
st.sidebar.image("HorizonsLogo.png")
# --------------------------------------------------------------------------------
# Function to encrypt PDF
def encrypt_pdf(pdf_file, password):
    reader = PdfReader(pdf_file)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    writer.encrypt(password)
    output = io.BytesIO()
    writer.write(output)
    output.seek(0)
    return output

# --------------------------------------------------------------------------------
st.title("PDF Encryption Tool")
st.divider()
st.write("This tool allows you to encrypt a PDF file with a password.")
st.divider()
pdf_file = st.file_uploader("Upload a PDF file to encrypt", type="pdf")
st.divider()

if pdf_file:
    password = st.text_input("Enter a password to encrypt the PDF:", type="password")

    if password and st.button("Encrypt PDF"):
        try:
            encrypted_pdf = encrypt_pdf(pdf_file, password)
            st.success("PDF encryption completed successfully!")
            st.divider()
            st.download_button(
                "Download Encrypted PDF",
                data=encrypted_pdf,
                file_name="encrypted.pdf",
                mime="application/pdf",
            )
        except Exception as e:
            st.error(f"An error occurred: {e}")
# --------------------------------------------------------------------------------