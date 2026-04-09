---
# === CORE IDENTIFICATION ===
concept: Ring Homomorphism
slug: ring-homomorphism

# === CLASSIFICATION ===
category: ring-theory
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Rings"
chapter_number: 16
pdf_page: 209
section: "16.3 Ring Homomorphisms and Ideals"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - ring
extends: []
related:
  - ring-isomorphism
  - kernel-of-ring-homomorphism
  - ideal
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a ring homomorphism?"
  - "How does a ring homomorphism differ from a group homomorphism?"
---

# Quick Definition

A ring homomorphism is a map between rings that preserves both addition and multiplication.

# Core Definition

"If $R$ and $S$ are rings, then a ring homomorphism is a map $\phi : R \to S$ satisfying $\phi(a + b) = \phi(a) + \phi(b)$ and $\phi(ab) = \phi(a)\phi(b)$ for all $a, b \in R$" (Judson, p. 209).

# Prerequisites

- **Ring** — Ring homomorphisms are maps between rings

# Key Properties

1. Preserves addition: $\phi(a + b) = \phi(a) + \phi(b)$
2. Preserves multiplication: $\phi(ab) = \phi(a)\phi(b)$
3. $\phi(0) = 0$ (Proposition 16.22)
4. If $\phi$ is onto and $R$ is commutative, then $\phi(R)$ is commutative (Proposition 16.22)
5. If $\phi$ is onto, then $\phi(1_R) = 1_S$ (Proposition 16.22)
6. If $R$ is a field and $\phi(R) \neq \{0\}$, then $\phi(R)$ is a field (Proposition 16.22)
7. The kernel of a ring homomorphism is an ideal (Proposition 16.27)

# Construction / Recognition

## To Verify:
1. Check that $\phi(a + b) = \phi(a) + \phi(b)$ for all $a, b$
2. Check that $\phi(ab) = \phi(a)\phi(b)$ for all $a, b$

# Context & Application

Ring homomorphisms are the structure-preserving maps of ring theory, analogous to group homomorphisms. They give rise to the isomorphism theorems for rings and connect to ideal theory through kernels.

# Examples

**Example 1** (p. 209): The map $\phi : \mathbb{Z} \to \mathbb{Z}_n$ defined by $a \mapsto a \pmod{n}$ is a ring homomorphism with kernel $n\mathbb{Z}$.

**Example 2** (p. 210): The evaluation map $\phi_\alpha : C[a,b] \to \mathbb{R}$ defined by $\phi_\alpha(f) = f(\alpha)$ is a ring homomorphism.

# Relationships

## Enables
- **Ring isomorphism** — A bijective ring homomorphism
- **Kernel of ring homomorphism** — The set mapped to zero; always an ideal
- **First Isomorphism Theorem for rings** — $R/\ker\phi \cong \phi(R)$

## Related
- **Ideal** — Kernels of ring homomorphisms are ideals, and conversely

# Common Errors

- **Error**: Forgetting to check both addition and multiplication preservation
  **Correction**: A ring homomorphism must preserve both operations; preserving just one is not enough

# Common Confusions

- **Confusion**: Assuming $\phi(1_R) = 1_S$ always holds
  **Clarification**: This is guaranteed only when $\phi$ is surjective (onto)

# Source Reference

Chapter 16: Rings, Section 16.3, pages 209-210. See Proposition 16.22.

# Verification Notes

- Definition source: Direct quote from p. 209
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
