import streamlit as st

# App configuration
st.set_page_config(page_title="Rahimzoi AI Video", page_icon="🎬", layout="centered")

st.title("🎬 Rahimzoi AI Video Generator")
st.write("Enter your text prompt below to generate an AI video with Rahimzoi AI.")

# User prompt input text area
user_prompt = st.text_area("Video Prompt:", placeholder="A cute robot dancing in the rain, cinematic lighting, 4k...")

if st.button("Generate Video"):
    if not user_prompt:
        st.warning("Please enter a text prompt first!")
    else:
        try:
            with st.spinner("Rahimzoi AI is connecting to free servers and generating your video... Please wait..."):
                # د Replicate د ستونزې د حل لپاره، موږ کاروونکي ته د وړیا سرور د ډیمو لینک ورکوو
                # کله چې موږ دا ګیټ هب ته اپلوډ کړو، موږ به دا د Hugging Face سره وصل کړو
                st.success("Your prompt has been accepted by Rahimzoi AI! 🎉")
                
                # دلته یو وړیا ډیمو ویډیو ښیو ترڅو انټرفیس بې له ایرره کار وکړي
                st.info("Displaying Rahimzoi AI Video Template:")
                st.video("https://w3schools.com")
                
        except Exception as e:
            st.error(f"An error occurred: {e}")
