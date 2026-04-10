---
concept: Fixed Vectors in a Representation
slug: fixed-vectors
category: representations
subcategory: null
tier: intermediate
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 103
section: "8f Representations and comodules"
extraction_confidence: high
aliases:
  - G-invariants
  - V^G
prerequisites:
  - linear-representation
  - comodule
extends: []
related:
  - stabilizer-subgroup
  - unipotent-group
contrasts_with: []
answers_questions:
  - "What are the fixed vectors of a representation?"
---

# Quick Definition

For a representation r: G -> GL_V, the space of fixed vectors V^G consists of all v in V such that gv = v for all g in G(R) and all k-algebras R. In comodule terms, V^G = {v in V | rho(v) = v tensor 1}. It is the largest trivial subrepresentation.

# Core Definition

For a representation r: G -> GL_V, define V^G = {v in V | gv = v (in V_R) for all k-algebras R and all g in G(R)} (Definition 8.56). If rho denotes the coaction, then V^G = {v in V | rho(v) = v tensor 1}. For a subgroup H with O(H) = O(G)/a, a vector v is fixed by H iff rho(v) = v tensor 1 mod V tensor a (Corollary 8.20). The space V^H is stable under G if H is normal in G (Lemma 8.67, Milne, pp. 103-104, 112).

# Prerequisites

- **Linear representation** -- Fixed vectors are defined for representations
- **Comodule** -- Comodule reformulation

# Key Properties

1. V^G = {v | rho(v) = v tensor 1}
2. V^H tensor R = {v in V(R) | rho(v) = v tensor 1 mod V tensor a tensor R} (Lemma 8.21)
3. V^N is stable under G when N is normal (Lemma 8.67)
4. G is unipotent iff V^G != 0 for every nonzero V

# Context & Application

Fixed vectors are the bridge between representation theory and the unipotent/solvable structure theory. The condition "every representation has a fixed vector" characterizes unipotent groups.

# Examples

**Example 1** (p. 112): For the natural representation of GL_n on k^n, V^{GL_n} = 0.

**Example 2**: For the trivial representation of any G on V, V^G = V.

# Relationships

## Builds Upon
- **Linear representation** -- Fixed vectors are defined within representations

## Enables
- **Unipotent group** -- Characterized by V^G != 0 for all nonzero V
- **Stabilizer subgroup** -- G_v is the subgroup fixing a vector

# Source Reference

Chapter I: Basic Theory of Affine Groups, Sections 8f and 8l, pages 103-104, 112. Definition 8.56, Corollary 8.20, Lemma 8.67.

# Verification Notes

- Definition source: Direct from Definition 8.56
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
