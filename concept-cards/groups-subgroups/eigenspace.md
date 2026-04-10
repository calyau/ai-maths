---
concept: Eigenspace for a Character
slug: eigenspace
category: representations
subcategory: null
tier: intermediate
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 116
section: "8p Characters and eigenspaces"
extraction_confidence: high
aliases:
  - weight space
  - chi-eigenspace
prerequisites:
  - character-of-affine-group
  - linear-representation
extends: []
related:
  - diagonalizable-group
  - split-torus
contrasts_with: []
answers_questions:
  - "What is an eigenspace for a character?"
---

# Quick Definition

For a representation (V, r) of G and a character chi of G, the eigenspace V_chi is the largest subspace on which G acts through chi, i.e., V_chi = {v in V | rho(v) = v tensor a(chi)}. When V is a sum of eigenspaces, the sum is automatically direct.

# Core Definition

Let r: G -> GL(V) be a representation and chi: G -> G_m a character. G *acts on a subspace W through chi* if r(g)v = chi(g)v for all g in G(R), v in W_R. The *eigenspace* V_chi is the largest such subspace. In comodule terms, V_chi = {v in V | rho(v) = v tensor a(chi)} (Lemma 8.64). The direct sum decomposition theorem (8.65) states: if V = sum V_chi, then V = direct-sum V_chi. The proof uses the linear independence of group-like elements (Milne, pp. 116-117).

# Prerequisites

- **Character of affine group** -- Eigenspaces are indexed by characters
- **Linear representation** -- The ambient representation

# Key Properties

1. V_chi is the largest subspace on which G acts through chi
2. If V is a sum of eigenspaces, the sum is direct (Theorem 8.65)
3. For diagonalizable groups, V = direct-sum V_chi for all representations (Theorem 14.15)
4. The direct sum decomposition uses the linear independence of group-like elements in O(G)

# Context & Application

Eigenspace decompositions are fundamental to the representation theory of tori and reductive groups. For a split torus T, every representation decomposes as V = direct-sum V_chi, giving a grading by the character group X(T). The characters appearing with nonzero eigenspace are called the *weights* of the representation.

# Examples

**Example 1** (p. 168): For T = G_m x G_m, a representation V decomposes as V = direct-sum V_{(m_1,m_2)} where (t_1,t_2) in T(k) acts on V_{(m_1,m_2)} as multiplication by t_1^{m_1} t_2^{m_2}.

# Relationships

## Builds Upon
- **Character of affine group** -- Eigenspaces are indexed by characters

## Enables
- **Diagonalizable group** -- Characterized by all representations decomposing into eigenspaces
- **Split torus** -- Weight decomposition of representations

# Source Reference

Chapter I: Basic Theory of Affine Groups, Section 8p and 14d, pages 116-117, 167-169. Lemma 8.64, Theorem 8.65, Theorem 14.15.

# Verification Notes

- Definition source: Direct from Lemma 8.64 and surrounding text
- Confidence rationale: Explicit definition with full algebraic characterization
- Uncertainties: None
- Cross-reference status: Verified
