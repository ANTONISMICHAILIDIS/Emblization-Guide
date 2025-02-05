import streamlit as st
import pandas as pd

# =============================================================================
# Title and Header
# =============================================================================
st.title("Embolization Guide")
st.markdown("<p style='font-size:12px'>Created by Michailidis A. for free use</p>", unsafe_allow_html=True)

# =============================================================================
# Sidebar: Organ and Pathology Selection
# =============================================================================
st.sidebar.header("Embolization Parameters")

organ_options = [
    "Liver",
    "Kidney",
    "Lung",
    "Gastrointestinal (GI)",
    "Genitourinary (Prostate)",
    "Uterus",
    "Musculoskeletal (MSK)",
    "Peripheral Vascular"
]
organ = st.sidebar.selectbox("Select the organ/system for embolization:", organ_options)

# Define pathology options based on the selected organ
if organ == "Liver":
    pathology_options = [
        "Malignant Tumors (HCC, Liver Metastases)",
        "Benign Tumors (Hepatic Adenoma, Hemangioma)"
    ]
elif organ == "Kidney":
    pathology_options = [
        "Renal Tumors (RCC, Angiomyolipoma)",
        "Renal Hemorrhage (Trauma, Iatrogenic, Postoperative)"
    ]
elif organ == "Lung":
    pathology_options = ["Hemoptysis (Massive or Chronic)"]
elif organ == "Gastrointestinal (GI)":
    pathology_options = ["GI Bleeding (Peptic Ulcer, Variceal, Tumor-Related)"]
elif organ == "Genitourinary (Prostate)":
    pathology_options = ["Prostate Artery Embolization (PAE) for BPH"]
elif organ == "Uterus":
    pathology_options = ["Fibroid Embolization (Uterine Artery Embolization)"]
elif organ == "Musculoskeletal (MSK)":
    pathology_options = ["Bone Tumors (Osteoid Osteoma, Metastases)"]
elif organ == "Peripheral Vascular":
    pathology_options = ["Arteriovenous Malformations (AVMs)"]
else:
    pathology_options = ["Other"]

pathology = st.sidebar.selectbox("Select the pathology/indication:", pathology_options)
emergency = st.sidebar.checkbox("Is this an emergency case?")

