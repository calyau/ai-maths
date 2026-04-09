---
# === CORE IDENTIFICATION ===
concept: Gaussian Integers
slug: gaussian-integers

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
pdf_page: 208
section: "16.2 Integral Domains and Fields"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - integral-domain
extends: []
related:
  - euclidean-domain
  - unit-in-ring
contrasts_with:
  - field

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the Gaussian integers?"
  - "What are the units of the Gaussian integers?"
---

# Quick Definition

The Gaussian integers $\mathbb{Z}[i] = \{m + ni : m, n \in \mathbb{Z}\}$ form an integral domain that is a subring of the complex numbers, where $i^2 = -1$.

# Core Definition

"The set $\mathbb{Z}[i] = \{m + ni : m, n \in \mathbb{Z}\}$ forms a ring known as the Gaussian integers" (Judson, p. 208). The Gaussian integers are an integral domain with units $\pm 1$ and $\pm i$ (the elements with $a^2 + b^2 = 1$). The norm function $\nu(a + bi) = a^2 + b^2$ makes $\mathbb{Z}[i]$ a Euclidean domain (Example 18.20).

# Prerequisites

- **Integral domain** — The Gaussian integers are an integral domain

# Key Properties

1. Elements have the form $m + ni$ with $m, n \in \mathbb{Z}$
2. Units are $\pm 1$ and $\pm i$ (elements with $a^2 + b^2 = 1$)
3. The norm $\nu(a + bi) = a^2 + b^2$ is a Euclidean valuation
4. $\mathbb{Z}[i]$ is a Euclidean domain, hence a PID and UFD

# Construction / Recognition

## To Construct:
1. Take all complex numbers $a + bi$ where $a, b \in \mathbb{Z}$
2. Addition and multiplication are inherited from $\mathbb{C}$

# Context & Application

The Gaussian integers are a key example in algebraic number theory. They demonstrate that familiar integer properties (factorization, divisibility) extend to algebraic number rings, though sometimes with different factorizations (e.g., $5 = (2 + i)(2 - i)$).

# Examples

**Example 1** (p. 208): To find units, note $\alpha\beta = 1$ implies $(a^2 + b^2)(c^2 + d^2) = 1$, so $a^2 + b^2 = 1$, giving units $\pm 1, \pm i$.

**Example 2** (p. 246): $\mathbb{Z}[i]$ is a Euclidean domain with valuation $\nu(a + bi) = a^2 + b^2$.

# Relationships

## Builds Upon
- **Integral domain** — $\mathbb{Z}[i]$ is an integral domain

## Enables
- **Euclidean domain** — $\mathbb{Z}[i]$ with the norm is a key example

## Contrasts With
- **Field** — $\mathbb{Z}[i]$ is not a field ($2$ has no inverse in $\mathbb{Z}[i]$)

# Common Errors

- **Error**: Assuming all nonzero Gaussian integers have inverses in $\mathbb{Z}[i]$
  **Correction**: Only the units ($\pm 1, \pm i$) have inverses; $(2+i)^{-1} = \frac{2-i}{5} \notin \mathbb{Z}[i]$

# Common Confusions

- **Confusion**: Confusing the Gaussian integers with the Gaussian rationals $\mathbb{Q}(i)$
  **Clarification**: $\mathbb{Z}[i]$ restricts to integer coefficients; $\mathbb{Q}(i)$ is the field of fractions

# Source Reference

Chapter 16: Rings, Section 16.2, Example 16.12, page 208. See also Chapter 18, Example 18.20, page 246.

# Verification Notes

- Definition source: Direct from p. 208
- Confidence: HIGH — explicit definition and examples
- Cross-reference status: Verified
- Uncertainties: None
