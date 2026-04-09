---
# === CORE IDENTIFICATION ===
concept: Epimorphism
slug: epimorphism

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
pdf_page: 21
section: "Theorems concerning homomorphisms"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases:
  - surjective homomorphism
  - surjection

# === TYPED RELATIONSHIPS ===
prerequisites:
  - homomorphism
extends:
  - homomorphism
related:
  - isomorphism
  - canonical-homomorphism
  - factorization-theorem
contrasts_with:
  - monomorphism

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a surjective homomorphism?"
  - "How does a surjective homomorphism relate to quotients?"
---

# Quick Definition

An epimorphism (surjective homomorphism) is a homomorphism $\alpha: G \to G'$ that is onto, meaning every element of $G'$ is in the image of $\alpha$.

# Core Definition

A surjective homomorphism $\alpha: G \twoheadrightarrow G'$ is one where $\alpha(G) = G'$. Milne uses the notation $\twoheadrightarrow$ for surjective homomorphisms, as in the correspondence theorem (1.47): "Let $\alpha: G \twoheadrightarrow \bar{G}$ be a surjective homomorphism." (Milne, p. 22)

# Prerequisites

- **Homomorphism** — An epimorphism is a homomorphism with surjectivity

# Key Properties

1. The canonical map $G \to G/N$ is always surjective
2. Every homomorphism factors as a surjection followed by an isomorphism followed by an injection (1.45)
3. Every group is a quotient of a free group (Corollary 2.5), hence a surjective image of a free group

# Construction / Recognition

## To Verify Surjectivity:
1. Show every element of $G'$ is in the image $\alpha(G)$
2. Alternatively, show $\alpha(G)$ contains a generating set for $G'$

# Context & Application

Surjective homomorphisms are central to the theory of quotient groups. The correspondence theorem (1.47) establishes a bijection between subgroups of $G$ containing $\mathrm{Ker}(\alpha)$ and subgroups of the image whenever $\alpha$ is surjective.

# Examples

**Example 1** (p. 20): The natural map $a \mapsto aN: G \to G/N$ is a surjective homomorphism with kernel $N$.

**Example 2** (p. 33): The extension of $X \to G$ to $FX \to G$ in Corollary 2.5 is surjective, showing every group is a quotient of a free group.

# Relationships

## Builds Upon
- **homomorphism** — an epimorphism is a surjective homomorphism

## Enables
- **correspondence-theorem** — requires a surjective homomorphism
- **quotient-group** — the canonical map is an epimorphism

## Contrasts With
- **monomorphism** — injective rather than surjective

# Common Errors

- **Error**: Assuming the preimage of a subgroup under a surjection is always normal
  **Correction**: The preimage of a subgroup is a subgroup, but normality of the preimage requires normality of the image subgroup

# Common Confusions

- **Confusion**: Thinking surjectivity is needed for the factorization theorem
  **Clarification**: The factorization theorem works for any homomorphism; surjectivity appears in the factored surjection $G \twoheadrightarrow G/N$

# Source Reference

Chapter 1, Theorem 1.45 (p. 21), Theorem 1.47 (p. 22).

# Verification Notes

- Definition source: Implicit in Milne's use of $\twoheadrightarrow$ notation
- Confidence: MEDIUM — term not explicitly defined, but concept used throughout
- Cross-reference status: Verified
- Uncertainties: None
