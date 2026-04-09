---
# === CORE IDENTIFICATION ===
concept: Decomposition of F[G]
slug: decomposition-of-f-g

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
  - wedderburn-artin-theorem
  - maschke-theorem
extends: []
related:
  - irreducible-representation
  - degree-of-representation
  - number-of-irreducible-representations
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does F[G] decompose as a product of matrix algebras?"
  - "What is the relationship between the decomposition of F[G] and the irreducible representations?"
---

# Quick Definition

Over an algebraically closed field F of characteristic zero, F[G] is isomorphic to M_{f_1}(F) x ... x M_{f_t}(F), where the f_i are the degrees of the irreducible representations and sum f_i^2 = |G|.

# Core Definition

**Proposition 7.40.** The group algebra F[G] is isomorphic to a product of matrix algebras over F (when F is algebraically closed of characteristic zero). **Theorem 7.41.** (a) t = number of conjugacy classes. (b) Each simple representation S_i appears with multiplicity f_i = dim S_i in the regular representation. (c) sum_{i=1}^t f_i^2 = |G|. (Milne, pp. 113-114)

# Prerequisites

- **Group algebra** — F[G] is decomposed
- **Wedderburn-Artin theorem** — provides the product structure
- **Maschke's theorem** — ensures F[G] is semisimple

# Key Properties

1. F[G] = M_{f_1}(F) x ... x M_{f_t}(F)
2. t = number of conjugacy classes of G
3. f_i = dim_F(S_i) for the ith irreducible representation
4. sum f_i^2 = |G| (dimension count)
5. Multiplicity of S_i in the regular representation equals f_i
6. The centre of F[G] has dimension t

# Construction / Recognition

1. By Maschke's theorem, F[G] is semisimple
2. By Wedderburn-Artin, F[G] = product of simple algebras
3. Over algebraically closed F, each simple algebra is M_n(F)
4. The sizes n_i are determined by the dimensions of the irreducible representations

# Context & Application

This decomposition is the bridge from abstract algebra to computational character theory. It shows that the representation theory of G is completely determined by the integers f_1, ..., f_t (and the conjugacy classes). The equation sum f_i^2 = |G| is a powerful constraint.

# Examples

**Example 1** (p. 114): For S_3 with |G| = 6 and 3 conjugacy classes: f_1^2 + f_2^2 + f_3^2 = 6, so (f_1, f_2, f_3) = (1, 1, 2).

**Example 2** (p. 114): For D_4 or Q_8 with |G| = 8 and 5 conjugacy classes: f_1^2 + ... + f_5^2 = 8, so (1,1,1,1,2).

# Relationships

## Builds Upon
- **group-algebra** — the object being decomposed
- **wedderburn-artin-theorem** — the structural framework
- **maschke-theorem** — ensures semisimplicity

## Enables
- **character-table** — the decomposition determines possible character tables
- **number-of-irreducible-representations** — equals number of conjugacy classes

## Related
- **regular-representation** — G acting on F[G]
- **degree-of-representation** — the f_i

## Contrasts With
- Non-semisimple case (char(F) | |G|): no clean decomposition

# Common Errors

- **Error**: Forgetting the condition that F is algebraically closed
  **Correction**: Over non-algebraically closed fields, the simple factors may be M_n(D) with D != F

# Source Reference

Chapter 7: Representations of Finite Groups, Proposition 7.40 and Theorem 7.41, pp. 113-114.

# Verification Notes

- Definition source: Direct from Proposition 7.40 and Theorem 7.41
- Confidence rationale: HIGH — explicit theorems
- Uncertainties: None
