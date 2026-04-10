---
concept: Mirror Image of a Link
slug: mirror-image-of-link
category: knot-theory
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "The Tutte Polynomial"
chapter_number: 10
pdf_page: 372
section: "X.6 Polynomials of Knots and Links"
extraction_confidence: high
aliases:
  - "reflection"
  - "amphicheiral"
  - "chiral"
prerequisites:
  - link-diagram
  - one-variable-kauffman-polynomial
extends: []
related:
  - jones-polynomial
contrasts_with: []
answers_questions:
  - "How do knot polynomials relate to the Tutte polynomial?"
---

# Quick Definition
The mirror image $L^*$ of a link diagram $L$ is obtained by reversing all crossings. A link is amphicheiral if it is equivalent to its mirror image. The Kauffman polynomial detects chirality: $f_{L^*}[A] = f_L[A^{-1}]$.

# Core Definition
Theorem 20 (p. 372): "The bracket and one-variable Kauffman polynomial of the mirror image $L^*$ of a link diagram $L$ are $\langle L^* \rangle(A) = \langle L \rangle(A^{-1})$ and $f_{L^*}[A] = f_L[A^{-1}]$." A link is amphicheiral if $L \sim L^*$; otherwise it is chiral.

# Prerequisites
- **Link diagram** — Mirror image reverses all crossings
- **One-variable Kauffman polynomial** — Detects chirality

# Key Properties
1. $\langle L^* \rangle(A) = \langle L \rangle(A^{-1})$
2. $f_{L^*}[A] = f_L[A^{-1}]$
3. If $f_L[A] \neq f_L[A^{-1}]$: the link is chiral
4. The trefoil is chiral (its Kauffman polynomial is not palindromic)
5. The figure-of-eight knot is amphicheiral

# Examples
**Example** (p. 372): The right-handed trefoil has $f[L] = -A^{-16} + A^{-12} + A^{-4}$, which changes under $A \to A^{-1}$, proving chirality.

# Relationships
## Builds Upon
- **link-diagram**, **one-variable-kauffman-polynomial**

## Related
- **jones-polynomial** — Also detects chirality

# Source Reference
Chapter X, Section X.6, Theorem 20, pages 372-373.

# Verification Notes
- Definition source: Direct from Theorem 20
- Confidence rationale: Explicit theorem
- Uncertainties: None
- Cross-reference status: Verified
