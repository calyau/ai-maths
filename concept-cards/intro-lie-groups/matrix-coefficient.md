---
# === CORE IDENTIFICATION ===
concept: Matrix Coefficient
slug: matrix-coefficient

# === CLASSIFICATION ===
category: representations
subcategory: characters
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Representations of Lie Groups and Lie Algebras"
chapter_number: 4
pdf_page: 47
section: "4.7 Orthogonality of characters and Peter-Weyl theorem"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "matrix element"
  - "representative function"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - representation-of-lie-group
  - haar-measure
extends: []
related:
  - character-of-representation
  - orthogonality-of-matrix-coefficients
  - peter-weyl-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a matrix coefficient of a representation?"
---

# Quick Definition

A matrix coefficient of a representation $V$ is a function on $G$ of the form $\rho_{ij}(g) = \langle v_i^*, \rho(g) v_j \rangle$, obtained by writing the operator $\rho(g)$ in a chosen basis.

# Core Definition

(Kirillov, p. 47): Let $v_i$ be a basis in a representation $V$. Writing the operator $\rho(g): V \to V$ in the basis $v_i$, we get a matrix-valued function on $G$. Each entry $\rho_{ij}(g)$ as a scalar-valued function on $G$ is called a matrix coefficient.

More invariantly, for $v \in V$ and $v^* \in V^*$, the function $\rho_{v^*, v}(g) = \langle v^*, \rho(g)v \rangle$ is a matrix coefficient. This gives a map $m: V^* \otimes V \to C^\infty(G, \mathbb{C})$.

# Prerequisites

- **Representation of a Lie group** — Matrix coefficients come from representations
- **Haar measure** — Needed for inner products between matrix coefficients

# Key Properties

1. Matrix coefficients of a representation form a finite-dimensional subspace of $C^\infty(G)$
2. They satisfy orthogonality relations (Theorem 4.39)
3. Characters are traces of matrix coefficients: $\chi_V(g) = \sum_i \rho_{ii}(g)$
4. The map $m: V^* \otimes V \to C^\infty(G)$ is injective (Corollary 4.46)
5. The map $m$ is a morphism of $G$-bimodules (Theorem 4.45)

# Context & Application

Matrix coefficients provide concrete functions on the group that encode representation-theoretic information. The Peter-Weyl theorem says they span a dense subspace of $L^2(G)$. For $G = S^1$, matrix coefficients are the exponentials $e^{2\pi ikx}$, and Peter-Weyl reduces to Fourier analysis.

# Examples

**Example 4.49** (p. 50): For $G = S^1$, irreducible representations are $V_k$ with $\rho(a) = e^{2\pi ika}$. The matrix coefficient equals the character: $\chi_k(a) = e^{2\pi ika}$.

# Relationships

## Enables
- **Character of representation** — Characters are sums of diagonal matrix coefficients
- **Peter-Weyl theorem** — Matrix coefficients span $L^2(G)$

## Related
- **Orthogonality of matrix coefficients** — Key structural result

# Source Reference

Chapter 4, Section 4.7, pp. 47-50.

# Verification Notes

- Definition source: Direct from text, p. 47
- Confidence rationale: Clear definition with basis-free reformulation
- Uncertainties: None
- Cross-reference status: Verified
