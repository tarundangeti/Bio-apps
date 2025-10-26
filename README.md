DNA k‑mer Counter
A tiny bioinformatics app to analyze DNA composition by counting k‑mers (all substrings of length k). It supports pasting raw DNA or uploading FASTA files and shows frequency tables and simple charts. This is ideal for learning Python, basic bioinformatics, and a minimal web UI.

What this does
Counts k‑mers for a given k (e.g., k=1 bases, k=2 dinucleotides, k=3 trimers).

Accepts raw DNA text or FASTA upload.

Displays a frequency table, total/distinct counts, and a chart (Streamlit).

Validates and normalizes input (uppercase, ignores whitespace; FASTA headers start with “>”).

Why it’s useful
Quick QC and composition profiling of sequences.

Explore how k affects patterns (GC bias, repeats, basic motif hints).

Foundation for more advanced workflows (motifs, assembly concepts, alignment‑free comparisons).

Project structure
text
dna-kmer-app/
├── app.py                 # Streamlit UI + logic
├── requirements.txt       # Dependencies (streamlit, biopython)
├── data/
│   └── sample.fa          # Test FASTA data
├── src/
│   ├── __init__.py
│   └── bio.py             # read_fasta, kmer_counts, helpers
├── .streamlit/
│   └── config.toml        # Optional Streamlit theme/config
├── .venv/                 # Python virtual environment (recommended)
└── README.md
Tip: You can also keep a sibling Flask app for a traditional HTML frontend:

text
bio-apps/
├── dna-kmer-app/          # Streamlit app
└── dna-kmer-flask/        # Flask app with templates/static
Prerequisites
Python 3.10+ installed.

VS Code recommended, with Python extension.

Create/Select a virtual environment (.venv) in the project folder.

Setup
Clone or create the folder and open it in VS Code.

Create/activate a virtual environment:

Windows (PowerShell):

python -m venv .venv

.venv\Scripts\Activate.ps1

macOS/Linux (bash/zsh):

python -m venv .venv

source .venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Running the Streamlit app
From the dna-kmer-app folder:

streamlit run app.py

Your browser will open to a local URL (e.g., http://localhost:8501).

Note: Do not use python app.py for Streamlit. Always use streamlit run app.py.

Using the app (Streamlit)
Paste DNA in the textarea or upload a .fa/.fasta file.

Choose k (1–6) in the sidebar.

Click Analyze to see:

Summary: total and distinct k‑mers.

Table: k‑mer counts (sortable).

Chart: bar plot of top k‑mers.

Valid FASTA:

First line starts with “>” (header).

Following lines contain DNA letters (A/C/G/T/N).

Example:

text
>seq1 synthetic_example
ACGTACGTACGTACGTACGTACGT
Sample data
data/sample.fa (add your own).

More quick samples:

Single sequence:

text
>seq1 synthetic_example
ACGTACGTACGTACGTACGTACGT
Two sequences (multi‑FASTA):

text
>seqA E_coli_mock_contig
ATGCGTACGTTTACGNNNACGTACGTACGTTT
>seqB Yeast_mock_contig
GGGAAACCCGGGTTTAAACCCGGGTTT
If your OS adds “.txt”, rename to .fa or .fasta (e.g., dna_sample2.fa) so upload filters accept it.

Running the Flask app (optional)
If you created a sibling project dna-kmer-flask:

From dna-kmer-flask folder:

python -m venv .venv

activate the venv

pip install -r requirements.txt

python app.py

Open http://127.0.0.1:5000

Template note: In Jinja, call dict methods in loops (use items()) or pass a prepared list of pairs from Python.

Testing and sanity checks
ACGTACGT with k=1 → counts A=2, C=2, G=2, T=2; total = 8.

For a sequence of length L, total k‑mers should be L − k + 1 (for clean A/C/G/T windows).

Try lowercase input and sequences with whitespace/newlines; logic should normalize to uppercase and ignore whitespace.

Common issues
Streamlit “ScriptRunContext” warnings: You used python app.py; fix by running streamlit run app.py.

Uploader rejects .fa.txt: Rename to .fa or .fasta.

Flask template error “items is not iterable”: Use result.items() or loop a pairs list.

Extending the app
Add GC% and base counts next to k‑mer table.

Add CSV download of k‑mer frequencies.

Per‑record k‑mer tables for multi‑FASTA.

Bar/line charts for selected k‑mers across samples.

License
Educational use. Customize as needed for your coursework or portfolio.

Acknowledgments
This project idea introduces practical k‑mer composition analysis for learning Python, simple bioinformatics parsing, and beginner web UIs (Streamlit or Flask).
