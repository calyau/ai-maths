---
# === CORE IDENTIFICATION ===
concept: Isomorphism Preserves Order
slug: isomorphism-preserves-order

# === CLASSIFICATION ===
category: fundamentals
subcategory: isomorphism-properties
tier: intermediate

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Isomorphisms"
chapter_number: 7
pdf_page: 39
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - isomorphism
  - isomorphism-preserves-subgroups
extends: []
related:
  - isomorphic-groups
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What properties are preserved by isomorphisms?"
  - "Does an isomorphism preserve element order?"
---

# Quick Definition

An isomorphism preserves the order of every element: the order of $\varphi(g)$ in $G'$ equals the order of $g$ in $G$.

# Core Definition

Armstrong proves: "As $H$ and $\varphi(H)$ have the same number of elements, the order of $\varphi(g)$ must be the same as the order of $g$. Therefore, an isomorphism preserves the order of each element" (p. 42). The argument proceeds by noting that if $H = \langle g \rangle$ is cyclic, then $\varphi(H) = \langle \varphi(g) \rangle$ is also cyclic with the same number of elements.

# Prerequisites

- **Isomorphism** — This is a property of isomorphisms
- **Isomorphism preserves subgroups** — The proof uses the fact that cyclic subgroups map to cyclic subgroups

# Key Properties

1. If $g \in G$ has order $n$, then $\varphi(g) \in G'$ has order $n$
2. This applies to both finite and infinite order elements
3. This provides a tool for showing groups are not isomorphic: compare the multisets of element orders

# Construction / Recognition

## To Use for Non-Isomorphism:
1. List the orders of all elements in $G$ and $G'$
2. If the multisets of orders differ, the groups are not isomorphic

# Context & Application

Order preservation is one of the most practical tools for proving groups are not isomorphic. Armstrong uses it on p. 42 to distinguish $D_6$ from $A_4$: $D_6$ contains an element of order 6 while $A_4$ does not.

# Examples

**Example** (p. 42): $D_6 \not\cong A_4$ because $D_6$ has an element of order 6 but $A_4$ does not (the maximum element order in $A_4$ is 3).

# Relationships

## Builds Upon
- **Isomorphism preserves subgroups** — Cyclic subgroup $\langle g \rangle$ maps to $\langle \varphi(g) \rangle$

## Related
- **Isomorphic groups** — Order preservation is a necessary condition for isomorphism

# Common Errors

- **Error**: Concluding groups are isomorphic because they have the same set of element orders.
  **Correction**: Matching element orders is necessary but not sufficient for isomorphism.

# Common Confusions

- **Confusion**: Confusing order of a group with order of an element.
  **Clarification**: Isomorphisms preserve both, but this card is about element orders. Group order preservation follows from bijectivity.

# Source Reference

Chapter 7: Isomorphisms, page 42 (pdf p. 42).

# Verification Notes

- Proof: Direct from p. 42
- Application: $D_6 \not\cong A_4$ example on p. 42
- Confidence: HIGH — explicit statement and proof
