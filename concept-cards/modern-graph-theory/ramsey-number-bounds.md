---
concept: Bounds on Diagonal Ramsey Numbers
slug: ramsey-number-bounds
category: ramsey-theory
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Ramsey Theory"
chapter_number: 6
pdf_page: 188
section: "VI.1 The Fundamental Ramsey Theorems"
extraction_confidence: high
aliases:
  - "R(s) bounds"
  - "diagonal Ramsey bounds"
prerequisites:
  - ramsey-number
  - ramsey-theorem-finite
extends:
  - ramsey-theorem-finite
related:
  - probabilistic-method-ramsey
contrasts_with: []
answers_questions:
  - "How do I determine upper/lower bounds for Ramsey numbers?"
  - "How do Ramsey numbers relate to the probabilistic method?"
---

# Quick Definition
The diagonal Ramsey number R(s) satisfies 2^{s/2} ≤ R(s) ≤ C(2s−2, s−1) ≤ 4^s/√s. The upper bound is from Erdős-Szekeres (1935); the lower bound from the probabilistic method (Chapter VII).

# Core Definition
The best known bounds on R(s) (Bollobás, pp. 188–189):
- **Upper**: R(s) ≤ C(2s−2, s−1) ≤ 2^{2s−2}/√s (Erdős-Szekeres, 1935)
- **Improved upper**: R(s) ≤ 2^{2s}/s for large s (Thomason, 1988)
- **Lower**: R(s) ≥ 2^{s/2} (probabilistic method, Chapter VII)
- **Conjecture**: R(s) = 2^{(c+o(1))s} for some constant c (perhaps c = 1), but this is very far from proved

# Prerequisites
- **Ramsey number** — the quantity being bounded
- **Ramsey theorem (finite)** — source of upper bounds

# Key Properties
1. R(s) grows exponentially in s
2. The gap between upper and lower bounds is a factor of √2 in the base of the exponential
3. The upper bound was hardly improved for 50+ years
4. Random colourings give the best lower bounds (disorderly colourings lack large monochromatic complete subgraphs)
5. Computer search is hopeless: for R(5,5), must examine 2^{1000}+ graphs

# Context & Application
Determining the growth rate of R(s) is one of the most important open problems in combinatorics. The gap between 2^{s/2} and 4^s has resisted all attempts to close significantly.

# Examples
**Example** (p. 188): Known exact values: R(3) = 6, R(4) = 18. R(5) is unknown but 43 ≤ R(5) ≤ 49.

**Example** (Table VI.1, p. 189): Extensive table of bounds for R(s,t).

# Relationships
## Related
- **Probabilistic method** — source of lower bounds (Chapter VII)

# Common Confusions
- **Confusion**: Thinking computers can determine R(5,5)
  **Clarification**: Would require examining ~2^{1000} graphs — far beyond any computer's capability

# Source Reference
Chapter VI: Ramsey Theory, Section VI.1, pages 188–189.

# Verification Notes
- Definition source: Direct from pp. 188–189
- Confidence rationale: Explicit bounds with discussion
- Uncertainties: None
- Cross-reference status: Verified
