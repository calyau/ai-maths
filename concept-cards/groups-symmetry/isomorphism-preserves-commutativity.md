---
# === CORE IDENTIFICATION ===
concept: Isomorphism Preserves Commutativity
slug: isomorphism-preserves-commutativity

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
extends: []
related:
  - isomorphic-groups
  - isomorphism-preserves-identity
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What properties are preserved by isomorphisms?"
  - "If G is abelian and G ≅ G', is G' abelian?"
---

# Quick Definition

If $G$ is abelian and $\varphi: G \to G'$ is an isomorphism, then $G'$ is also abelian.

# Core Definition

Armstrong proves: "If $G$ is abelian then so is $G'$" (p. 42). The proof: if $x', y' \in G'$ with $\varphi(x) = x'$, $\varphi(y) = y'$, then
$$x'y' = \varphi(x)\varphi(y) = \varphi(xy) = \varphi(yx) = \varphi(y)\varphi(x) = y'x',$$
where the middle step uses the fact that $G$ is abelian.

# Prerequisites

- **Isomorphism** — This is a property of isomorphisms

# Key Properties

1. If $G$ is abelian and $G \cong G'$, then $G'$ is abelian
2. Equivalently, if $G'$ is non-abelian and $G \cong G'$, then $G$ is non-abelian
3. This provides a quick test for non-isomorphism

# Construction / Recognition

## To Use for Non-Isomorphism:
1. Check whether one group is abelian and the other is not
2. If they differ in abelianness, they cannot be isomorphic

# Context & Application

This is one of the simplest and most frequently used criteria for showing groups are not isomorphic. Armstrong uses it on p. 42 to show that $\mathbb{Z}_{12}$ is not isomorphic to $D_6$ or $A_4$ (the first is abelian, the latter two are not).

# Examples

**Example** (p. 42): $\mathbb{Z}_{12}$ is abelian, while $D_6$ and $A_4$ are non-abelian. Therefore $\mathbb{Z}_{12}$ is not isomorphic to either $D_6$ or $A_4$.

# Relationships

## Builds Upon
- **Isomorphism** — Property of isomorphisms

## Related
- **Isomorphic groups** — Abelianness is a group-theoretic invariant

# Common Errors

- **Error**: Concluding that two non-abelian groups must be isomorphic.
  **Correction**: Both being non-abelian is necessary but not sufficient. $D_6$ and $A_4$ are both non-abelian but not isomorphic.

# Common Confusions

- **Confusion**: Thinking commutativity preservation means individual elements commute in the same way.
  **Clarification**: The result is about the global property of the group being abelian, not about which specific pairs of elements commute.

# Source Reference

Chapter 7: Isomorphisms, page 42 (pdf p. 42).

# Verification Notes

- Proof: Direct from p. 42
- Application: p. 42 example distinguishing three groups
- Confidence: HIGH — explicit proof
