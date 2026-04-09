---
# === CORE IDENTIFICATION ===
concept: Canonical Homomorphism
slug: canonical-homomorphism

# === CLASSIFICATION ===
category: morphisms
subcategory: group-maps
tier: intermediate

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Homomorphisms"
chapter_number: 11
pdf_page: 148
section: "The Isomorphism Theorems"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "natural homomorphism"
  - "quotient map"
  - "projection homomorphism"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - normal-subgroup
  - factor-group
  - group-homomorphism
extends:
  - group-homomorphism
related:
  - first-isomorphism-theorem
  - kernel-of-homomorphism
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the canonical homomorphism?"
  - "How does every normal subgroup give rise to a homomorphism?"
---

# Quick Definition

The canonical (or natural) homomorphism is the map $\phi: G \to G/H$ defined by $\phi(g) = gH$, where $H$ is a normal subgroup of $G$. Its kernel is $H$.

# Core Definition

"Let $H$ be a normal subgroup of $G$. Define the **natural** or **canonical homomorphism** $\phi: G \to G/H$ by $\phi(g) = gH$" (Judson, p. 148). This is indeed a homomorphism since $\phi(g_1 g_2) = g_1 g_2 H = g_1 H g_2 H = \phi(g_1)\phi(g_2)$. The kernel of this homomorphism is $H$.

# Prerequisites

- **Normal subgroup** — $H$ must be normal for $G/H$ to be a group
- **Factor group** — The codomain of the canonical homomorphism
- **Group homomorphism** — The canonical map is a specific homomorphism

# Key Properties

1. $\phi$ is always surjective (onto)
2. $\ker\phi = H$
3. $\phi$ is a homomorphism since $\phi(g_1 g_2) = g_1 g_2 H = g_1 H g_2 H$
4. Every normal subgroup arises as the kernel of the canonical homomorphism
5. The canonical homomorphism mediates the First Isomorphism Theorem

# Context & Application

The canonical homomorphism establishes the precise correspondence between normal subgroups and homomorphisms: every normal subgroup $N$ of $G$ is the kernel of the canonical homomorphism $G \to G/N$, and conversely, the kernel of any homomorphism is a normal subgroup.

# Examples

**Example 1** (p. 148): $\phi: \mathbb{Z} \to \mathbb{Z}/n\mathbb{Z}$ defined by $\phi(k) = k + n\mathbb{Z}$ is the canonical homomorphism with kernel $n\mathbb{Z}$.

# Relationships

## Builds Upon
- **Normal subgroup** — Defines the kernel
- **Factor group** — The codomain

## Enables
- **First isomorphism theorem** — Uses the canonical homomorphism in its commutative diagram

## Related
- **Kernel of homomorphism** — The kernel of the canonical map is $H$

# Common Confusions

- **Confusion**: Thinking the canonical homomorphism requires choosing coset representatives
  **Clarification**: The map $g \mapsto gH$ is well-defined regardless of how we think about the cosets

# Source Reference

Chapter 11: Homomorphisms, Section 11.2, p. 148.

# Verification Notes

- Definition source: Direct quote from p. 148
- Confidence: HIGH — explicitly defined
- Cross-reference status: Verified
