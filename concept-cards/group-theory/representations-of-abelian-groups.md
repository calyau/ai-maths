---
# === CORE IDENTIFICATION ===
concept: Representations of Abelian Groups
slug: representations-of-abelian-groups

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
pdf_page: 102
section: "Linear representations"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - linear-representation
  - roots-of-unity-in-fields
extends: []
related:
  - one-dimensional-representation
  - linear-character
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the irreducible representations of an abelian group?"
  - "How do representations of abelian groups decompose?"
---

# Quick Definition

For an abelian group G of exponent n over a field containing a primitive nth root of unity, every irreducible representation is 1-dimensional. Representations decompose as direct sums of eigenspaces indexed by characters chi in G^v = Hom(G, F^x).

# Core Definition

Let G be a commutative group of exponent n, and assume F contains a primitive nth root of 1. Let G^v = Hom(G, F^x) = Hom(G, mu_n(F)). To give a representation of G on V is the same as giving a direct sum decomposition V = direct sum_{chi in G^v} V_chi, where V_chi = {v in V : gv = chi(g)v for all g in G}. (Milne, Example 7.3b, p. 102)

# Prerequisites

- **Linear representation** — these are representations of abelian groups
- **Roots of unity in fields** — primitive roots needed for the decomposition

# Key Properties

1. Every irreducible representation is 1-dimensional
2. Representations are determined by the dual group G^v = Hom(G, F^x)
3. V decomposes as V = direct sum V_chi indexed by chi in G^v
4. For cyclic G = C_n: reduces to eigenspace decomposition for powers of a primitive nth root

# Examples

**Example 1** (p. 102, 7.3a): For C_n = <sigma> with primitive nth root zeta: V = direct sum V_i where sigma acts as zeta^i on V_i.

**Example 2** (p. 102, 7.3b): For general abelian G: decompose iteratively using the cyclic factors.

**Example 3** (p. 117, 7.53): Character table of C_3 has 3 irreducible representations, all 1-dimensional.

# Relationships

## Builds Upon
- **linear-representation** — abelian case
- **roots-of-unity-in-fields** — needed for eigenspace decomposition

## Enables
- Understanding character tables of abelian groups

## Related
- **one-dimensional-representation** — all irreducibles are 1-dimensional
- **linear-character** — characters of abelian groups are group homomorphisms

# Source Reference

Chapter 7: Representations of Finite Groups, Example 7.3, p. 102.

# Verification Notes

- Definition source: Direct from Example 7.3
- Confidence rationale: HIGH — explicit discussion
- Uncertainties: None
