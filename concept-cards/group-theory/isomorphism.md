---
# === CORE IDENTIFICATION ===
concept: Isomorphism
slug: isomorphism

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
  - group isomorphism
  - bijective homomorphism

# === TYPED RELATIONSHIPS ===
prerequisites:
  - homomorphism
extends:
  - homomorphism
related:
  - kernel
  - factorization-theorem
contrasts_with:
  - monomorphism
  - epimorphism

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a group isomorphism?"
  - "When are two groups considered the same?"
---

# Quick Definition

An isomorphism is a bijective homomorphism. Two groups are isomorphic if there exists an isomorphism between them.

# Core Definition

"An *isomorphism* is a bijective homomorphism." (Milne, Definition 1.20, p. 16)

Milne uses $\approx$ for isomorphic and $\simeq$ for canonically isomorphic.

# Prerequisites

- **Homomorphism** — An isomorphism is a homomorphism with additional bijectivity

# Key Properties

1. If $\alpha: G \to G'$ is an isomorphism, then $\alpha^{-1}: G' \to G$ is also an isomorphism
2. Isomorphic groups have identical group-theoretic properties
3. A homomorphism is injective if and only if $\mathrm{Ker}(\alpha) = \{e\}$ (p. 20)
4. The factorization theorem (1.45) shows every homomorphism induces an isomorphism $G/\mathrm{Ker}(\alpha) \cong \mathrm{Im}(\alpha)$

# Construction / Recognition

## To Show Two Groups are Isomorphic:
1. Construct a homomorphism between them
2. Show it is bijective (injective + surjective)
3. Alternatively, show kernel is trivial and map is surjective

# Context & Application

Isomorphisms identify groups that are "the same" algebraically. Classification results (e.g., groups of small order) are always stated up to isomorphism.

# Examples

**Example 1** (p. 7): Two groups $(G, *)$ and $(G', *')$ are isomorphic if there exists a bijection $a \leftrightarrow a'$ such that $(a * b)' = a' *' b'$.

**Example 2** (p. 12): $C_n \approx \mathbb{Z}/n\mathbb{Z}$ for any cyclic group of order $n$.

# Relationships

## Builds Upon
- **homomorphism** — an isomorphism is a bijective homomorphism

## Enables
- **factorization-theorem** — produces canonical isomorphisms
- **isomorphism-theorem** — relates quotients via isomorphisms

## Contrasts With
- **monomorphism** — injective but not necessarily surjective
- **epimorphism** — surjective but not necessarily injective

# Common Errors

- **Error**: Assuming any bijection between groups is an isomorphism
  **Correction**: The map must also preserve the group operation

# Common Confusions

- **Confusion**: Confusing $\approx$ and $\simeq$ in Milne's notation
  **Clarification**: Milne uses $\approx$ for "isomorphic" and $\simeq$ for "canonically isomorphic" (a specific, natural isomorphism)

# Source Reference

Chapter 1, Definition 1.20, page 16.

# Verification Notes

- Definition source: Direct quote from Definition 1.20
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
