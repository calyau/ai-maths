---
concept: Properties of the Lie Functor
slug: lie-functor-properties
category: lie-algebras
subcategory: null
tier: intermediate
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Lie Algebras and Algebraic Groups"
chapter_number: 2
pdf_page: 255
section: "2 Lie algebras and algebraic groups"
extraction_confidence: high
aliases: []
prerequisites:
  - lie-algebra-of-algebraic-group
extends: []
related:
  - semisimple-algebraic-group
  - semisimple-lie-algebra
contrasts_with: []
answers_questions:
  - "How does the Lie algebra functor connect algebraic groups to Lie algebras?"
---

# Quick Definition

In characteristic zero, the Lie functor G -> Lie(G) from connected algebraic groups to Lie algebras is faithful (injective on Hom sets), exact on short exact sequences, and sends semisimple groups to semisimple Lie algebras. It is not fully faithful or right exact.

# Core Definition

The functor Lie from algebraic groups to Lie algebras has the following properties in characteristic zero (Milne, Section 2):
- dim Lie(G) >= dim G, with equality iff G smooth (Proposition 2.2)
- If Lie(H) = Lie(G) and H smooth connected subgroup of connected G, then H = G (Proposition 2.5)
- If G connected and char 0, a surjection on Lie algebras implies surjection on groups (Corollary 2.6)
- In char 0, exact sequences of groups give exact sequences of Lie algebras (Corollary 2.7)
- H -> Lie(H) is injective on connected subgroups in char 0 (Theorem 2.11)
- Lie(alpha) = Lie(beta) and G connected implies alpha = beta in char 0 (Proposition 2.13)

# Prerequisites

- **Lie algebra of algebraic group** -- The Lie functor is the main object of study

# Key Properties

1. Lie preserves fibred products (Proposition 1.34)
2. Lie(Ker(alpha)) = Ker(Lie(alpha)) (Example 1.36)
3. In char 0, Lie is faithful on connected groups but NOT fully faithful (p. 258)
4. Lie is NOT right exact: the sequence Lie is left exact but not exact on the right (1.39)
5. Lie is trivial on etale groups (1.18): Lie(G) = 0 for finite etale G
6. Normal subgroups correspond to ideals (2.23): H normal in G implies Lie(H) ideal in Lie(G)

# Context & Application

The Lie functor provides the fundamental dictionary between algebraic groups and Lie algebras. In characteristic zero for connected groups, it captures most of the structure -- subgroups, quotients, normality, centrality -- making Lie algebras the primary computational tool for studying algebraic groups.

# Examples

**Example 1** (p. 256): Lie is NOT fully faithful: End(G_m) = Z but End(Lie(G_m)) = k.

**Example 2** (p. 257): Infinitely many groups can share the same Lie algebra: G_n = G_a rtimes G_m with action t^n gives Lie(G_n) = <x,y | [x,y] = y> for all nonzero n.

# Relationships

## Builds Upon
- **Lie algebra of algebraic group** -- The functor Lie

## Enables
- **Semisimple algebraic group** -- G semisimple iff Lie(G) semisimple (in char 0)

# Common Errors

- **Error**: Believing Lie is fully faithful (that Lie algebra homomorphisms always come from group homomorphisms)
  **Correction**: End(G_m) = Z != k = End(Lie(G_m)); not all Lie algebra maps lift to group maps

# Source Reference

Chapter II: Lie Algebras and Algebraic Groups, Section 2, pages 254-263.

# Verification Notes

- Definition source: Synthesized from multiple propositions in Section 2
- Confidence rationale: Multiple explicit theorems
- Uncertainties: None
- Cross-reference status: Verified
