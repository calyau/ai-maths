---
concept: Character Module X*(G)
slug: character-module
category: multiplicative-groups
subcategory: null
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 169
section: "14e Groups of multiplicative type"
extraction_confidence: high
aliases:
  - "X*(G)"
  - character lattice
prerequisites:
  - character-of-affine-group
  - group-of-multiplicative-type
extends:
  - character-of-affine-group
related:
  - algebraic-torus
  - cocharacter
contrasts_with: []
answers_questions:
  - "How do characters classify groups of multiplicative type?"
  - "How do characters and cocharacters pair in the theory of tori?"
---

# Quick Definition

For an affine group G, the character module X*(G) = Hom(G_{k^sep}, G_m) is the group of characters defined over k^sep, equipped with the continuous action of Gamma = Gal(k^sep/k). For groups of multiplicative type, X* is a contravariant equivalence to abelian groups with continuous Galois action.

# Core Definition

For an affine group G, define X*(G) = Hom(G_{k^sep}, G_m) with the canonical continuous action of Gamma = Gal(k^sep/k) (the action is continuous by Lemma 14.19). The functor X* is a contravariant equivalence from groups of multiplicative type over k to commutative groups with continuous Gamma-action, preserving short exact sequences (Theorem 14.20). For a torus T, X*(T) is a free abelian group of finite rank. The natural pairing X*(T) x X_*(T) -> Z (where X_*(T) = Hom(G_m, T_{k^sep}) is the cocharacter module) is perfect (Milne, pp. 169-170).

# Prerequisites

- **Character of affine group** -- X*(G) is the group of characters over k^sep
- **Group of multiplicative type** -- X* classifies these groups

# Key Properties

1. X* gives a contravariant equivalence (Theorem 14.20)
2. For a torus T of rank n, X*(T) = Z^n with continuous Gamma-action
3. Short exact sequences of groups correspond to short exact sequences of character modules
4. Rep(G) is semisimple with simples indexed by Gamma-orbits on X*(G) (Theorem 14.27)
5. G is split (diagonalizable) iff Gamma acts trivially on X*(G)
6. G is anisotropic iff X*(G)^Gamma = 0

# Context & Application

The character module is the fundamental invariant of groups of multiplicative type, analogous to the fundamental group in topology. For reductive groups, the character and cocharacter lattices of a maximal torus determine the root system and hence the entire group (up to isogeny).

# Examples

**Example 1** (p. 170): For T = G_m, X*(T) = Z with trivial Gamma-action.

**Example 2** (p. 170): For the Weil restriction T = (G_m)_{K/k}, X*(T) = Z^{Hom_k(K, k^sep)} with Gamma acting by permuting the Hom set.

# Relationships

## Builds Upon
- **Character of affine group** -- X*(G) collects all characters over k^sep

## Enables
- **Algebraic torus** -- Tori have torsion-free X*
- **Root system** -- Roots live in X*(T) for a maximal torus T

## Related
- **Cocharacter** -- X_*(T) pairs with X*(T)

# Source Reference

Chapter I: Basic Theory of Affine Groups, Section 14e, pages 169-170. Theorem 14.20, Lemma 14.19.

# Verification Notes

- Definition source: Direct from Section 14e
- Confidence rationale: Explicit definition as part of classification theorem
- Uncertainties: None
- Cross-reference status: Verified
