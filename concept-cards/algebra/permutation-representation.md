---
concept: Permutation Representation
slug: permutation-representation
category: symmetry
subcategory: group-actions
tier: intermediate
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Symmetry"
chapter_number: 6
pdf_page: 162
section: "6.11 Permutation Representations"
extraction_confidence: high
aliases: []
prerequisites:
  - group-action
extends: []
related:
  - faithful-action
  - cayleys-theorem
contrasts_with: []
answers_questions:
  - "What is a permutation representation?"
  - "How do group actions correspond to homomorphisms into symmetric groups?"
---

# Quick Definition

A permutation representation of a group G is a homomorphism phi: G -> S_n (or G -> Perm(S)). There is a bijective correspondence between operations of G on a set S and permutation representations G -> Perm(S).

# Core Definition

A permutation representation of a group G is a homomorphism from the group to a symmetric group phi: G -> S_n (Artin, (6.11.1), p. 196). There is a bijective correspondence between operations of G on S = {1, ..., n} and permutation representations G -> S_n (Proposition 6.11.2): given an action, phi(g) = m_g (left multiplication by g).

# Prerequisites

- **Group action** — Permutation representations encode actions

# Key Properties

1. Bijective correspondence: actions <-> permutation representations
2. Faithful action <-> injective representation
3. The kernel of phi is the set of elements acting trivially on all of S
4. Rarely surjective (Perm(S) is usually much larger than G)

# Context & Application

Permutation representations translate the geometric/combinatorial concept of a group action into an algebraic homomorphism. They are used in Cayley's theorem, in the proofs of simplicity of alternating groups, and in the Sylow theorems.

# Examples

**Example 1** (p. 196): D_n acting on n vertices gives phi: D_n -> S_n.

**Example 2** (p. 197): GL_2(F_2) acts on the 3 nonzero vectors of F_2^2, giving an isomorphism GL_2(F_2) -> S_3.

# Relationships

## Builds Upon
- **Group action** — Every action yields a representation

## Enables
- **Cayley's theorem** — G -> S_n via left multiplication
- **Simplicity proofs** — Uses representations to study normal subgroups

# Source Reference

Chapter 6: Symmetry, Section 6.11, (6.11.1), Proposition 6.11.2, pages 196-197.

# Verification Notes

- Definition source: Direct from (6.11.1) and Proposition 6.11.2
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
