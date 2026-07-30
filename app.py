import streamlit as st
import google.generativeai as genai

st.set_page_config(
    page_title="AI Quality & CAPA Assistant",
    layout="wide"
)

# ---------------- Sidebar ---------------- #

st.sidebar.title("🔑 AI Brain Setup")

api_key = st.sidebar.text_input(
    "Apni Gemini API Key yahan paste karein:",
    type="password"
)

st.sidebar.info(
    "Free API Key:\nhttps://aistudio.google.com/app/apikey"
)

# ---------------- Main Title ---------------- #

st.title("🛠️ AI Quality Management & CAPA Assistant")
st.write("Professional CAPA Generator + AI Quality Expert")

tab1, tab2 = st.tabs([
    "📋 Complaint & CAPA Generator",
    "🤖 AI Quality Assistant"
])

# ======================================================
# TAB 1
# ======================================================

with tab1:

    st.header("Customer Complaint → Professional CAPA")

    uploaded_file = st.file_uploader(
        "Upload Defect Image (Optional)",
        type=["jpg", "jpeg", "png"]
    )

    customer_name = st.text_input("Customer Name")

    product_name = st.text_input("Product / Part Name")

    defect_desc = st.text_area("Defect Description")

    if st.button("Generate Professional CAPA"):

        if defect_desc.strip() == "":
            st.warning("Please enter defect description.")
        else:

            st.success("Professional CAPA Generated")

            if uploaded_file:
                st.image(uploaded_file)

            st.markdown("## 🚨 1. Immediate Containment Action")

            st.write(
                f"""
- Stop dispatch of affected stock.
- Quarantine all inventory related to *{customer_name}*.
- Perform 100% inspection.
- Inform production and quality team immediately.
"""
            )

            st.markdown("## 🦴 2. Root Cause Analysis (4M1E)")

            st.write("""
*Man*
- Operator training issue

*Machine*
- Tool wear / Machine calibration

*Material*
- Raw material variation

*Method*
- SOP not followed

*Environment*
- Temperature / Humidity variation
""")

            st.markdown("## ⚡ 3. Corrective Action")

            st.write(
                f"""
- Repair/Rework defective *{product_name}*.
- Recalibrate machine.
- Replace worn tooling.
"""
            )

            st.markdown("## 🛡️ 4. Preventive Action")

            st.write("""
- Update SOP
- Operator Retraining
- Poka-Yoke Implementation
- Layered Process Audit
- SPC Monitoring
""")

# ======================================================
# TAB 2
# ======================================================

with tab2:

    st.header("🤖 AI Quality Expert")

    user_query = st.text_area(
        "Ask anything about Quality, CAPA, Welding, 8D, ISO, SPC, MSA etc."
    )

    if st.button("Get Expert Answer"):

        if user_query.strip() == "":
            st.warning("Please enter your question.")

        elif not api_key:
            st.error("Please enter Gemini API Key first.")

        else:

            try:

                genai.configure(api_key=api_key)

                # ---------------- Find Available Gemini Models ---------------- #

                models = []

                for m in genai.list_models():

                    if "generateContent" in m.supported_generation_methods:

                        if "gemini" in m.name.lower():

                            models.append(m.name)

                if len(models) == 0:
                    st.error("No supported Gemini model found.")
                    st.stop()

                # Prefer Flash Model

                best_model = None

                priority = [
                    "gemini-2.5-flash",
                    "gemini-2.0-flash",
                    "gemini-1.5-flash"
                ]

                for p in priority:
                    for m in models:
                        if p in m.lower():
                            best_model = m
                            break
                    if best_model:
                        break

                if best_model is None:
                    best_model = models[0]

                st.success(f"Connected Model : {best_model}")

                model = genai.GenerativeModel(best_model)

                prompt = f"""
You are an Expert Quality Assurance Engineer.

Provide detailed professional answer.

Question:

{user_query}
"""

                with st.spinner("AI is thinking..."):

                    response = model.generate_content(prompt)

                st.markdown("## 🤖 Expert Answer")

                st.write(response.text)

            except Exception as e:

                st.error(str(e))
