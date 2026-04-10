---
concept: Chromatic Surplus
slug: chromatic-surplus
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
  - "u(G)"
prerequisites:
  - chromatic-number
extends: []
related:
  - graphical-ramsey-number
  - ramsey-number-lower-bound
contrasts_with: []
answers_questions:
  - "What is the chromatic surplus of a graph?"
---

# Quick Definition
The chromatic surplus u(G) is the minimum number of vertices in a colour class over all proper χ(G)-colourings. It appears in the general lower bound for graphical Ramsey numbers.

# Core Definition
For a graph G, the **chromatic surplus** u(G) is the minimal number of vertices in a colour class, taken over all proper χ(G)-colourings: u(G) = min{|U| : U ⊂ V(G), χ(G − U) < χ(G)}. For example, u(C_{2k}) = k and u(C_{2k+1}) = 1 (Bollobás, p. 198).

# Prerequisites
- **Chromatic number** — u(G) is defined in terms of χ(G)-colourings

# Key Properties
1. u(G) = min size of a colour class in any χ(G)-colouring
2. u(C_{2k}) = k, u(C_{2k+1}) = 1
3. u(Kₙ) = 1
4. Appears in the lower bound r(H₁, H₂) ≥ (χ(H₁) − 1)(c(H₂) − 1) + u(H₁)

# Relationships
## Enables
- **Ramsey number lower bound** — r(H₁, H₂) ≥ (χ(H₁) − 1)(c(H₂) − 1) + u(H₁)

# Source Reference
Chapter VI: Ramsey Theory, Section VI.3, page 198.

# Verification Notes
- Definition source: Direct from p. 198
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
