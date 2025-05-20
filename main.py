import streamlit as st
import qrcode
from PIL import Image
import io

def generate_qr_code(url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    qr_image = qr.make_image(fill_color="black", back_color="white")
    return qr_image

def main():
    st.title("URL to QR Code Generator")
    st.write("Enter a URL and get a downloadable QR code!")

    # URL input
    url = st.text_input("Enter URL:", placeholder="https://example.com")
    
    # Generate button
    if st.button("Generate QR Code"):
        if url:
            if not url.startswith(('http://', 'https://')):
                url = 'https://' + url
            
            # Generate QR code
            qr_image = generate_qr_code(url)
            
            # Convert PIL image to bytes
            img_byte_arr = io.BytesIO()
            qr_image.save(img_byte_arr, 'PNG')
            img_byte_arr = img_byte_arr.getvalue()

            # Display QR code
            st.image(img_byte_arr, caption='Generated QR Code')
            
            # Download button
            st.download_button(
                label="Download QR Code",
                data=img_byte_arr,
                file_name="qr_code.png",
                mime="image/png"
            )
        else:
            st.warning("Please enter a URL first!")

if __name__ == "__main__":
    main()
