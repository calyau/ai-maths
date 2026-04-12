---
concept: Irreducible Representation
slug: irreducible-representation
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
aliases: ["irrep"]
prerequisites: [group-representation]
extends: [group-representation]
related: [maschkes-theorem, schurs-lemma, completely-reducible-representation]
contrasts_with: [reducible-representation]
answers_questions: ["What is an irreducible representation?"]
---
# Quick Definition
A representation rho of G on V is irreducible if V has no proper G-invariant subspace. Irreducible representations are the building blocks: by Maschke's theorem, every representation of a finite group is a direct sum of irreducibles.
# Core Definition
If rho is a representation of G on V and V has no proper G-invariant subspace, rho is called irreducible. If V has a proper G-invariant subspace, rho is reducible (Artin, p. 307). A subspace W is G-invariant if gW subset W for all g (10.2.4). An irreducible character is the character of an irreducible representation.
# Prerequisites
- **Group representation** — Irreducibility is a property of representations
# Key Properties
1. No proper G-invariant subspaces (only {0} and V)
2. One-dimensional representations are always irreducible
3. (chi, chi) = 1 iff chi is irreducible (follows from (10.4.10))
4. The number of irreducible representations equals the number of conjugacy classes (Main Theorem 10.4.6(b))
5. Dimensions d_i satisfy |G| = d_1^2 + ... + d_r^2 (Main Theorem 10.4.6(c))
6. d_i divides |G| (stated in Main Theorem, proof not given)
# Construction / Recognition
## To Recognize:
1. Check that (chi, chi) = 1 where chi is the character
2. Or verify there are no proper G-invariant subspaces
# Context & Application
Irreducible representations are the atoms of representation theory. Every representation decomposes uniquely into irreducibles (Maschke + Main Theorem). Finding all irreducible representations of a group amounts to filling in the character table.
# Examples
**Example 1** (p. 307): The standard 2D representation A of S_3 is irreducible (verified: (chi_A, chi_A) = 1).
**Example 2** (p. 302): Any one-dimensional representation (like T or Sigma for S_3) is automatically irreducible.
# Relationships
## Builds Upon
- **Group representation** — Irreducibility is a property of representations
## Enables
- **Character table** — Rows are irreducible characters
- **Main theorem on characters** — Irreducible characters are orthonormal
## Related
- **Maschke's theorem** — Every representation is a direct sum of irreducibles
- **Schur's lemma** — Fundamental structural result for irreducible representations
## Contrasts With
- **Reducible representation** — Has proper G-invariant subspaces
# Common Errors
- **Error**: Assuming a representation is irreducible because no block decomposition is visible
  **Correction**: The matrix representation may need a change of basis to reveal a block decomposition
# Common Confusions
- **Confusion**: Thinking irreducible over R is the same as irreducible over C
  **Clarification**: A representation can be irreducible over R but reducible over C
# Source Reference
Chapter 10: Group Representations, Section 10.2, pages 306-309.
# Verification Notes
- Definition source: Direct from p. 307
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
