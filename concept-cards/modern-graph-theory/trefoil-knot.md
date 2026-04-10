---
concept: Trefoil Knot
slug: trefoil-knot
category: knot-theory
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "The Tutte Polynomial"
chapter_number: 10
pdf_page: 363
section: "X.6 Polynomials of Knots and Links"
extraction_confidence: high
aliases:
  - "right-handed trefoil"
  - "left-handed trefoil"
prerequisites:
  - knot
extends: []
related:
  - kauffman-bracket
  - jones-polynomial
  - mirror-image-of-link
  - three-colouring-of-link
contrasts_with: []
answers_questions:
  - "How do knot polynomials relate to the Tutte polynomial?"
---

# Quick Definition
The trefoil knot is the simplest non-trivial knot, with 3 crossings. It is chiral: the right-handed and left-handed trefoils are not equivalent, as proved by the Kauffman polynomial.

# Core Definition
The trefoil knot appears in Fig. X.3 (p. 363) and Figs. X.5, VIII.4. Its Kauffman bracket is $A^{-7} - A^{-3} - A^5$ (right-handed), giving $f[L] = -A^{-16} + A^{-12} + A^{-4}$. Since $f[L](A) \neq f[L](A^{-1})$, the trefoil is chiral (Bollobás, p. 372).

# Prerequisites
- **Knot** — The trefoil is a specific knot

# Key Properties
1. Three crossings (the minimum for a non-trivial knot)
2. Has a non-trivial proper 3-colouring (so it is knotted)
3. Chiral: right-handed $\neq$ left-handed (proved by Kauffman polynomial)
4. Alternating knot (standard diagram is alternating)
5. Bracket: $\langle L \rangle = A^{-7} - A^{-3} - A^5$ (right-handed, writhe $+3$)

# Examples
**Example** (p. 372): $f[\text{right trefoil}] = -A^{-16} + A^{-12} + A^{-4}$, which is not invariant under $A \mapsto A^{-1}$, proving chirality.

# Relationships
## Builds Upon
- **knot**

## Related
- **kauffman-bracket**, **jones-polynomial**, **mirror-image-of-link**, **three-colouring-of-link**

# Source Reference
Chapter X, Section X.6, pages 363, 371-372. Figures X.3, X.5.

# Verification Notes
- Definition source: Direct from pp. 363, 371-372
- Confidence rationale: Explicit computations
- Uncertainties: None
- Cross-reference status: Verified
