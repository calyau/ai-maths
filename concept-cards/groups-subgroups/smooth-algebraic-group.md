---
# === CORE IDENTIFICATION ===
concept: Smooth Algebraic Group
slug: smooth-algebraic-group

# === CLASSIFICATION ===
category: algebraic-groups
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 62
section: "Smooth algebraic groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - affine-algebraic-group
  - reduced-algebraic-group
extends:
  - reduced-algebraic-group
related:
  - cartier-theorem
  - affine-group-scheme
contrasts_with:
  - reduced-algebraic-group

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an affine algebraic group?"
  - "What distinguishes an algebraic group from a group scheme?"
---

# Quick Definition

An algebraic group G is smooth if |G_{k^{al}}| is regular as an algebraic scheme. By Cartier's theorem, every algebraic group over a field of characteristic zero is smooth.

# Core Definition

An algebraic group G is said to be **smooth** if |G| is smooth, i.e., if G_{k^{al}} is regular (6.23, p. 62). G is **connected** if |G| is connected as a topological space.

Key characterizations (over a field k):
- G is smooth iff |G| is geometrically reduced (an algebraic variety) (Proposition 6.26a, p. 63)
- Over a perfect field, G is smooth iff |G| is reduced (Proposition 6.26b)
- Over algebraically closed k, G is smooth iff O(G)_{m_e} is a regular local ring (Proposition 6.25, p. 63)

**Cartier's Theorem** (6.31, p. 65): Every algebraic group over a field of characteristic zero is smooth.

# Prerequisites

- **Affine algebraic group** — Smoothness is a property of algebraic groups
- **Reduced algebraic group** — Smooth implies reduced; the converse holds over perfect fields

# Key Properties

1. Smooth iff geometrically reduced (6.26a)
2. Over perfect fields: smooth iff reduced (6.26b)
3. In characteristic zero: always smooth (Cartier's theorem)
4. Quotients and extensions of smooth groups are smooth (Proposition 7.66, p. 90)
5. Kernels of homomorphisms of smooth groups need NOT be smooth (7.67, p. 90)

# Examples

**Example 1** (p. 63): Over a nonperfect field of characteristic 2 with a non-square a, the subgroup G of G_a x G_a defined by Y^p = aX^p is reduced but not smooth (6.28).

**Example 2** (p. 90): The kernel of x -> x^p: G_m -> G_m is mu_p, which is not smooth in characteristic p.

# Relationships

## Extends
- **Reduced algebraic group** — Smooth implies reduced; equivalent over perfect fields

## Related
- **Cartier theorem** — Guarantees smoothness in characteristic zero

## Contrasts With
- **Reduced algebraic group** — Over non-perfect fields, reduced does not imply smooth

# Source Reference

Chapter I, Section 6k "Smooth algebraic groups" (p. 62-63), Cartier's theorem 6.31 (p. 65).

# Verification Notes

- Definition source: Direct from Propositions 6.25, 6.26
- Confidence rationale: Explicit characterizations
- Uncertainties: None
- Cross-reference status: Verified
