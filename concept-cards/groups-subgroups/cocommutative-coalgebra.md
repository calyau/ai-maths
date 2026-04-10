---
# === CORE IDENTIFICATION ===
concept: Cocommutative Coalgebra
slug: cocommutative-coalgebra

# === CLASSIFICATION ===
category: hopf-algebras
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 49
section: "Affine groups and Hopf algebras"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - co-commutative

# === TYPED RELATIONSHIPS ===
prerequisites:
  - coalgebra
extends:
  - coalgebra
related:
  - hopf-algebra
  - cartier-duality
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a coalgebra?"
  - "What is a Hopf algebra?"
---

# Quick Definition

A coalgebra (or bialgebra) C is cocommutative if t composed with Delta = Delta, where t is the transposition map x tensor y -> y tensor x. An affine group is commutative if and only if its coordinate ring is cocommutative.

# Core Definition

A coalgebra or bialgebra C is said to be **cocommutative** if the diagram with Delta followed by the transposition map t: x tensor y -> y tensor x equals Delta, i.e., t composed with Delta = Delta (Section 5h, p. 49).

An affine monoid or group is commutative if and only if its coordinate ring is cocommutative (p. 50).

# Prerequisites

- **Coalgebra** — Cocommutativity is a property of coalgebras

# Key Properties

1. Cocommutativity is the dual notion to commutativity of algebras
2. G is a commutative group iff O(G) is cocommutative
3. A commutative cocommutative bialgebra that is finitely generated projective has a dual that is also commutative cocommutative (Section 5i)
4. The notion of "commutative bialgebra" is NOT self-dual, but cocommutativity is the dual property

# Relationships

## Extends
- **Coalgebra** — Cocommutative is an additional property on a coalgebra

## Related
- **Hopf algebra** — A commutative cocommutative Hopf algebra corresponds to a commutative affine group
- **Cartier duality** — Duality exchanges commutativity and cocommutativity

# Source Reference

Chapter I, Section 5h (p. 49-50).

# Verification Notes

- Definition source: Direct from Section 5h
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
