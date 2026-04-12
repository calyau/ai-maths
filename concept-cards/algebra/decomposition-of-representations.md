---
concept: Decomposition of Representations
slug: decomposition-of-representations
category: group-representations
subcategory: null
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Group Representations"
chapter_number: 10
pdf_page: 301
section: "10.4 Characters"
extraction_confidence: high
aliases: ["projection formula for representations"]
prerequisites: [orthogonality-of-characters, maschkes-theorem]
extends: []
related: [character-table]
contrasts_with: []
answers_questions: ["How do I decompose a representation into irreducibles?"]
---
# Quick Definition
Any representation rho of a finite group decomposes uniquely as rho = n_1 rho_1 + ... + n_r rho_r, where the multiplicities n_i = (chi, chi_i) are computed using the Hermitian product of the character chi with the irreducible characters chi_i.
# Core Definition
Corollary 10.4.8: Let rho_1, ..., rho_r represent the isomorphism classes of irreducible representations, and let rho be any representation with character chi. Then: (a) chi = n_1 chi_1 + ... + n_r chi_r, and (b) rho is isomorphic to n_1 rho_1 + ... + n_r rho_r, where n_i = (chi, chi_i) (Artin, p. 312).
# Prerequisites
- **Orthogonality of characters** — Used to compute the multiplicities
- **Maschke's theorem** — Guarantees the decomposition exists
# Key Properties
1. n_i = (chi, chi_i) is always a non-negative integer
2. Decomposition is unique (up to isomorphism)
3. (chi, chi) = n_1^2 + ... + n_r^2 (10.4.10)
4. (chi, chi) = 1 iff rho is irreducible
5. chi determines rho up to isomorphism
# Examples
**Example 1** (p. 312): For the regular representation of S_3: chi^reg = chi_1 + chi_2 + 2 chi_3 (multiplicities 1, 1, 2).
# Relationships
## Builds Upon
- **Orthogonality of characters** — The projection formula
- **Maschke's theorem** — Existence of decomposition
## Related
- **Character table** — Used to compute decompositions
# Source Reference
Chapter 10: Group Representations, Section 10.4, Corollary 10.4.8, page 312.
# Verification Notes
- Definition source: Direct from Corollary 10.4.8
- Confidence rationale: Explicitly stated
- Uncertainties: None
- Cross-reference status: Verified
