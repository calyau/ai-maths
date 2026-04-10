---
concept: "Gowers' Tower Bound for Regularity"
slug: gowers-tower-bound
category: regularity-method
subcategory: bounds
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Extremal Problems"
chapter_number: 4
pdf_page: 110
section: "IV.5 Szemerédi's Regularity Lemma"
extraction_confidence: high
aliases:
  - "Gowers lower bound"
prerequisites:
  - szemeredis-regularity-lemma
extends: []
related: []
contrasts_with: []
answers_questions:
  - "How large must M(ε,m) be in the regularity lemma?"
---

# Quick Definition
In 1997, Gowers proved that $M(\varepsilon, 2)$ must grow at least as a tower of 2s of height about $\varepsilon^{-1/16}$, showing the enormous bound in Szemerédi's proof is unavoidable.

# Core Definition
The bound on $M(\varepsilon, m)$ in the proof of Theorem 29 is roughly a tower of 2s of height $\varepsilon^{-5}$. In 1997, Gowers proved that $M(\varepsilon, 2)$ grows at least as a tower of 2s of height about $\varepsilon^{-1/16}$: "the argument is a tour de force" (Bollobás, p. 146).

# Prerequisites
- **Szemerédi's regularity lemma** — The bound being analyzed

# Key Properties
1. Tower-type growth is inherent, not an artifact of the proof
2. Gap between upper ($\varepsilon^{-5}$ levels) and lower ($\varepsilon^{-1/16}$ levels) bounds remains
3. Determining exact growth is an open problem

# Context & Application
Shows that regularity-based arguments inherently require partitions with an enormous number of classes.

# Examples
**Example** (p. 146): For $\varepsilon = 0.01$, the bound is roughly a tower of $10^{10}$ levels of 2s.

# Relationships
## Related
- **szemeredis-regularity-lemma** — The theorem whose bound is analyzed

# Source Reference
Chapter IV, Section IV.5, page 146.

# Verification Notes
- Definition source: Direct from p. 146
- Confidence rationale: Explicitly stated
- Uncertainties: None
- Cross-reference status: Verified
