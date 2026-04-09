---
concept: Compactness Argument in Ramsey Theory
slug: bad-colouring-compactness
category: ramsey-theory
subcategory: classical-ramsey
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Ramsey Theory for Graphs"
chapter_number: 9
pdf_page: 264
section: "9.1 Ramsey's original theorems"
extraction_confidence: high
aliases:
  - "bad colouring argument"
prerequisites:
  - ramsey-theorem-infinite
  - ramsey-theorem-general
related:
  - ramsey-number
answers_questions:
  - "How is the finite Ramsey theorem deduced from the infinite version?"
---

# Quick Definition
The finite Ramsey theorem is deduced from the infinite version by a compactness argument: if the finite version fails, "bad colourings" of [n]^k for all n can be combined via Konig's infinity lemma into a bad colouring of [N]^k, contradicting the infinite version.

# Core Definition
Proof of Theorem 9.1.3 from Theorem 9.1.2: Suppose the finite version fails for some k, c, r. Then for every n >= k there exists a "bad" c-colouring of [n]^k with no monochromatic r-set. By Konig's infinity lemma (8.1.2), there is a sequence g_k, g_{k+1}, ... of bad colourings with g_n restricting to g_{n-1}. These combine into a bad colouring g of [N]^k, contradicting the infinite version. (Diestel, pp. 254-255)

# Prerequisites
- **Ramsey's theorem (infinite)** — The result being used
- **Ramsey's theorem (general)** — The result being proved

# Key Properties
1. Avoids the tedious size-tracking of a direct finite proof
2. Uses Konig's infinity lemma as the compactness tool
3. A standard technique in infinite combinatorics

# Source Reference
Chapter 9, Section 9.1, proof of Theorem 9.1.3, pages 254-255 (pdf pages 264-265).

# Verification Notes
- Confidence: HIGH — proof given
