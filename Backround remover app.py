import streamlit as st
from rembg import remove
from PIL import Image
import io
st.header("Pictures Backround Remover")

def removebg(img):
    input_img=Image.open(img)
    return remove(input_img)

def main():
    st.title("Backroundround Remover app")
    uploaded_file=st.file_uploader("Choose an Image...",type=["jpg","jpng","png"])

    if uploaded_file is not None:
        st.image(uploaded_file,caption='uploaded image')
        st.write("processing image")

        result=removebg(uploaded_file)
        st.image(result,caption="result")

        result_bytes=io.BytesIO()
        result.save(result_bytes,format='png')
        download_button=st.download_button(
            label="Download Image",
            data=result_bytes.getvalue(),
            file_name="image.png",
            key="download_button",
        )



if __name__=='__main__':
    main()