---
# === CORE IDENTIFICATION ===
concept: Third Isomorphism Theorem
slug: third-isomorphism-theorem

# === CLASSIFICATION ===
category: morphisms
subcategory: isomorphism-theorems
tier: intermediate

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Homomorphisms"
chapter_number: 11
pdf_page: 150
section: "The Isomorphism Theorems"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "quotient of quotients theorem"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - normal-subgroup
  - factor-group
  - correspondence-theorem
extends:
  - first-isomorphism-theorem
related:
  - second-isomorphism-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Third Isomorphism Theorem?"
  - "How can quotients of quotients be simplified?"
---

# Quick Definition

The Third Isomorphism Theorem states that if $N$ and $H$ are normal subgroups of $G$ with $N \subset H$, then $G/H \cong (G/N)/(H/N)$. It allows "cancellation" of a common normal subgroup in nested quotients.

# Core Definition

**Theorem 11.14 (Third Isomorphism Theorem)**: "Let $G$ be a group and $N$ and $H$ be normal subgroups of $G$ with $N \subset H$. Then $G/H \cong \frac{G/N}{H/N}$" (Judson, p. 150).

# Prerequisites

- **Normal subgroup** — Both $N$ and $H$ must be normal in $G$
- **Factor group** — Multiple levels of quotients
- **Correspondence theorem** — Used in the proof

# Key Properties

1. Requires $N \subset H$ with both normal in $G$
2. $H/N$ is a normal subgroup of $G/N$ (by the Correspondence Theorem)
3. The quotient $(G/N)/(H/N)$ is isomorphic to $G/H$
4. Informally: "you can cancel the $N$'s"

# Context & Application

The Third Isomorphism Theorem simplifies computations involving nested quotients and is frequently used in proofs about group structure, including the Jordan-Holder Theorem.

# Examples

**Example 1** (p. 150): $\mathbb{Z}/m\mathbb{Z} \cong (\mathbb{Z}/mn\mathbb{Z})/(m\mathbb{Z}/mn\mathbb{Z})$. Since $|\mathbb{Z}/mn\mathbb{Z}| = mn$ and $|\mathbb{Z}/m\mathbb{Z}| = m$, we get $|m\mathbb{Z}/mn\mathbb{Z}| = n$.

# Relationships

## Builds Upon
- **Correspondence theorem** — $H/N$ is normal in $G/N$
- **First isomorphism theorem** — Underlying technique

## Related
- **Second isomorphism theorem** — Another structural theorem about quotients

# Common Errors

- **Error**: Applying the theorem when $N$ is not contained in $H$
  **Correction**: The theorem requires $N \subset H$; otherwise $H/N$ is not defined

# Source Reference

Chapter 11: Homomorphisms, Section 11.2, p. 150. Theorem 11.14.

# Verification Notes

- Definition source: Direct quote of Theorem 11.14
- Confidence: HIGH — explicitly stated theorem
- Cross-reference status: Verified