# =============================================================================
# Instruction Generation Function
# =============================================================================
def get_instructions(organ, pathology, emergency):
    instructions = ""
    
    # -------------------------------
    # 1. Liver Embolization
    # -------------------------------
    if organ == "Liver":
        if pathology == "Malignant Tumors (HCC, Liver Metastases)":
            instructions += "### Liver Embolization: Malignant Tumors (HCC, Liver Metastases)\n\n"
            instructions += "**Primary Techniques:**\n"
            instructions += "- Transarterial Chemoembolization (TACE)\n"
            instructions += "- Transarterial Radioembolization (TARE/Y90)\n"
            instructions += "- Bland Embolization (TAE)\n\n"
            instructions += "**Embolic Agents:**\n"
            instructions += "- Drug-Eluting Beads (DEB-TACE)\n"
            instructions += "- Yttrium-90 Microspheres (for TARE)\n"
            instructions += "- Polyvinyl Alcohol (PVA) Particles\n\n"
            instructions += "**Catheter Selection:**\n"
            instructions += "- Microcatheters (2.0–2.8 Fr) for superselective embolization\n"
            instructions += "- 5–6 Fr guiding catheters for main access\n\n"
            instructions += "**Vascular Access:**\n"
            instructions += "- Common Femoral Artery (CFA) → Celiac Axis → Hepatic Artery\n"
            instructions += "- Radial Artery access is an alternative option\n\n"
            instructions += "**Medications:**\n"
            instructions += "- Administer antibiotics to prevent postembolization syndrome\n"
            instructions += "- IV analgesia and sedation are recommended\n\n"
            instructions += "**Anatomical Variations:**\n"
            instructions += "- Be alert for a replaced right hepatic artery originating from the Superior Mesenteric Artery (SMA)\n"
            instructions += "- A replaced left hepatic artery may arise from the left gastric artery\n\n"
            
        elif pathology == "Benign Tumors (Hepatic Adenoma, Hemangioma)":
            instructions += "### Liver Embolization: Benign Tumors (Hepatic Adenoma, Hemangioma)\n\n"
            instructions += "**Techniques:**\n"
            instructions += "- Superselective embolization is recommended\n\n"
            instructions += "**Embolic Agents:**\n"
            instructions += "- Microspheres (300–500 μm) for precise vessel occlusion\n"
            instructions += "- Coils for occluding larger feeding arteries\n\n"
            instructions += "**Emergency Considerations:**\n"
            instructions += "- In cases of active bleeding, use Gelatin Sponge for temporary occlusion\n\n"
    
    # -------------------------------
    # 2. Kidney (Renal) Embolization
    # -------------------------------
    elif organ == "Kidney":
        if pathology == "Renal Tumors (RCC, Angiomyolipoma)":
            instructions += "### Renal Embolization: Renal Tumors (RCC, Angiomyolipoma)\n\n"
            instructions += "**Techniques:**\n"
            instructions += "- Superselective Renal Artery Embolization\n\n"
            instructions += "**Embolic Agents:**\n"
            instructions += "- Microparticles (100–300 μm) to induce tumor ischemia\n"
            instructions += "- Coils for occluding large feeding arteries\n\n"
            instructions += "**Catheter Selection:**\n"
            instructions += "- 5–6 Fr guiding catheter for renal artery access\n"
            instructions += "- Microcatheters for superselective embolization\n\n"
            instructions += "**Vascular Access:**\n"
            instructions += "- Common Femoral Artery → Abdominal Aorta → Renal Artery\n\n"
            instructions += "**Medications:**\n"
            instructions += "- IV fluids periprocedurally to prevent contrast-induced nephropathy\n"
            instructions += "- Pain management for post-embolization syndrome is recommended\n\n"
            
        elif pathology == "Renal Hemorrhage (Trauma, Iatrogenic, Postoperative)":
            instructions += "### Renal Embolization: Renal Hemorrhage (Trauma, Iatrogenic, Postoperative)\n\n"
            instructions += "**Embolic Agents:**\n"
            instructions += "- Gelatin Sponge for temporary hemostasis\n"
            instructions += "- Coils for permanent occlusion if needed\n\n"
            instructions += "**Emergency Considerations:**\n"
            instructions += "- Urgent embolization is required in cases of active renal hemorrhage\n\n"
    
    # -------------------------------
    # 3. Lung (Pulmonary) Embolization
    # -------------------------------
    elif organ == "Lung":
        instructions += "### Pulmonary Embolization: Hemoptysis (Massive or Chronic)\n\n"
        instructions += "**Techniques:**\n"
        instructions += "- Bronchial Artery Embolization (BAE)\n\n"
        instructions += "**Embolic Agents:**\n"
        instructions += "- PVA Particles (300–500 μm)\n"
        instructions += "- Coils (especially for treating arteriovenous malformations)\n\n"
        instructions += "**Catheter Selection:**\n"
        instructions += "- 5–6 Fr guiding catheter for bronchial artery access\n"
        instructions += "- Microcatheters for selective embolization\n\n"
        instructions += "**Vascular Access:**\n"
        instructions += "- Common Femoral Artery → Descending Thoracic Aorta → Bronchial Arteries\n\n"
        instructions += "**Medications:**\n"
        instructions += "- IV heparin may be used in cases of pulmonary AVM embolization\n\n"
        instructions += "**Anatomical Variations:**\n"
        instructions += "- Be aware of anomalous bronchial artery origins (e.g., arising from intercostal arteries)\n\n"
    
    # -------------------------------
    # 4. Gastrointestinal (GI) Embolization
    # -------------------------------
    elif organ == "Gastrointestinal (GI)":
        instructions += "### GI Embolization: GI Bleeding (Peptic Ulcer, Variceal, Tumor-Related)\n\n"
        instructions += "**Techniques:**\n"
        instructions += "- Superselective embolization is critical for controlling bleeding\n\n"
        instructions += "**Embolic Agents:**\n"
        instructions += "- Microcoils for precise arterial occlusion\n"
        instructions += "- NBCA glue for rapid hemostasis when needed\n\n"
        instructions += "**Catheter Selection:**\n"
        instructions += "- Microcatheters (typically 2.5 Fr) for superselective embolization\n\n"
        instructions += "**Vascular Access:**\n"
        instructions += "- Common Femoral Artery → Celiac Axis → Left Gastric Artery\n\n"
        instructions += "**Emergency Considerations:**\n"
        instructions += "- In massive GI bleeding, immediate embolization is essential\n\n"
    
    # -------------------------------
    # 5. Genitourinary (Prostate) Embolization
    # -------------------------------
    elif organ == "Genitourinary (Prostate)":
        instructions += "### Prostate Artery Embolization (PAE) for BPH\n\n"
        instructions += "**Techniques:**\n"
        instructions += "- Bilateral embolization of the prostate arteries\n\n"
        instructions += "**Embolic Agents:**\n"
        instructions += "- Microparticles (100–300 μm) are used to induce ischemia in the prostatic tissue\n\n"
        instructions += "**Catheter Selection:**\n"
        instructions += "- 5 Fr guiding catheter for iliac access\n"
        instructions += "- Microcatheters for selective embolization of the prostatic arteries\n\n"
        instructions += "**Vascular Access:**\n"
        instructions += "- Common Femoral Artery → Internal Iliac Artery → Prostatic Artery\n\n"
        instructions += "**Anatomical Variations:**\n"
        instructions += "- Expect four anatomical subtypes of prostatic arteries (Type I–IV) that may affect access and embolization technique\n\n"
    
    # -------------------------------
    # 6. Uterine Artery Embolization (UAE)
    # -------------------------------
    elif organ == "Uterus":
        instructions += "### Uterine Artery Embolization: Fibroid Embolization\n\n"
        instructions += "**Techniques:**\n"
        instructions += "- Superselective embolization of the uterine arteries\n\n"
        instructions += "**Embolic Agents:**\n"
        instructions += "- Microparticles (300–500 μm) to infarct the fibroids\n\n"
        instructions += "**Catheter Selection:**\n"
        instructions += "- 5 Fr guiding catheter for internal iliac artery access\n"
        instructions += "- Microcatheters for selective uterine artery embolization\n\n"
        instructions += "**Vascular Access:**\n"
        instructions += "- Common Femoral Artery → Internal Iliac Artery → Uterine Artery\n\n"
    
    # -------------------------------
    # 7. Musculoskeletal (MSK) Embolization
    # -------------------------------
    elif organ == "Musculoskeletal (MSK)":
        instructions += "### Musculoskeletal Embolization: Bone Tumors (Osteoid Osteoma, Metastases)\n\n"
        instructions += "**Techniques:**\n"
        instructions += "- Preoperative embolization to reduce tumor vascularity\n\n"
        instructions += "**Embolic Agents:**\n"
        instructions += "- Microparticles (100–300 μm) for tumor devascularization\n\n"
        instructions += "**Catheter Selection:**\n"
        instructions += "- Microcatheters for selective embolization of the tumor feeding artery\n\n"
        instructions += "**Vascular Access:**\n"
        instructions += "- Common Femoral Artery → Selective Tumor Feeding Artery\n\n"
    
    # -------------------------------
    # 8. Peripheral Vascular Embolization
    # -------------------------------
    elif organ == "Peripheral Vascular":
        instructions += "### Peripheral Vascular Embolization: Arteriovenous Malformations (AVMs)\n\n"
        instructions += "**Techniques:**\n"
        instructions += "- Superselective embolization is performed to occlude the AVM\n\n"
        instructions += "**Embolic Agents:**\n"
        instructions += "- NBCA glue for permanent occlusion of the AVM\n\n"
        instructions += "**Catheter Selection:**\n"
        instructions += "- Microcatheters are used for precise embolization\n\n"
        instructions += "**Vascular Access:**\n"
        instructions += "- Common Femoral Artery → Selective Target Vessel\n\n"
    
    # -------------------------------
    # Emergency Adjustments (General)
    # -------------------------------
    if emergency:
        instructions += "\n**Emergency Protocol Adjustments:**\n"
        instructions += "- Prioritize rapid hemostasis using fast-acting embolic agents (e.g., NBCA glue or Gelatin Sponge).\n"
        instructions += "- Streamline the procedure to reduce imaging delays.\n"
        instructions += "- Ensure immediate availability of all embolic materials and backup devices.\n"

    return instructions

# =============================================================================
# Generate and Display Instructions
# =============================================================================
st.header("Embolization Instructions")
instructions_text = get_instructions(organ, pathology, emergency)
st.text_area("Detailed Instructions", value=instructions_text, height=600)
