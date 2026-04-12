---
concept: Orthogonality of Characters
slug: orthogonality-of-characters
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
aliases: ["orthogonality relations", "first orthogonality relation"]
prerequisites: [character-of-a-representation, irreducible-representation]
extends: []
related: [schurs-lemma, character-table, main-theorem-on-characters]
contrasts_with: []
answers_questions: ["What are the orthogonality relations for characters?"]
---
# Quick Definition
The irreducible characters of a finite group are orthonormal with respect to the Hermitian product (chi, chi') = (1/|G|) sum_g chi(g)-bar chi'(g). This means (chi_i, chi_i) = 1 and (chi_i, chi_j) = 0 for non-isomorphic irreducibles.
# Core Definition
The orthogonality relations (Main Theorem 10.4.6(a)): If chi_i is the character of an irreducible representation rho_i, then (chi_i, chi_i) = 1. If chi_i and chi_j are characters of non-isomorphic irreducible representations, then (chi_i, chi_j) = 0 (Artin, p. 311). The Hermitian product is (chi, chi') = (1/|G|) sum_g chi(g)-bar chi'(g), which can be rewritten by grouping conjugacy classes: (1/|G|) sum_{i=1}^r c_i chi(g_i)-bar chi'(g_i) where c_i = |C_i|.
# Prerequisites
- **Character of a representation** — The objects being compared
- **Irreducible representation** — Orthogonality holds for irreducible characters
# Key Properties
1. (chi_i, chi_j) = delta_{ij} for irreducible characters (Main Theorem)
2. Any character can be decomposed: n_i = (chi, chi_i) (Corollary 10.4.8)
3. (chi, chi) = n_1^2 + ... + n_r^2 where chi = sum n_i chi_i (10.4.10)
4. (chi, chi) = 1 iff chi is irreducible
5. Columns of the character table are also orthogonal (Exercise 4.6)
6. Proved using Schur's Lemma and the averaging process (Section 10.8)
# Context & Application
The orthogonality relations are described by Artin as "one of the most beautiful theorems of algebra." They reduce representation classification to a linear algebra problem and make the character table a powerful computational tool.
# Examples
**Example 1** (p. 311): For S_3: (chi_A, chi_A) = (1/6)(4 + 2 + 0) = 1 and (chi_A, chi_Sigma) = (1/6)(2 + (-2) + 0) = 0.
# Relationships
## Builds Upon
- **Character of a representation** — Orthogonality is a property of characters
## Enables
- **Character table** — Computed using orthogonality
- **Decomposition of representations** — n_i = (chi, chi_i)
## Related
- **Schur's lemma** — Used in the proof
# Source Reference
Chapter 10: Group Representations, Section 10.4, Main Theorem 10.4.6, pages 311-312. Proof in Section 10.8.
# Verification Notes
- Definition source: Direct from Main Theorem 10.4.6(a)
- Confidence rationale: Central theorem, fully proved in Section 10.8
- Uncertainties: None
- Cross-reference status: Verified
