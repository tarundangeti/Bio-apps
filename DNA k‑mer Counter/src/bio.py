from collections import Counter

def read_fasta_str(text: str) -> str:
    seq = []
    for line in text.splitlines():
        if not line.startswith(">") and line.strip():
            seq.append(line.strip())
    return "".join(seq)

def kmer_counts(seq: str, k: int):
    s = seq.upper()
    kmers = [s[i:i+k] for i in range(len(s) - k + 1) if set(s[i:i+k]).issubset({"A","C","G","T"})]
    counts = Counter(kmers)
    total = sum(counts.values())
    top5 = counts.most_common(5)
    return counts, total, top5
