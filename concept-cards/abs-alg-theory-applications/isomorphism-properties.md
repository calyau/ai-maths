---
concept: Isomorphism Properties
slug: isomorphism-properties
category: morphisms
subcategory: null
tier: intermediate
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Isomorphisms"
chapter_number: 9
pdf_page: 129
section: "9.1 Definition and Examples"
extraction_confidence: high
aliases:
  - properties preserved by isomorphism
prerequisites:
  - group-isomorphism
extends: []
related:
  - cyclic-group-classification
contrasts_with: []
answers_questions:
  - "What properties are preserved by isomorphisms?"
  - "What invariants can distinguish non-isomorphic groups?"
---

# Quick Definition

An isomorphism $\phi : G \to H$ preserves all group-theoretic properties: the inverse map is an isomorphism, the groups have equal order, abelianness, cyclicity, and subgroup structure are all preserved.

# Core Definition

**Theorem 9.6** (Judson, p. 129): Let $\phi : G \to H$ be an isomorphism. Then:
1. $\phi^{-1} : H \to G$ is an isomorphism
2. $|G| = |H|$
3. If $G$ is abelian, then $H$ is abelian
4. If $G$ is cyclic, then $H$ is cyclic
5. If $G$ has a subgroup of order $n$, then $H$ has a subgroup of order $n$

# Prerequisites

- **Group Isomorphism** — These are properties of isomorphisms

# Key Properties

1. All five properties serve as isomorphism invariants
2. If any property differs, the groups are not isomorphic
3. Having the same invariants is necessary but not sufficient for isomorphism
4. These invariants provide practical tools for proving non-isomorphism

# Construction / Recognition

## To Prove Non-Isomorphism:
1. Check orders: if $|G| \neq |H|$, then $G \not\cong H$
2. Check abelianness: one abelian, one not implies $G \not\cong H$
3. Check element orders: different distributions of element orders implies $G \not\cong H$
4. Check cyclicity: one cyclic, one not implies $G \not\cong H$

# Context & Application

These properties give necessary conditions for isomorphism, enabling quick proofs that certain groups are not isomorphic without constructing explicit maps.

# Examples

**Example 1** (p. 128): $\mathbb{Z}_8 \not\cong \mathbb{Z}_{12}$ because $|\mathbb{Z}_8| = 8 \neq 12 = |\mathbb{Z}_{12}|$.

**Example 2** (p. 128): $S_3 \not\cong \mathbb{Z}_6$ even though both have 6 elements, because $\mathbb{Z}_6$ is abelian and $S_3$ is not.

# Relationships

## Builds Upon
- **Group Isomorphism** — These are properties of isomorphisms

## Enables
- **Cyclic Group Classification** — Cyclic groups are classified by these invariants

# Common Errors

- **Error**: Concluding $G \cong H$ because they share the same invariants
  **Correction**: Matching invariants is necessary but not sufficient; an explicit isomorphism is still needed

# Common Confusions

- **Confusion**: Thinking same element orders imply isomorphism
  **Clarification**: $\mathbb{Z}_2 \times \mathbb{Z}_2$ and $\mathbb{Z}_4$ both have 4 elements, but different element order distributions

# Source Reference

Chapter 9: Isomorphisms, Section 9.1, Theorem 9.6, page 129.

# Verification Notes

- Definition source: Direct from Theorem 9.6
- Confidence rationale: Explicit theorem
- Uncertainties: None
- Cross-reference status: Verified
