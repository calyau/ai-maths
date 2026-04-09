---
# === CORE IDENTIFICATION ===
concept: Factorization Theorem (Homomorphism Theorem)
slug: factorization-theorem

# === CLASSIFICATION ===
category: homomorphisms
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Basic Definitions and Results"
chapter_number: 1
pdf_page: 21
section: "Theorems concerning homomorphisms"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - homomorphism theorem
  - first isomorphism theorem

# === TYPED RELATIONSHIPS ===
prerequisites:
  - kernel
  - quotient-group
  - image-of-homomorphism
  - canonical-homomorphism
extends: []
related:
  - isomorphism-theorem
  - correspondence-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does a homomorphism factor through its kernel?"
  - "What is the first isomorphism theorem?"
---

# Quick Definition

Every homomorphism $\alpha: G \to G'$ factors as a surjection, an isomorphism, and an injection: $G \twoheadrightarrow G/\mathrm{Ker}(\alpha) \xrightarrow{\sim} \mathrm{Im}(\alpha) \hookrightarrow G'$.

# Core Definition

"For any homomorphism $\alpha: G \to G'$ of groups, the kernel $N$ of $\alpha$ is a normal subgroup of $G$, the image $I$ of $\alpha$ is a subgroup of $G'$, and $\alpha$ factors in a natural way into the composite of a surjection, an isomorphism, and an injection:

$G \twoheadrightarrow G/N \xrightarrow{gN \mapsto \alpha(g)} I \hookrightarrow G'$."

(Milne, Theorem 1.45, p. 21)

# Prerequisites

- **Kernel** — the normal subgroup being quotiented
- **Quotient group** — $G/\mathrm{Ker}(\alpha)$ is the intermediate group
- **Image of a homomorphism** — the target of the isomorphism
- **Canonical homomorphism** — the surjection $G \twoheadrightarrow G/N$

# Key Properties

1. $\mathrm{Ker}(\alpha) \trianglelefteq G$ (already proven in 1.41)
2. $\mathrm{Im}(\alpha) \le G'$ (subgroup)
3. The induced map $\bar{\alpha}: G/N \to I$, $gN \mapsto \alpha(g)$, is an isomorphism
4. $\bar{\alpha}$ is surjective (by definition of $I$) and injective (if $\bar{\alpha}(gN) = e$ then $g \in \mathrm{Ker}(\alpha) = N$)

# Construction / Recognition

## The Factorization:
1. Compute $N = \mathrm{Ker}(\alpha)$
2. Form the quotient $G/N$
3. The map $\bar{\alpha}: gN \mapsto \alpha(g)$ is the isomorphism $G/N \xrightarrow{\sim} \mathrm{Im}(\alpha)$

# Context & Application

This is arguably the most important structural theorem in basic group theory. It says every homomorphism is "essentially" a quotient map followed by an inclusion. It is often called the First Isomorphism Theorem.

# Examples

**Example 1**: For $\det: \mathrm{GL}_n(F) \to F^{\times}$, the theorem gives $\mathrm{GL}_n(F)/\mathrm{SL}_n(F) \cong F^{\times}$.

**Example 2** (p. 21): The map $\mathbb{Z} \to \mathbb{Z}/m\mathbb{Z}$ gives $\mathbb{Z}/m\mathbb{Z} \cong C_m$.

# Relationships

## Builds Upon
- **kernel**, **quotient-group**, **image-of-homomorphism**, **canonical-homomorphism**

## Enables
- **isomorphism-theorem** — the second isomorphism theorem
- **correspondence-theorem** — the third isomorphism theorem

# Common Errors

- **Error**: Applying the theorem without verifying that $\alpha$ is a homomorphism
  **Correction**: The factorization only works for group homomorphisms

# Source Reference

Chapter 1, Theorem 1.45, page 21.

# Verification Notes

- Definition source: Direct from Theorem 1.45
- Confidence: HIGH — explicit theorem with proof
- Uncertainties: None
