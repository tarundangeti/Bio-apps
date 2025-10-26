from flask import Flask, render_template, request
from collections import Counter

app = Flask(__name__)

def kmer_counts(seq: str, k: int):
  s = seq.upper()
  kmers = [s[i:i+k] for i in range(len(s) - k + 1) if set(s[i:i+k]).issubset({"A","C","G","T"})]
  counts = Counter(kmers)
  total = sum(counts.values())
  return counts, total

@app.route("/", methods=["GET","POST"])
def index():
  result = None
  if request.method == "POST":
    dna = request.form.get("dna","").replace(" ", "").replace("\n", "")
    k = int(request.form.get("k","2"))
    counts, total = kmer_counts(dna, k)
    result = {"total": total, "items": sorted(counts.items())}
  return render_template("index.html", result=result)

if __name__ == "__main__":
  app.run(debug=True)
