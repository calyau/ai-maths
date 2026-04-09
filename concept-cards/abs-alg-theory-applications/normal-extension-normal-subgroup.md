---
# === CORE IDENTIFICATION ===
concept: Normal Extensions and Normal Subgroups
slug: normal-extension-normal-subgroup

# === CLASSIFICATION ===
category: galois-theory
subcategory: field-automorphisms
tier: advanced

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Galois Theory"
chapter_number: 23
pdf_page: 307
section: "23.2 The Fundamental Theorem"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - fundamental-theorem-of-galois-theory
  - normal-extension
  - normal-subgroup
extends: []
related:
  - galois-correspondence
  - factor-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do normal field extensions relate to normal subgroups?"
---

# Quick Definition

In the Galois correspondence, an intermediate field $K$ is a normal extension of the base field $F$ if and only if $G(E/K)$ is a normal subgroup of $G(E/F)$. In this case, $G(K/F) \cong G(E/F)/G(E/K)$.

# Core Definition

Part (4) of the **Fundamental Theorem of Galois Theory** (Theorem 23.23): $K$ is a normal extension of $F$ if and only if $G(E/K)$ is a normal subgroup of $G(E/F)$. In this case,

$$G(K/F) \cong G(E/F)/G(E/K)$$

(Judson, p. 314).

# Prerequisites

- **Fundamental Theorem of Galois Theory** — This is part (4) of the theorem
- **Normal extension** — The field-theoretic condition
- **Normal subgroup** — The group-theoretic condition

# Key Properties

1. Normal extensions correspond to normal subgroups (and vice versa)
2. The Galois group of $K/F$ is the quotient $G(E/F)/G(E/K)$
3. The proof uses the fact that automorphisms of $K$ are restrictions of automorphisms of $E$
4. This connects normality in field theory to normality in group theory

# Context & Application

This correspondence is one of the most beautiful results in algebra. It shows that the same algebraic structure (normality) manifests in both field theory and group theory, connected through the Galois correspondence. It is essential for understanding solvability by radicals.

# Examples

**Example 1** (p. 314): In $G(\mathbb{Q}(\sqrt{3}, \sqrt{5})/\mathbb{Q}) \cong \mathbb{Z}_2 \times \mathbb{Z}_2$, all subgroups are normal, so all intermediate fields are normal extensions of $\mathbb{Q}$.

**Example 2** (p. 315): In the Galois group $D_4$ of $x^4 - 2$, the subgroup $\{\text{id}, \sigma^2\}$ is normal, corresponding to $\mathbb{Q}(\sqrt{2}, i)$ being a normal extension of $\mathbb{Q}$.

# Relationships

## Builds Upon
- **Fundamental Theorem of Galois Theory** — This is part of the theorem
- **Normal extension** — One side of the correspondence
- **Normal subgroup** — The other side

## Related
- **Factor group** — $G(K/F) \cong G(E/F)/G(E/K)$

# Source Reference

Chapter 23: Galois Theory, Section 23.2, pages 314–316. Theorem 23.23, part (4).

# Verification Notes

- Definition source: Direct from Theorem 23.23 part (4), p. 314
- Confidence: HIGH — explicit theorem statement with proof
- Cross-reference status: Verified
- Uncertainties: None
