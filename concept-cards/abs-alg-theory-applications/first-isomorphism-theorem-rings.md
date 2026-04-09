---
# === CORE IDENTIFICATION ===
concept: First Isomorphism Theorem for Rings
slug: first-isomorphism-theorem-rings

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
pdf_page: 212
section: "16.3 Ring Homomorphisms and Ideals"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - ring-homomorphism
  - kernel-of-ring-homomorphism
  - factor-ring
extends: []
related:
  - second-isomorphism-theorem-rings
  - third-isomorphism-theorem-rings
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the First Isomorphism Theorem for rings?"
---

# Quick Definition

If $\psi : R \to S$ is a ring homomorphism, then $\ker\psi$ is an ideal of $R$ and $R/\ker\psi \cong \psi(R)$.

# Core Definition

"Let $\psi : R \to S$ be a ring homomorphism. Then $\ker\psi$ is an ideal of $R$. If $\phi : R \to R/\ker\psi$ is the canonical homomorphism, then there exists a unique isomorphism $\eta : R/\ker\psi \to \psi(R)$ such that $\psi = \eta\phi$" (Judson, Theorem 16.31, p. 212).

# Prerequisites

- **Ring homomorphism** — The theorem concerns ring homomorphisms
- **Kernel of ring homomorphism** — The kernel determines the quotient
- **Factor ring** — The quotient $R/\ker\psi$ appears in the conclusion

# Key Properties

1. $\ker\psi$ is an ideal of $R$
2. $R/\ker\psi \cong \psi(R)$ as rings
3. The isomorphism $\eta$ satisfies $\eta(r + \ker\psi) = \psi(r)$
4. $\psi = \eta \circ \phi$ where $\phi$ is the canonical map

# Construction / Recognition

## To Apply:
1. Identify a ring homomorphism $\psi : R \to S$
2. Compute $\ker\psi$
3. Conclude $R/\ker\psi \cong \psi(R)$

# Context & Application

The First Isomorphism Theorem is the most frequently used of the three isomorphism theorems. It allows one to identify quotient rings with images of homomorphisms. For example, it immediately gives $\mathbb{Z}/n\mathbb{Z} \cong \mathbb{Z}_n$.

# Examples

**Example 1** (p. 209): The map $\phi : \mathbb{Z} \to \mathbb{Z}_n$ with $\ker\phi = n\mathbb{Z}$ gives $\mathbb{Z}/n\mathbb{Z} \cong \mathbb{Z}_n$.

# Relationships

## Builds Upon
- **Ring homomorphism** — Input to the theorem
- **Kernel** — Determines the ideal for the quotient

## Related
- **Second Isomorphism Theorem for rings** — Related structural result
- **Third Isomorphism Theorem for rings** — Related structural result

# Common Errors

- **Error**: Applying the theorem without verifying the map is a ring homomorphism
  **Correction**: Must verify both addition and multiplication preservation

# Common Confusions

- **Confusion**: Confusing with the group version
  **Clarification**: The ring version requires that both ring operations are preserved

# Source Reference

Chapter 16: Rings, Section 16.3, Theorem 16.31, page 212.

# Verification Notes

- Definition source: Direct from Theorem 16.31
- Confidence: HIGH — explicit theorem
- Cross-reference status: Verified
- Uncertainties: None
