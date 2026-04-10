---
concept: Unknot
slug: unknot
category: knot-theory
subcategory: null
tier: foundational
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "The Tutte Polynomial"
chapter_number: 10
pdf_page: 366
section: "X.6 Polynomials of Knots and Links"
extraction_confidence: high
aliases:
  - "trivial knot"
prerequisites:
  - knot
extends: []
related:
  - kauffman-bracket
  - jones-polynomial
  - three-colouring-of-link
contrasts_with: []
answers_questions:
  - "How do knot polynomials relate to the Tutte polynomial?"
---

# Quick Definition
The unknot (trivial knot) is a knot equivalent to a simple circle with no crossings. Detecting whether a given knot is the unknot is a fundamental problem in knot theory.

# Core Definition
The unknot is the equivalence class of the "trivial knot whose diagram has no crossings" (Bollobás, p. 366). A basic question in knot theory: "Is a knot really 'knotted' or is it (equivalent to) the unknot?"

# Prerequisites
- **Knot** — The unknot is the simplest knot

# Key Properties
1. Diagram with no crossings
2. $\langle \text{unknot} \rangle = 1$ (Kauffman bracket)
3. $V_{\text{unknot}}(t) = 1$ (Jones polynomial)
4. No non-trivial proper 3-colouring
5. Any knot with a non-trivial 3-colouring is not the unknot

# Relationships
## Builds Upon
- **knot**

## Related
- **kauffman-bracket** — $\langle \bigcirc \rangle = 1$
- **jones-polynomial** — $V_{\bigcirc} = 1$
- **three-colouring-of-link** — Detects non-unknottedness

# Source Reference
Chapter X, Section X.6, page 366.

# Verification Notes
- Definition source: Direct from p. 366
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
