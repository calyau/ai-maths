---
concept: Reducible Representation
slug: reducible-representation
category: group-representations
subcategory: null
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Group Representations"
chapter_number: 10
pdf_page: 301
section: "10.2 Irreducible Representations"
extraction_confidence: high
aliases: []
prerequisites: [g-invariant-subspace]
extends: [group-representation]
related: [completely-reducible-representation]
contrasts_with: [irreducible-representation]
answers_questions: ["What is a reducible representation?"]
---
# Quick Definition
A representation rho on V is reducible if V has a proper G-invariant subspace. The matrix representation then has an upper block-triangular form with respect to a basis extending a basis of the invariant subspace.
# Core Definition
If V has a proper G-invariant subspace W, the representation rho is reducible (Artin, p. 307). Choosing a basis (w_1, ..., w_k, v_{k+1}, ..., v_d) with the first k vectors in W gives R_g = [[A_g, *],[0, B_g]] (10.2.9). By Maschke's theorem, the "junk" block * can be eliminated by choosing a better basis.
# Prerequisites
- **G-invariant subspace** — Reducibility means such a subspace exists
# Key Properties
1. V has a proper G-invariant subspace
2. Matrix representation has upper block-triangular form
3. By Maschke's theorem, can always be made block-diagonal (for finite groups over C)
# Examples
**Example 1** (p. 308): The permutation representation N of S_3 on C^3 is reducible: the span of (1,1,1)^t is G-invariant.
# Relationships
## Contrasts With
- **Irreducible representation** — No proper G-invariant subspaces
## Related
- **Completely reducible representation** — A direct sum of irreducibles
# Source Reference
Chapter 10: Group Representations, Section 10.2, pages 307-308.
# Verification Notes
- Definition source: Direct from p. 307
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
