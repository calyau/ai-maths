---
# === CORE IDENTIFICATION ===
concept: Correspondence Theorem
slug: correspondence-theorem

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
pdf_page: 22
section: "Theorems concerning homomorphisms"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - third isomorphism theorem
  - lattice isomorphism theorem
  - fourth isomorphism theorem

# === TYPED RELATIONSHIPS ===
prerequisites:
  - quotient-group
  - normal-subgroup
  - epimorphism
extends: []
related:
  - factorization-theorem
  - isomorphism-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do subgroups of a quotient G/N relate to subgroups of G?"
  - "What is the correspondence theorem?"
---

# Quick Definition

For a surjective homomorphism $\alpha: G \twoheadrightarrow \bar{G}$ with kernel $N$, there is a bijection between subgroups of $G$ containing $N$ and subgroups of $\bar{G}$, preserving inclusion, index, and normality.

# Core Definition

"Let $\alpha: G \twoheadrightarrow \bar{G}$ be a surjective homomorphism, and let $N = \mathrm{Ker}(\alpha)$. Then there is a one-to-one correspondence $\{\text{subgroups of } G \text{ containing } N\} \leftrightarrow \{\text{subgroups of } \bar{G}\}$ under which $H \leftrightarrow \bar{H} = \alpha(H)$ and $\bar{H} \leftrightarrow H = \alpha^{-1}(\bar{H})$." (Milne, Theorem 1.47, p. 22)

# Prerequisites

- **Quotient group** — the correspondence involves quotients
- **Normal subgroup** — the kernel $N$ is the baseline
- **Epimorphism** — the homomorphism must be surjective

# Key Properties

Under the correspondence $H \leftrightarrow \bar{H}$:
1. $\bar{H} \subset \bar{H}' \iff H \subset H'$, and then $(\bar{H}' : \bar{H}) = (H' : H)$
2. $\bar{H} \trianglelefteq \bar{G} \iff H \trianglelefteq G$, and then $G/H \cong \bar{G}/\bar{H}$

Special case (Corollary 1.48): For the canonical map $G \to G/N$, subgroups of $G/N$ correspond to subgroups of $G$ containing $N$ via $H \leftrightarrow H/N$. If $H \trianglelefteq G$, then $G/H \cong (G/N)/(H/N)$.

# Context & Application

This theorem shows the lattice of subgroups of a quotient mirrors the part of the lattice of $G$ lying above the kernel. It is essential for inductive arguments in group theory.

# Examples

**Example 1** (p. 22): Let $G = D_4$ and $N = \langle r^2 \rangle$. The subgroup lattice of $G/N$ corresponds to the part of $D_4$'s lattice above $\langle r^2 \rangle$.

# Relationships

## Builds Upon
- **quotient-group**, **normal-subgroup**, **epimorphism**

## Enables
- Understanding the structure of quotient groups via the original group

## Related
- **factorization-theorem**, **isomorphism-theorem**

# Common Errors

- **Error**: Applying the correspondence to subgroups of $G$ that do not contain $N$
  **Correction**: The bijection only applies to subgroups containing $N$

# Source Reference

Chapter 1, Theorem 1.47, Corollary 1.48, Example 1.49, pages 22-23.

# Verification Notes

- Definition source: Direct from Theorem 1.47
- Confidence: HIGH — explicit theorem
- Uncertainties: None
