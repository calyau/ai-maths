---
# === CORE IDENTIFICATION ===
concept: Reduced Algebraic Group
slug: reduced-algebraic-group

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
pdf_page: 61
section: "Affine groups and affine group schemes"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "G_{red}"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - affine-algebraic-group
extends: []
related:
  - smooth-algebraic-group
  - cartier-theorem
contrasts_with:
  - smooth-algebraic-group

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an affine algebraic group?"
  - "What distinguishes an algebraic group from a group scheme?"
---

# Quick Definition

An algebraic group G is reduced if O(G) has no nilpotent elements. Over a perfect field, the reduced algebraic group G_{red} attached to G always exists and is smooth. Over non-perfect fields, a Hopf algebra structure on O(G) may not descend to O(G)/N.

# Core Definition

An algebraic group G is **reduced** if |G| is reduced, i.e., if O(G) has no nilpotents (Section 6i, p. 61).

**Proposition 6.18** (p. 61): Over a perfect field k, if N is the nilradical of O(G), there is a unique Hopf algebra structure on O(G)/N such that O(G) -> O(G)/N is a Hopf algebra homomorphism. The corresponding algebraic group G_{red} is the **reduced algebraic group attached to G**. Every homomorphism H -> G with H reduced factors uniquely through G_{red}.

**Warning** (6.19, p. 62): Over non-perfect fields, a Hopf algebra structure on O(G) may not pass to O(G)/N.

**Proposition 6.16** (p. 61): A reduced algebraic group G with G(K) = {1} for some algebraically closed K must be trivial (O(G) = k).

# Prerequisites

- **Affine algebraic group** — Reduced is a property of algebraic groups

# Key Properties

1. O(G) has no nilpotent elements
2. Over perfect fields: reduced iff smooth (Proposition 6.26b)
3. Over non-perfect fields: reduced does NOT imply smooth (Example 6.28)
4. G_{red} exists over perfect fields and is universal for maps from reduced groups
5. A reduced algebraic group G with G(K) = {1} for algebraically closed K is trivial (6.16)

# Examples

**Example 1** (p. 63): Over a non-perfect field of characteristic 2 with non-square a, the group defined by Y^p = aX^p in G_a x G_a is reduced but not smooth.

**Example 2** (p. 61): alpha_p is not reduced (O(alpha_p) = k[T]/(T^p) has nilpotents).

# Relationships

## Related
- **Smooth algebraic group** — Smooth implies reduced; equivalent over perfect fields
- **Cartier theorem** — In characteristic zero, all algebraic groups are smooth (hence reduced)

## Contrasts With
- **Smooth algebraic group** — Over non-perfect fields, reduced is weaker than smooth

# Source Reference

Chapter I, Section 6i (p. 61), Proposition 6.18, Proposition 6.16.

# Verification Notes

- Definition source: Direct from Section 6i
- Confidence rationale: Explicit definition with examples and counterexamples
- Uncertainties: None
- Cross-reference status: Verified
