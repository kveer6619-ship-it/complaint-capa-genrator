import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="AI Quality & CAPA Assistant", layout="wide")

# Side bar mein API Key dalne ka option
st.sidebar.title("🔑 AI Brain Setup")
api_key = st.sidebar.text_input("Apni Gemini API Key yahan paste karein:", type="password")
st.sidebar.info("API key box mein paste karke Enter dabayein.")

st.title("🛠️ AI Quality Management & CAPA Assistant")
st.write("Professional CAPA aur AI-Powered Quality Q&A Assistant.")

tab1, tab2 = st.tabs(["📋 Complaint & CAPA Generator", "🤖 AI Quality Q&A Assistant"])

# --- TAB 1: CAPA GENERATOR ---
with tab1:
    st.header("Customer Complaint to Advanced CAPA Generator")
    uploaded_file = st.file_uploader("📸 Defect ki photo upload karein (Optional)", type=["jpg", "png", "jpeg"])
    
    customer_name = st.text_input("Customer Name / Company")
    product_name = st.text_input("Product / Part Name / Part Code")
    defect_desc = st.text_area("Defect / Problem Description (Detail mein likhein)")
    
    if st.button("Generate Professional CAPA"):
        if defect_desc.strip() == "":
            st.warning("Kripya pehle defect description darj karein!")
        else:
            with st.spinner("Advanced CAPA taiyar ho raha hai..."):
                st.success("Professional CAPA Generated Successfully!")
                if uploaded_file is not None:
                    st.image(uploaded_file, caption="Defect ki Image", use_container_width=True)
                
                st.markdown("### 🚨 1. Immediate Outflow / Containment Action")
                st.write(f"- *Stock Quarantine:* {customer_name} ke is batch ke saare products ka dispatch turant rokein.\n- *Line Inspection:* Line ko turant rok kar 100% sorting karwayein.")
                
                st.markdown("### 🦴 2. Root Cause Analysis (Fishbone - 4M1E)")
                st.write("- *Man:* Operator ki training ka abhav.\n- *Machine:* Tool wear/tear ya calibration error.\n- *Material:* Raw material variation.\n- *Method:* SOP deviation.\n- *Environment:* Temperature/Humidity impact.")
                
                st.markdown("### ⚡ 3. Corrective Action (Permanent Fix)")
                st.write(f"1. Defective parts ({product_name}) ko rework ya scrap karein.\n2. Machine ke component ko recalibrate karein.")
                
                st.markdown("### 🛡️ 4. Preventive Action (Future Proofing)")
                st.write("1. Poka-Yoke implement karein.\n2. SOP ko update karke retraining karwayein.")

# --- TAB 2: AI QUALITY ASSISTANT (Powered by Smart Auto-Detection V2) ---
with tab2:
    st.header("🤖 AI Quality & Manufacturing Q&A Assistant")
    st.write("Quality standards ya kisi bhi defect ke baare mein sawal puchein.")
    
    user_query = st.text_input("Apna sawal yahan type karein:")
    
    if st.button("Get Expert Answer"):
        if user_query.strip() == "":
            st.warning("Kripya koi sawal puchein!")
        elif not api_key:
            st.error("⚠️ Kripya pehle left side bar (menu) mein apni Gemini API Key paste karein!")
        else:
            with st.spinner("Gemini AI jawab soch raha hai..."):
                try:
                    # AI ko set karna
                    genai.configure(api_key=api_key)
                    
                    # SMART SCANNER V2: Google ke restricted models ko ignore karna
                    valid_model = None
                    for m in genai.list_models():
                        if 'generateContent' in m.supported_generation_methods:
                            # 2.5 wale model ko chhod kar agla valid model chunega
                            if '2.5' not in m.name:
                                valid_model = m.name
                                break
                    
                    if valid_model:
                        model = genai.GenerativeModel(valid_model)
                        prompt = f"Tum ek expert Quality Assurance and Manufacturing Engineer ho. Is sawal ka jawab technical aur professional tareeqe se hindi aur english mix mein do: {user_query}"
                        
                        response = model.generate_content(prompt)
                        st.success(f"🤖 AI Expert Jawab (Model: {valid_model}):")
                        st.write(response.text)
                    else:
                        st.error("⚠️ Maaf kijiye, is API key mein koi valid model nahi mila.")
                        
                except Exception as e:
                    st.error(f"Error aagaya bhai: {e}")
