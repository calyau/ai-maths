---
concept: Completely Reducible Representation
slug: completely-reducible-representation
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
aliases: ["semisimple representation"]
prerequisites: [irreducible-representation, maschkes-theorem]
extends: [group-representation]
related: []
contrasts_with: []
answers_questions: ["What is a completely reducible representation?"]
---
# Quick Definition
A completely reducible representation is one that decomposes as a direct sum of irreducible representations. By Maschke's theorem, every representation of a finite group over C is completely reducible.
# Core Definition
A representation rho is completely reducible if it is isomorphic to a direct sum of irreducible representations: rho = n_1 rho_1 + ... + n_r rho_r (Artin, (10.4.7), p. 312). The multiplicities n_i are determined by the inner products n_i = (chi, chi_i) (Corollary 10.4.8).
# Prerequisites
- **Irreducible representation** — The building blocks
- **Maschke's theorem** — Guarantees complete reducibility for finite groups
# Key Properties
1. Every representation of a finite group is completely reducible (Maschke)
2. The decomposition rho = n_1 rho_1 + ... + n_r rho_r is unique up to isomorphism
3. Multiplicities determined by n_i = (chi, chi_i)
4. Matrix form: block diagonal with blocks A_g, B_g, ...
# Examples
**Example 1** (p. 308): The 3D representation M of S_3 as rotations decomposes as A + Sigma (standard + sign).
# Relationships
## Builds Upon
- **Irreducible representation** — Direct sum of irreducibles
- **Maschke's theorem** — Guarantees the decomposition exists
# Source Reference
Chapter 10: Group Representations, Section 10.2, pages 306-309.
# Verification Notes
- Definition source: Synthesized from Sections 10.2 and 10.4
- Confidence rationale: Well-defined concept
- Uncertainties: None
- Cross-reference status: Verified
