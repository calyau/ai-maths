---
# === CORE IDENTIFICATION ===
concept: Cartier's Theorem
slug: cartier-theorem

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
pdf_page: 65
section: "Algebraic groups in characteristic zero are smooth"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - affine-algebraic-group
  - hopf-algebra
  - smooth-algebraic-group
extends: []
related:
  - reduced-algebraic-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an affine algebraic group?"
  - "What distinguishes an algebraic group from a group scheme?"
---

# Quick Definition

Cartier's theorem (1962) states that every algebraic group over a field of characteristic zero is smooth. This means the coordinate ring is automatically reduced (no nilpotent elements) in characteristic zero.

# Core Definition

**Theorem 6.31** (Cartier 1962, p. 65): Every algebraic group over a field of characteristic zero is smooth.

The proof uses the Hopf algebra structure of O(G). The key steps are:
1. Let a be a nilpotent element of O(G) and m = m_e = Ker(epsilon). It suffices to show a lies in m^2 (by Corollary 6.27).
2. By Lemma 6.30, Delta(a) = a tensor 1 + 1 tensor a (mod m tensor m) for a in m (the "primitive" property modulo m tensor m).
3. Expanding Delta(a^n) = (Delta(a))^n = 0 and using characteristic zero (n is invertible), one shows a must lie in m^2.

**Corollary 6.32**: If G(K) = {1} for some algebraically closed field K, then G is the trivial algebraic group (in characteristic zero).

# Prerequisites

- **Affine algebraic group** — The theorem applies to algebraic groups
- **Hopf algebra** — The proof uses the Hopf algebra structure
- **Smooth algebraic group** — The conclusion of the theorem

# Key Properties

1. Fails in characteristic p: alpha_p and mu_p are non-smooth algebraic groups
2. Implies that in characteristic zero, algebraic group = group variety
3. Extends to: every flat affine group scheme of finite presentation over a ring containing Q is smooth (Aside 6.33)

# Examples

**Example 1** (p. 61): alpha_p over a field of characteristic p has alpha_p(K) = {0} for all fields K, yet is nontrivial -- showing the corollary fails in characteristic p.

# Relationships

## Related
- **Smooth algebraic group** — Cartier's theorem says all characteristic-zero algebraic groups are smooth
- **Reduced algebraic group** — Smooth implies reduced; in characteristic zero both are automatic

# Source Reference

Chapter I, Section 6l, Theorem 6.31 (p. 65), Corollary 6.32.

# Verification Notes

- Definition source: Direct from Theorem 6.31
- Confidence rationale: Named theorem with full proof
- Uncertainties: None
- Cross-reference status: Verified
