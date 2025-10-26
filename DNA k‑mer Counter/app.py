import streamlit as st
from src.bio import read_fasta_str, kmer_counts

st.set_page_config(page_title="DNA k-mer Counter", page_icon="🧬")
st.title("🧬 DNA k-mer Counter")
st.caption("Paste DNA or upload FASTA, choose k, and view k-mer frequencies")

with st.sidebar:
    k = st.number_input("Choose k", min_value=1, max_value=6, value=2, step=1)

dna_text = st.text_area("Paste DNA (ACGT only; whitespace ignored)", height=150)
uploaded = st.file_uploader("Or upload FASTA (.fasta/.fa)", type=["fasta","fa"])

seq = ""
if uploaded is not None:
    seq = read_fasta_str(uploaded.getvalue().decode("utf-8", errors="ignore"))
elif dna_text.strip():
    seq = "".join(dna_text.split())

if st.button("Analyze") and seq:
    counts, total, top5 = kmer_counts(seq, k)
    st.write({"Total k-mers": total, "Distinct k-mers": len(counts)})
    items = sorted(counts.items(), key=lambda x: x[0])
    st.dataframe({"k-mer": [k for k,_ in items], "count": [v for _,v in items]}, use_container_width=True)
    st.bar_chart(dict(counts.most_common(20)))
    st.write("Top 5:", top5)
