---
# === CORE IDENTIFICATION ===
concept: Roots of Unity in Fields
slug: roots-of-unity-in-fields

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
pdf_page: 101
section: "Roots of 1 in fields"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "mu_n(F)"
  - "nth roots of unity"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
extends: []
related:
  - primitive-root-of-unity
  - matrix-representation
  - representations-of-abelian-groups
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is mu_n(F)?"
  - "How do roots of unity in a field affect group representations?"
---

# Quick Definition

The nth roots of unity in a field F form a cyclic subgroup mu_n(F) of F^x. Their existence in F determines what representations of cyclic (and abelian) groups are available over F.

# Core Definition

The nth roots of 1 in a field F form a subgroup mu_n(F) of F^x, which is cyclic. If char(F) divides n, then |mu_n(F)| < n. Otherwise, X^n - 1 has distinct roots, and one can always arrange that |mu_n(F)| = n by extending F. (Milne, Chapter 7, p. 101)

# Prerequisites

- **Group** — mu_n(F) is a cyclic subgroup of F^x

# Key Properties

1. mu_n(F) is always a cyclic group (by 1.56)
2. |mu_n(F)| = n when char(F) does not divide n and F is large enough
3. If char(F) divides n, then |mu_n(F)| < n because X^n - 1 has repeated roots
4. Can always enlarge F to contain all nth roots of unity (e.g., F[zeta] where zeta = e^{2pi i/n}, or F[X]/(g(X)))

# Construction / Recognition

1. Solve X^n = 1 in F
2. The solutions form mu_n(F)
3. If char(F) does not divide n, then X^n - 1 has n distinct roots (derivative nX^{n-1} shares no roots)
4. If char(F) | n, then X^n - 1 has fewer than n distinct roots

# Context & Application

The representations of a group over F depend crucially on the roots of 1 available in F. For a cyclic group C_n, the 1-dimensional representations are determined by nth roots of unity. This motivates working over algebraically closed fields or fields containing enough roots of unity.

# Examples

**Example 1** (p. 101): For F a subfield of C, mu_n(F) can be enlarged to have order n by replacing F with F[e^{2pi i/n}].

**Example 2** (p. 101): If n = p = char(F), then X^p - 1 = (X-1)^p, so mu_p(F) = {1}.

# Relationships

## Builds Upon
- Cyclic groups, field theory

## Enables
- **primitive-root-of-unity** — generators of mu_n(F)
- **representations-of-abelian-groups** — decomposition depends on roots of unity

## Related
- **matrix-representation** — 1-dimensional representations of C_n correspond to elements of mu_n(F)

## Contrasts With
- Roots of unity in characteristic dividing n vs. not dividing n

# Common Errors

- **Error**: Assuming mu_n(F) always has order n
  **Correction**: This fails when char(F) divides n

# Common Confusions

- **Confusion**: Confusing "F contains a primitive nth root of unity" with "char(F) does not divide n"
  **Clarification**: Char(F) not dividing n is necessary but not sufficient; F must also be large enough to contain all roots

# Source Reference

Chapter 7: Representations of Finite Groups, "Roots of 1 in fields" subsection, p. 101.

# Verification Notes

- Definition source: Direct from p. 101
- Confidence rationale: HIGH — explicit discussion
- Uncertainties: None
