---
concept: "Chvátal-Szemerédi Theorem"
slug: chvatal-szemeredi-theorem
category: regularity-method
subcategory: applications
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Extremal Problems"
chapter_number: 4
pdf_page: 110
section: "IV.4 The Structure of Graphs"
extraction_confidence: high
aliases:
  - "Chvátal-Szemerédi 1981"
prerequisites:
  - erdos-stone-theorem
  - szemeredis-regularity-lemma
extends: []
related: []
contrasts_with: []
answers_questions:
  - "Is the logarithmic speed in the Erdős-Stone theorem optimal?"
---

# Quick Definition
The logarithmic growth rate of $t$ in the Erdős-Stone theorem is optimal: there exist graphs with $\varepsilon n^2$ edges avoiding $K_2(t)$ for $t = c \log n$.

# Core Definition
In 1981, Chvátal and Szemerédi proved that the logarithmic speed for $t \to \infty$ in the Erdős-Stone theorem (Theorem 22) is the correct speed, using Szemerédi's regularity lemma. For every $\varepsilon$ and $r$, there is a constant $d_r^*$ tending to 0 with $\varepsilon$ such that a graph need not contain $K_r(t)$ with $t = \lfloor d_r^* \log n \rfloor$ (Bollobás, pp. 137-138).

# Prerequisites
- **Erdős-Stone theorem** — The theorem whose bound is shown to be tight
- **Szemerédi's regularity lemma** — Used in the proof

# Key Properties
1. Shows Theorem 22 is best possible up to the constant
2. Uses regularity lemma in the proof
3. The random graph construction (Chapter VII) gives the lower bound

# Context & Application
Completes the picture of the Erdős-Stone theorem by showing the $\log n$ speed is unavoidable.

# Examples
**Example** (p. 138): For $0 < \varepsilon < 1/2$, the constant $d_2^*$ satisfies $d_2^* > -2/\log(2\varepsilon)$.

# Relationships
## Builds Upon
- **erdos-stone-theorem** — Sharpness result
- **szemeredis-regularity-lemma** — Proof tool

# Source Reference
Chapter IV, Section IV.4, pages 137-138.

# Verification Notes
- Definition source: Direct from pp. 137-138
- Confidence rationale: Explicitly stated
- Uncertainties: None
- Cross-reference status: Verified
