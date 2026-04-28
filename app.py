import streamlit as st
import numpy as np
from PIL import Image
import cv2
import io
result=None

img=Image.open("imageProcessing_output_24.ico")
st.set_page_config(
    page_title="Morphological operations",
    page_icon=img,
    layout="wide"
)

def erosion(test_img, element_size, kernel_size):
    global result
    if element_size == 0:
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
    elif element_size == 1:
        kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (kernel_size, kernel_size))
    elif element_size == 2:
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (kernel_size, kernel_size))
    elif element_size == 3:
        kernel = cv2.getStructuringElement(cv2.MORPH_DIAMOND, (kernel_size, kernel_size))
    result = cv2.erode(test_img, kernel)
    st.header("Erosion")
    st.image(result, width="stretch")
    

def dilation(test_img, element_size, kernel_size):
    global result
    if element_size == 0:
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
    elif element_size == 1:
        kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (kernel_size, kernel_size))
    elif element_size == 2:
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (kernel_size, kernel_size))
    elif element_size == 3:
        kernel = cv2.getStructuringElement(cv2.MORPH_DIAMOND, (kernel_size, kernel_size))
    result = cv2.dilate(test_img, kernel)
    st.header("Dilation")
    st.image(result, width="stretch")

def opening(test_img, element_size, kernel_size):
    global result
    if element_size == 0:
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
    elif element_size == 1:
        kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (kernel_size, kernel_size))
    elif element_size == 2:
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (kernel_size, kernel_size))
    elif element_size == 3:
        kernel = cv2.getStructuringElement(cv2.MORPH_DIAMOND, (kernel_size, kernel_size))
    result = cv2.morphologyEx(test_img, cv2.MORPH_OPEN, kernel)
    st.header("Opening")
    st.image(result, width="stretch")

def closing(test_img, element_size, kernel_size):
    global result
    if element_size == 0:
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
    elif element_size == 1:
        kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (kernel_size, kernel_size))
    elif element_size == 2:
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (kernel_size, kernel_size))
    elif element_size == 3:
        kernel = cv2.getStructuringElement(cv2.MORPH_DIAMOND, (kernel_size, kernel_size))
    result = cv2.morphologyEx(test_img, cv2.MORPH_CLOSE, kernel)
    st.header("Closing")
    st.image(result, width="stretch")

def gradient(test_img, element_size, kernel_size):
    global result
    if element_size == 0:
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
    elif element_size == 1:
        kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (kernel_size, kernel_size))
    elif element_size == 2:
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (kernel_size, kernel_size))
    elif element_size == 3:
        kernel = cv2.getStructuringElement(cv2.MORPH_DIAMOND, (kernel_size, kernel_size))
    result = cv2.morphologyEx(test_img, cv2.MORPH_GRADIENT, kernel)
    st.header("Gradient")
    st.image(result, width="stretch")
            


def on_selection_change(test_img, options, selected, element_size, kernel_size):
    if selected == options[0]:
        erosion(test_img, element_size, kernel_size)
    elif selected == options[1]:
        dilation(test_img, element_size, kernel_size)
    elif selected == options[2]:
        opening(test_img, element_size, kernel_size)
    elif selected == options[3]:
        closing(test_img, element_size, kernel_size)
    elif selected == options[4]:
        gradient(test_img, element_size, kernel_size)

with st.popover("INSTRUCTIONS"):
    st.write("### 📚 How to Use This App")

    st.write("**1. Upload an Image**")
    st.write("Click on 'Select Image File' and upload any image (JPG, JPEG, PNG, BMP). This will be your input image for processing.")
    st.write("**2. Choose a Morphological Operation**")
    st.write("Select an operation like Erosion, Dilation, Opening, Closing, or Gradient. Each operation modifies the image differently (e.g., erosion shrinks objects, dilation expands them).")

    st.write("**3. Select Element Shape**")
    st.write("This defines the structuring element (kernel shape) used in processing:")
    st.write("- Rect → Square shape (general purpose)")
    st.write("- Cross → Cross shape (preserves thin structures)")
    st.write("- Ellipse → Circular shape (smoother results)")
    st.write("- Diamond → Diamond shape (balanced effect)")

    st.write("**4. Adjust Kernel Size**")
    st.write("Use the slider to control the size of the kernel:")
    st.write("- Smaller values → subtle changes")
    st.write("- Larger values → stronger effects")
    st.write("Actual kernel size is displayed below the slider.")
    st.info("**📱 Note for Mobile Users:** Because phone screens have very high pixel density (PPI), you may need to use a **larger kernel value** (30-50) to see the same visual effect that appears at smaller values on a computer.")

    st.write("**5. Apply and Download Result**")
    st.write("Click 'Apply Operation' to process the image.")
    st.write("View original vs processed image side-by-side.")
    st.write("Download your result as a PNG file. If you need a different format, you can use a free online converter or another app to change it.")
    
#Single Image file uploader 
uploaded_file = st.file_uploader("Select Image File", type=["jpg", "jpeg", "png", "bmp"], accept_multiple_files=False)
if uploaded_file == None:
    st.error("Please Select an Image File")
    
else:
    st.success(f"Selected: {uploaded_file.name}")
    # read image
    file_bytes = np.frombuffer(uploaded_file.read(), np.uint8)
    test_img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)  # reads as BGR
    test_img = cv2.cvtColor(test_img, cv2.COLOR_BGR2RGB)   # convert to RGB

    options = ["Erosion", "Dilation", "Opening", "Closing", "Gradient"]
    selected = st.selectbox("Morphological Operations", options, index=0)
    #dictionary
    element_shapes = {"0: Rect": 0, "1: Cross": 1, "2: Ellipse": 2, "3: Diamond": 3}
    element_label = st.selectbox("Element Shape", list(element_shapes.keys()), index=0)
    element_size = element_shapes[element_label]
    #kernel slider
    trackbar_val=st.slider("Kernel Size", min_value=0, max_value=50, value=0)
    kernel_size=trackbar_val*2+1
    st.caption(f"Actual kernel size: {kernel_size}x{kernel_size}")
                
    if st.button("Apply Operation"):
        col1, col2 = st.columns(2)
        with col1:
            st.header("Original")
            st.image(test_img, width="stretch")
        with col2:
            on_selection_change(test_img, options, selected, element_size, kernel_size)
       
        result_pil = Image.fromarray(result)
        buf = io.BytesIO()
        result_pil.save(buf, format="PNG")
        st.download_button(
                label=f"Download {selected.lower()}",
                data=buf.getvalue(),
                file_name=f"{selected.lower()}_result.png",
                mime="image/png"
            )

else:
    st.warning("Please upload a file first")
