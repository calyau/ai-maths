---
# === CORE IDENTIFICATION ===
concept: One-dimensional Representation
slug: one-dimensional-representation

# === CLASSIFICATION ===
category: representation-theory
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Representations of Finite Groups"
chapter_number: 7
pdf_page: 114
section: "The characters of G"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "degree-1 representation"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - linear-representation
extends:
  - irreducible-representation
related:
  - linear-character
  - representations-of-abelian-groups
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a 1-dimensional representation?"
  - "When is a representation automatically irreducible?"
---

# Quick Definition

A 1-dimensional representation is a homomorphism G -> F^x. It is automatically irreducible. Its character equals the representation itself.

# Core Definition

A representation of degree 1 is a homomorphism G -> GL_1(F) = F^x. Since a 1-dimensional space has no proper nonzero subspaces, every 1-dimensional representation is irreducible. Its character chi(g) = rho(g) is a homomorphism G -> F^x, called a **linear character**. (Milne, Chapter 7, p. 114)

# Prerequisites

- **Linear representation** — 1-dimensional is a special case

# Key Properties

1. Automatically irreducible (no proper nonzero subspaces)
2. Character = representation (chi(g) = rho(g))
3. The character is a group homomorphism G -> F^x
4. Number of 1-dimensional representations = [G : G'] (index of commutator subgroup)
5. For abelian groups, all irreducible representations are 1-dimensional

# Examples

**Example 1** (p. 100, 7.1c): sigma^i -> zeta^i: C_n -> F^x is a 1-dimensional representation.

**Example 2** (p. 117): The sign representation sigma -> sgn(sigma): S_n -> {+1, -1} is 1-dimensional.

# Relationships

## Builds Upon
- **linear-representation** — special case

## Enables
- **linear-character** — same as the character of a 1-dimensional representation
- **representations-of-abelian-groups** — all irreducible reps are 1-dimensional

## Related
- Detection of the commutator subgroup: G' = intersection of kernels

# Source Reference

Chapter 7: Representations of Finite Groups, pp. 100-101, 114.

# Verification Notes

- Definition source: Synthesized from pp. 100-101, 114
- Confidence rationale: HIGH — explicit discussion
- Uncertainties: None
