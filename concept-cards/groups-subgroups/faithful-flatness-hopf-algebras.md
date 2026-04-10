---
# === CORE IDENTIFICATION ===
concept: Faithful Flatness of Hopf Algebras
slug: faithful-flatness-hopf-algebras

# === CLASSIFICATION ===
category: hopf-algebras
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 69
section: "Affine groups and affine group schemes"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - hopf-algebra
extends: []
related:
  - surjective-homomorphism
  - affine-subgroup
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Hopf algebra?"
  - "How does a Hopf algebra relate to an affine algebraic group?"
---

# Quick Definition

For any inclusion A subset B of Hopf algebras over a field k, B is faithfully flat over A. This fundamental technical result underpins the theory of quotients and surjective homomorphisms.

# Core Definition

**Theorem 6.43** (p. 69): For any Hopf algebras A subset B over a field k, B is faithfully flat over A.

This result is essential for the theory of surjective homomorphisms: it is used in Theorem 7.51 to show that G -> Q is surjective iff O(Q) -> O(G) is injective (the faithful flatness ensures the converse direction).

# Prerequisites

- **Hopf algebra** — The theorem concerns inclusions of Hopf algebras

# Key Properties

1. Any Hopf subalgebra inclusion is faithfully flat
2. This implies that O(Q) -> O(G) being injective forces the homomorphism to be surjective
3. Used in the proof of Theorem 7.51 (characterization of surjective homomorphisms)
4. Used in the proof of Proposition 7.1 (criterion to be an isomorphism)

# Context & Application

This is described as a "very important technical result" (p. 69). It connects the algebraic condition (injectivity of coordinate ring map) with the geometric condition (surjectivity of the group homomorphism). Without this theorem, the equivalence between surjective homomorphisms and injective maps on coordinate rings would fail.

# Relationships

## Related
- **Surjective homomorphism** — This theorem powers the characterization of surjectivity
- **Affine subgroup** — Subgroup inclusions give Hopf algebra inclusions, which are faithfully flat

# Source Reference

Chapter I, Section 6o, Theorem 6.43 (p. 69).

# Verification Notes

- Definition source: Direct from Theorem 6.43
- Confidence rationale: Named theorem stated explicitly
- Uncertainties: None
- Cross-reference status: Verified
