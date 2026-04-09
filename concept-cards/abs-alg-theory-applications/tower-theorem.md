---
# === CORE IDENTIFICATION ===
concept: Tower Theorem
slug: tower-theorem

# === CLASSIFICATION ===
category: field-theory
subcategory: field-extensions
tier: advanced

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Fields"
chapter_number: 21
pdf_page: 274
section: "21.1 Extension Fields"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "multiplicativity of degrees"
  - "degree formula"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - degree-of-field-extension
  - extension-field
extends: []
related:
  - dimension
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do degrees of field extensions multiply in a tower?"
---

# Quick Definition

If $E$ is a finite extension of $F$ and $K$ is a finite extension of $E$, then $K$ is a finite extension of $F$ and $[K:F] = [K:E][E:F]$.

# Core Definition

**Theorem 21.17.** If $E$ is a finite extension of $F$ and $K$ is a finite extension of $E$, then $K$ is a finite extension of $F$ and

$$[K:F] = [K:E][E:F]$$

(Judson, p. 279).

The proof constructs a basis $\{\alpha_i \beta_j\}$ for $K$ over $F$ from a basis $\{\alpha_1, \ldots, \alpha_n\}$ for $E$ over $F$ and a basis $\{\beta_1, \ldots, \beta_m\}$ for $K$ over $E$.

# Prerequisites

- **Degree of field extension** — The theorem relates degrees of extensions in a tower
- **Extension field** — Requires understanding of field extensions

# Key Properties

1. Generalizes to chains: $[F_k:F_1] = [F_k:F_{k-1}] \cdots [F_2:F_1]$ (Corollary 21.18)
2. Implies $[F(\alpha):F]$ divides $[E:F]$ when $\alpha \in E$ (Corollary 21.19)
3. Analogous to Lagrange's Theorem in group theory: $|G| = |G:H| \cdot |H|$

# Context & Application

The tower theorem is one of the most frequently used tools in field theory. It provides immediate divisibility constraints: if $[E:F] = n$, then the degree of any intermediate extension must divide $n$. This is the key to proving impossibility of geometric constructions.

# Examples

**Example 1** (p. 280): $[\mathbb{Q}(\sqrt{3}, \sqrt{5}):\mathbb{Q}] = [\mathbb{Q}(\sqrt{3}, \sqrt{5}):\mathbb{Q}(\sqrt{3})][\mathbb{Q}(\sqrt{3}):\mathbb{Q}] = 2 \cdot 2 = 4$.

**Example 2** (p. 280): $[\mathbb{Q}(\sqrt[3]{5}, \sqrt{5}i):\mathbb{Q}] = [\mathbb{Q}(\sqrt[3]{5}, \sqrt{5}i):\mathbb{Q}(\sqrt[3]{5})][\mathbb{Q}(\sqrt[3]{5}):\mathbb{Q}] = 2 \cdot 3 = 6$.

# Relationships

## Builds Upon
- **Degree of field extension** — The theorem relates multiple degrees

## Enables
- **Impossibility proofs** — Geometric constructions require $[F(\alpha):\mathbb{Q}] = 2^k$; if an intermediate degree is not a power of 2, the construction is impossible

# Source Reference

Chapter 21: Fields, Section 21.1, pages 279–280. See Corollaries 21.18, 21.19.

# Verification Notes

- Definition source: Direct from Theorem 21.17, p. 279
- Confidence: HIGH — explicit theorem statement with proof
- Cross-reference status: Verified
- Uncertainties: None
