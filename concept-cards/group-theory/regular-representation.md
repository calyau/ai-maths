---
# === CORE IDENTIFICATION ===
concept: Regular Representation
slug: regular-representation

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
pdf_page: 113
section: "The representations of G"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group-algebra
  - linear-representation
extends:
  - linear-representation
related:
  - decomposition-of-f-g
  - regular-character
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the regular representation of a finite group?"
  - "How does each irreducible representation appear in the regular representation?"
---

# Quick Definition

The regular representation is the representation G -> GL(F[G]) given by left multiplication of G on the group algebra F[G]. Each irreducible representation of degree f_i appears in it with multiplicity f_i.

# Core Definition

The representation G -> GL(_{F[G]}F[G]) given by the left action of G on F[G] is called the **regular representation**. Its degree is |G|. Each simple representation S_i appears in the regular representation with multiplicity equal to its degree dim_F(S_i) = f_i (Theorem 7.41b). (Milne, Chapter 7, pp. 113-114)

# Prerequisites

- **Group algebra** — the regular representation acts on F[G]
- **Linear representation** — it is a particular representation

# Key Properties

1. Degree = |G|
2. Multiplicity of S_i in the regular representation = f_i = dim S_i (7.41b)
3. sum f_i^2 = |G| (7.41c)
4. The regular character satisfies chi_reg(e) = |G| and chi_reg(g) = 0 for g != e

# Construction / Recognition

1. Take V = F[G] as an F-vector space (basis = elements of G)
2. G acts by left multiplication: g(sum c_h h) = sum c_h (gh)
3. This gives a representation of degree |G|

# Context & Application

The regular representation is the universal representation of a finite group: it contains every irreducible representation. The decomposition F[G] = M_{f_1}(F) x ... x M_{f_t}(F) shows exactly how each irreducible appears. The regular character is a key tool in proving the orthogonality relations.

# Examples

**Example 1** (p. 114): For S_3, the regular representation has degree 6 and decomposes as S_1 + S_2 + 2S_3 (multiplicities 1, 1, 2 matching degrees).

# Relationships

## Builds Upon
- **group-algebra** — the representation space
- **linear-representation** — a specific linear representation

## Enables
- **regular-character** — the character of the regular representation
- Dimension formula: sum f_i^2 = |G|

## Related
- **decomposition-of-f-g** — describes the decomposition of the regular representation

# Source Reference

Chapter 7: Representations of Finite Groups, pp. 113-114 (7.41).

# Verification Notes

- Definition source: Direct from p. 113
- Confidence rationale: HIGH — explicit definition
- Uncertainties: None
