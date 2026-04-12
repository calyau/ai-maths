---
concept: "Maschke's Theorem"
slug: maschkes-theorem
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
prerequisites: [irreducible-representation, unitary-representation]
extends: []
related: [g-invariant-hermitian-form]
contrasts_with: []
answers_questions: ["What is Maschke's theorem?"]
---
# Quick Definition
Maschke's Theorem states that every representation of a finite group G on a nonzero, finite-dimensional complex vector space is a direct sum of irreducible representations.
# Core Definition
Theorem 10.2.10 (Maschke's Theorem): Every representation of a finite group G on a nonzero, finite-dimensional complex vector space is a direct sum of irreducible representations (Artin, p. 307). The proof (Corollary 10.3.8(a)) proceeds by: (1) constructing a G-invariant positive definite Hermitian form by averaging (Theorem 10.3.6), (2) showing that if W is G-invariant, then W^perp is also G-invariant (Lemma 10.3.4), (3) inducting on dimension.
# Prerequisites
- **Irreducible representation** — The building blocks in the decomposition
- **Unitary representation** — The proof goes through unitary representations
# Key Properties
1. Applies to FINITE groups over C
2. Decomposition exists (but may not be unique as subspaces, only unique up to isomorphism)
3. The key tool is averaging over the group to construct G-invariant forms
4. Fails for infinite groups and for representations over fields of characteristic dividing |G|
# Context & Application
Maschke's theorem is the fundamental structural result of representation theory of finite groups. It reduces the study of all representations to the study of irreducible ones. The averaging technique used in the proof is a recurring tool.
# Examples
**Example 1** (p. 308): The permutation representation N of S_3 on C^3 decomposes as T direct-sum A (trivial plus standard), verified using orthogonal complements.
# Relationships
## Builds Upon
- **Irreducible representation** — Provides the building blocks
## Enables
- **Main theorem on characters** — Irreducible decomposition is unique
# Common Errors
- **Error**: Applying Maschke's theorem to infinite groups
  **Correction**: The theorem requires the group to be finite (the averaging uses 1/|G|)
# Source Reference
Chapter 10: Group Representations, Sections 10.2-10.3. Theorem 10.2.10, Corollary 10.3.8.
# Verification Notes
- Definition source: Direct from Theorem 10.2.10
- Confidence rationale: Major theorem, fully proved
- Uncertainties: None
- Cross-reference status: Verified
