---
# === CORE IDENTIFICATION ===
concept: Factor Ring
slug: factor-ring

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
pdf_page: 211
section: "16.3 Ring Homomorphisms and Ideals"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "quotient ring"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - ring
  - ideal
extends: []
related:
  - maximal-ideal
  - prime-ideal
  - first-isomorphism-theorem-rings
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a factor ring?"
  - "How do you construct a quotient ring?"
---

# Quick Definition

The factor ring (or quotient ring) $R/I$ is formed from a ring $R$ and an ideal $I$ by defining addition and multiplication on cosets: $(r + I)(s + I) = rs + I$.

# Core Definition

"Let $I$ be an ideal of $R$. The factor group $R/I$ is a ring with multiplication defined by $(r + I)(s + I) = rs + I$" (Judson, Theorem 16.29, p. 211). The ring $R/I$ is called the factor ring or quotient ring of $R$ by $I$.

# Prerequisites

- **Ring** — The parent structure
- **Ideal** — The ideal $I$ determines the cosets

# Key Properties

1. Elements are cosets $r + I$
2. Addition: $(r + I) + (s + I) = (r + s) + I$
3. Multiplication: $(r + I)(s + I) = rs + I$
4. Multiplication is well-defined because $I$ is an ideal
5. $R/I$ is a field iff $I$ is maximal (Theorem 16.35)
6. $R/I$ is an integral domain iff $I$ is prime (Proposition 16.38)

# Construction / Recognition

## To Construct:
1. Start with ring $R$ and ideal $I$
2. Form cosets $r + I = \{r + a : a \in I\}$
3. Define operations on cosets as above

# Context & Application

Factor rings are the ring-theoretic analog of factor groups. They provide a way to "collapse" a ring by an ideal, producing a simpler ring. The nature of the quotient (field, integral domain, etc.) depends on the type of ideal used.

# Examples

**Example 1** (p. 211): $\mathbb{Z}/n\mathbb{Z} \cong \mathbb{Z}_n$, the integers modulo $n$.

**Example 2** (p. 213): $\mathbb{Z}/p\mathbb{Z} \cong \mathbb{Z}_p$ is a field when $p$ is prime, because $p\mathbb{Z}$ is maximal.

# Relationships

## Builds Upon
- **Ideal** — The ideal determines the equivalence relation

## Enables
- **First Isomorphism Theorem for rings** — $R/\ker\phi \cong \phi(R)$

## Related
- **Maximal ideal** — $R/M$ is a field iff $M$ is maximal
- **Prime ideal** — $R/P$ is an integral domain iff $P$ is prime

# Common Errors

- **Error**: Trying to form $R/S$ where $S$ is a subring but not an ideal
  **Correction**: Multiplication on cosets is well-defined only when $I$ is an ideal

# Common Confusions

- **Confusion**: Confusing quotient rings with quotient groups
  **Clarification**: A quotient ring preserves both operations; the multiplicative structure requires the ideal property

# Source Reference

Chapter 16: Rings, Section 16.3, Theorem 16.29, pages 211-212.

# Verification Notes

- Definition source: Direct from Theorem 16.29, p. 211
- Confidence: HIGH — explicit theorem
- Cross-reference status: Verified
- Uncertainties: None
