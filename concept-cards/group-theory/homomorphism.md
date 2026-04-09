---
# === CORE IDENTIFICATION ===
concept: Homomorphism
slug: homomorphism

# === CLASSIFICATION ===
category: homomorphisms
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Basic Definitions and Results"
chapter_number: 1
pdf_page: 16
section: "Homomorphisms"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - group homomorphism
  - morphism of groups

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
extends: []
related:
  - isomorphism
  - kernel
  - image-of-homomorphism
contrasts_with:
  - isomorphism

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a homomorphism of groups?"
  - "How does a homomorphism preserve group structure?"
---

# Quick Definition

A homomorphism from a group $G$ to a group $G'$ is a map $\alpha: G \to G'$ that preserves the group operation: $\alpha(ab) = \alpha(a)\alpha(b)$ for all $a, b \in G$.

# Core Definition

"A *homomorphism* from a group $G$ to a second $G'$ is a map $\alpha: G \to G'$ such that $\alpha(ab) = \alpha(a)\alpha(b)$ for all $a, b \in G$." (Milne, Definition 1.20, p. 16)

# Prerequisites

- **Group** — A homomorphism is a structure-preserving map between groups

# Key Properties

1. Homomorphisms preserve all finite products: $\alpha(a_1 \cdots a_m) = \alpha(a_1) \cdots \alpha(a_m)$ (1.21)
2. $\alpha(e) = e$ (the identity maps to the identity)
3. $\alpha(a^{-1}) = \alpha(a)^{-1}$ (inverses map to inverses)
4. $\alpha(a^m) = \alpha(a)^m$ for all $m \in \mathbb{Z}$
5. A homomorphism of commutative groups is also a homomorphism of $\mathbb{Z}$-modules

# Construction / Recognition

## To Verify a Map is a Homomorphism:
1. Confirm domain and codomain are groups
2. Show $\alpha(ab) = \alpha(a)\alpha(b)$ for all $a, b$
3. The identity and inverse conditions follow automatically

# Context & Application

Homomorphisms are the fundamental structure-preserving maps in group theory. They allow comparison between groups and lead to the key notions of kernel, image, quotient, and the isomorphism theorems.

# Examples

**Example 1** (p. 16): The determinant map $\det: \mathrm{GL}_n(F) \to F^{\times}$ is a homomorphism.

**Example 2** (p. 16): Cayley's Theorem (1.22) provides an injective homomorphism $G \to \mathrm{Sym}(G)$ via left multiplication $a \mapsto a_L$.

# Relationships

## Builds Upon
- **group** — homomorphisms are maps between groups

## Enables
- **kernel** — defined as preimage of identity under a homomorphism
- **image-of-homomorphism** — the range of a homomorphism
- **quotient-group** — arises from kernels of homomorphisms
- **factorization-theorem** — every homomorphism factors through its kernel

## Related
- **isomorphism** — a bijective homomorphism

# Common Errors

- **Error**: Assuming $\alpha(e_G) = e_{G'}$ must be checked separately
  **Correction**: This follows automatically from $\alpha(e) = \alpha(ee) = \alpha(e)\alpha(e)$

# Common Confusions

- **Confusion**: Thinking a homomorphism must be injective or surjective
  **Clarification**: A homomorphism can be neither; injectivity and surjectivity are additional properties

# Source Reference

Chapter 1, Definition 1.20, page 16; properties in 1.21, page 16.

# Verification Notes

- Definition source: Direct quote from Definition 1.20
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified with 1.21 properties
- Uncertainties: None
