---
# === CORE IDENTIFICATION ===
concept: Campbell-Hausdorff Formula
slug: campbell-hausdorff-formula

# === CLASSIFICATION ===
category: lie-algebras
subcategory: exponential-map
tier: advanced

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Lie Groups and Lie Algebras"
chapter_number: 3
pdf_page: 29
section: "3.7"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Baker-Campbell-Hausdorff formula"
  - "BCH formula"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - exponential-map
  - commutator-bracket
  - lie-algebra
extends:
  - commutator-bracket
related:
  - commuting-elements-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I use the exponential map to go between Lie group and Lie algebra?"
  - "How does a Lie algebra relate to its Lie group?"
---

# Quick Definition

The Campbell-Hausdorff formula expresses $\exp(x)\exp(y) = \exp(\mu(x,y))$ where $\mu(x,y) = x + y + \frac{1}{2}[x,y] + \frac{1}{12}([x,[x,y]] + [y,[y,x]]) + \cdots$ is a universal series of iterated Lie brackets.

# Core Definition

**Theorem 3.34** (Kirillov): For small enough $x, y \in \mathfrak{g}$, $\exp(x)\exp(y) = \exp(\mu(x,y))$ where $\mu(x,y) = x + y + \sum_{n \geq 2} \mu_n(x,y)$ and each $\mu_n(x,y)$ is a Lie polynomial in $x, y$ of degree $n$ (an expression of iterated commutators). This expression is universal: it does not depend on $\mathfrak{g}$ or the choice of $x, y$.

First several terms (equation 3.15): $\mu(x,y) = x + y + \frac{1}{2}[x,y] + \frac{1}{12}([x,[x,y]] + [y,[y,x]]) + \cdots$

# Prerequisites

- **Exponential map** — the group law in logarithmic coordinates
- **Commutator bracket** — the brackets appearing in the formula
- **Lie algebra** — the setting for the formula

# Key Properties

1. The formula is universal — independent of the specific Lie algebra.
2. Each term $\mu_n$ is a Lie polynomial (only uses brackets, no products).
3. The group law is entirely determined by the Lie bracket (Corollary 3.35).
4. Special case: if $[x, y] = 0$, then $\mu(x, y) = x + y$ (Theorem 3.33).

# Construction / Recognition

## To Construct/Create:
1. Write a differential equation for $Z(t) = \mu(tx, y)$.
2. Solve by power series; the right-hand side involves $\sum a_n t^n (\mathrm{ad}\, x)^n y$.

## To Identify/Recognize:
1. Any expression for $\log(\exp(x)\exp(y))$ in terms of iterated brackets of $x$ and $y$.

# Context & Application

The BCH formula is the key result showing that the Lie algebra determines the group law. It justifies the study of Lie algebras as a substitute for Lie groups: the entire group structure (for connected groups) is encoded in the bracket.

# Examples

**Example** (Theorem 3.33, p. 29): If $[x, y] = 0$, then $\exp(x)\exp(y) = \exp(x + y) = \exp(y)\exp(x)$.

**Example** (Corollary 3.35, p. 29): The group operation in any connected Lie group can be recovered from the commutator in $\mathfrak{g}$.

# Relationships

## Builds Upon
- **Commutator bracket** — the brackets in the formula
- **Exponential map** — $\mu$ describes the group law via exp

## Enables
- **Group law recovery** — the group law is determined by the bracket (Corollary 3.35)
- **Proof of Theorem 3.43** — can be used as alternative to Frobenius theorem

## Related
- **Commuting elements theorem** — $[x,y]=0 \Rightarrow \exp(x)\exp(y) = \exp(x+y)$

# Common Errors

- **Error**: Trying to use $\exp(x)\exp(y) = \exp(x+y)$ when $[x,y] \neq 0$.
  **Correction**: The correction terms are $\frac{1}{2}[x,y] + \frac{1}{12}([x,[x,y]] + [y,[y,x]]) + \cdots$.

# Common Confusions

- **Confusion**: Whether the BCH formula determines the group completely.
  **Clarification**: Locally yes (near the identity). But it does not by itself determine the global topology of $G$ (Remark after Corollary 3.35).

# Source Reference

Chapter 3: Lie Groups and Lie Algebras, Section 3.7, Theorem 3.33, Theorem 3.34, Corollary 3.35, pages 29-30.

# Verification Notes

- Definition source: Direct from Theorem 3.34
- Confidence rationale: Explicit theorem; proof referenced to external source
- Uncertainties: Full proof not given in text
- Cross-reference status: Verified with Theorem 3.33, Corollary 3.35
