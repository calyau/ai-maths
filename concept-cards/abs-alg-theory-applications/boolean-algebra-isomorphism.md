---
# === CORE IDENTIFICATION ===
concept: Boolean Algebra Isomorphism
slug: boolean-algebra-isomorphism

# === CLASSIFICATION ===
category: lattice-theory
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Lattices and Boolean Algebras"
chapter_number: 19
pdf_page: 258
section: "19.2 Boolean Algebras"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - boolean-algebra
extends: []
related:
  - finite-boolean-algebra-classification
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an isomorphism of Boolean algebras?"
---

# Quick Definition

A Boolean algebra isomorphism is a bijective map $\phi : B \to C$ between Boolean algebras that preserves both join and meet: $\phi(a \vee b) = \phi(a) \vee \phi(b)$ and $\phi(a \wedge b) = \phi(a) \wedge \phi(b)$.

# Core Definition

"A bijective map $\phi : B \to C$ is an isomorphism of Boolean algebras if $\phi(a \vee b) = \phi(a) \vee \phi(b)$ and $\phi(a \wedge b) = \phi(a) \wedge \phi(b)$ for all $a$ and $b$ in $B$" (Judson, p. 258).

# Prerequisites

- **Boolean algebra** — Isomorphisms are between Boolean algebras

# Key Properties

1. Preserves join ($\vee$) and meet ($\wedge$)
2. Also preserves complement, $O$, and $I$ (automatically)
3. Two finite Boolean algebras are isomorphic iff they have the same number of atoms

# Construction / Recognition

## To Verify:
1. Check $\phi$ is bijective
2. Verify $\phi(a \vee b) = \phi(a) \vee \phi(b)$ for all $a, b$
3. Verify $\phi(a \wedge b) = \phi(a) \wedge \phi(b)$ for all $a, b$

# Context & Application

Boolean algebra isomorphisms establish when two Boolean algebras have identical structure. The classification theorem (Theorem 19.23) uses isomorphisms to show every finite Boolean algebra is isomorphic to a power set.

# Examples

**Example 1** (p. 259): The isomorphism $\phi : B \to \mathcal{P}(X)$ maps $a = a_1 \vee \cdots \vee a_n$ to $\{a_1, \ldots, a_n\}$.

# Relationships

## Related
- **Classification theorem** — Every finite Boolean algebra $\cong \mathcal{P}(X)$

# Common Errors

- **Error**: Assuming any bijection between Boolean algebras is an isomorphism
  **Correction**: The bijection must preserve both $\vee$ and $\wedge$

# Common Confusions

- **Confusion**: Confusing Boolean algebra isomorphism with ring isomorphism
  **Clarification**: They preserve different operations; a Boolean algebra can be given a ring structure, but the isomorphism notions differ

# Source Reference

Chapter 19: Lattices and Boolean Algebras, Section 19.2, page 258.

# Verification Notes

- Definition source: Direct from p. 258
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
