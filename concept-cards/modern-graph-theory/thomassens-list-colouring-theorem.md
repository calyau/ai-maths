---
concept: Thomassen's List Colouring Theorem
slug: thomassens-list-colouring-theorem
category: list-coloring
subcategory: null
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Colouring"
chapter_number: 5
pdf_page: 169
section: "V.4 List Colouring"
extraction_confidence: high
aliases:
  - "Theorem V.12"
  - "5-list-colouring of planar graphs"
prerequisites:
  - list-chromatic-number
  - five-colour-theorem
extends:
  - five-colour-theorem
related:
  - near-triangulation
contrasts_with: []
answers_questions:
  - "What is the list-chromatic number of a planar graph?"
---

# Quick Definition
Every planar graph has list-chromatic number at most 5. This strengthens the five-colour theorem to the list colouring setting.

# Core Definition
**Theorem 12** (Bollobás, p. 170): Let G be a near-triangulation with outer cycle C = x₁x₂···xₖ, and let L(x) be lists with |L(x₁)| = |L(x₂)| = 1 (precoloured), |L(xᵢ)| ≥ 3 for other boundary vertices, and |L(x)| ≥ 5 for interior vertices. Then G has an L-colouring.

As a corollary, every planar graph has χ_ℓ ≤ 5. The proof uses induction on |G|, distinguishing cases by whether the outer cycle has a diagonal.

# Prerequisites
- **List-chromatic number** — the quantity being bounded
- **Five colour theorem** — this result strictly strengthens it

# Key Properties
1. χ_ℓ(G) ≤ 5 for every planar graph G
2. The result is best possible: there exist planar graphs with χ_ℓ = 5 (Voigt)
3. The proof is a striking example of strengthening the induction hypothesis
4. The near-triangulation version is much easier to prove by induction than the plain statement

# Context & Application
Thomassen's proof is celebrated for its elegance and brevity. It demonstrates the principle that proving a stronger statement can be easier by providing a stronger induction hypothesis. Much effort had been expended before Thomassen found this ingenious approach.

# Examples
**Example** (p. 170): The proof handles two cases: (i) outer cycle has a diagonal — split and apply induction to each piece; (ii) no diagonal — remove the last outer vertex xₖ, reduce lists of its internal neighbours by 2, and apply induction.

# Relationships
## Builds Upon
- **Five colour theorem** — strengthens it to list colouring

## Related
- **Near-triangulation** — the setting of the stronger induction statement

# Source Reference
Chapter V: Colouring, Section V.4, Theorem 12, pages 169–171.

# Verification Notes
- Definition source: Direct theorem statement from p. 170
- Confidence rationale: Explicit theorem with complete proof
- Uncertainties: None
- Cross-reference status: Verified
