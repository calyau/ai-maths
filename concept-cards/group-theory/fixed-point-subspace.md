---
# === CORE IDENTIFICATION ===
concept: Fixed-Point Subspace
slug: fixed-point-subspace

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
pdf_page: 116
section: "The characters of G"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "V^G"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - linear-representation
extends:
  - g-invariant-subspace
related:
  - character-of-a-representation
contrasts_with:
  - g-invariant-subspace

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the fixed-point subspace V^G?"
  - "How does the dimension of V^G relate to the character?"
---

# Quick Definition

For an F[G]-module V, the fixed-point subspace V^G = {v in V : gv = v for all g in G} is the subspace of vectors fixed by all group elements.

# Core Definition

For an F[G]-module V, **V^G** denotes the submodule of elements fixed by G: V^G = {v in V : gv = v for all g in G}. The element pi = (1/|G|) sum_{a in G} a of F[G] is a projector with image V^G (Lemma 7.49), and dim_F(V^G) = (1/|G|) sum_{a in G} chi_V(a) (Proposition 7.50). (Milne, pp. 116-117)

# Prerequisites

- **Linear representation** — V^G is defined for representation spaces

# Key Properties

1. V^G is a G-invariant subspace (in fact, every g acts as identity on it)
2. pi = (1/|G|) sum a is a projector onto V^G (7.49)
3. dim V^G = (1/|G|) sum chi_V(a) = average of the character values (7.50)
4. For the regular representation: F[G]^G has dimension 1

# Construction / Recognition

1. Compute the averaging operator pi_V = (1/|G|) sum_{a in G} a_V
2. The image of pi_V is V^G
3. dim V^G = Tr(pi_V) = (1/|G|) sum chi_V(a)

# Context & Application

The fixed-point formula dim V^G = (1/|G|) sum chi_V(a) is a key step in proving the orthogonality relations. It connects the character to the algebraic structure of the module.

# Examples

**Example 1** (p. 116-117): pi = (1/|G|) sum a satisfies g pi = pi for all g, so pi^2 = pi and Im(pi_V) = V^G.

# Relationships

## Builds Upon
- **linear-representation** — V^G is defined for representations

## Enables
- Dimension formula for Hom spaces (7.51)
- **orthogonality-relations** — via dim V^G formula

## Related
- **character-of-a-representation** — dim V^G computed from the character

## Contrasts With
- **g-invariant-subspace** — V^G is fixed pointwise; a G-invariant subspace is just preserved setwise

# Source Reference

Chapter 7: Representations of Finite Groups, Lemma 7.49 and Proposition 7.50, pp. 116-117.

# Verification Notes

- Definition source: Direct from p. 116
- Confidence rationale: HIGH — explicit definition and formula
- Uncertainties: None
