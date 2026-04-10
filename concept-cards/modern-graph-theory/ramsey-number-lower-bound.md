---
concept: Lower Bound for Graphical Ramsey Numbers
slug: ramsey-number-lower-bound
category: ramsey-theory
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Ramsey Theory"
chapter_number: 6
pdf_page: 198
section: "VI.3 Ramsey Theory For Graphs"
extraction_confidence: high
aliases:
  - "Theorem VI.11"
prerequisites:
  - graphical-ramsey-number
  - chromatic-surplus
extends: []
related:
  - ramsey-number-for-trees
contrasts_with: []
answers_questions:
  - "How do I determine lower bounds for Ramsey numbers?"
---

# Quick Definition
r(H₁, H₂) ≥ (χ(H₁) − 1)(c(H₂) − 1) + u(H₁), where c(H₂) is the maximum component order and u(H₁) is the chromatic surplus. If H₂ is connected, r(H₁, H₂) ≥ (χ(H₁) − 1)(|H₂| − 1) + 1.

# Core Definition
**Theorem 11** (Bollobás, p. 198): For all nonempty graphs H₁ and H₂, r(H₁, H₂) ≥ (χ(H₁) − 1)(c(H₂) − 1) + u(H₁). If H₂ is connected, r(H₁, H₂) ≥ (χ(H₁) − 1)(|H₂| − 1) + 1.

The proof constructs the graph G = (k−1)K_{c−1} ∪ K_{u−1} which has no H₂ and whose complement has no H₁.

# Prerequisites
- **Graphical Ramsey number** — the quantity being bounded
- **Chromatic surplus** — appears in the formula

# Key Properties
1. Valid for all nonempty H₁, H₂
2. Tight for trees vs. complete graphs (Chvátal's theorem)
3. Tight for fans vs. triangles
4. A graph H₂ is "H₁-good" when equality holds

# Relationships
## Enables
- **Ramsey number for trees** — tight for this family

# Source Reference
Chapter VI: Ramsey Theory, Section VI.3, Theorem 11, page 198.

# Verification Notes
- Definition source: Direct from p. 198
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
