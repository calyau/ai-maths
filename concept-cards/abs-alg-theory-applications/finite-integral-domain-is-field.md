---
# === CORE IDENTIFICATION ===
concept: Finite Integral Domain is a Field
slug: finite-integral-domain-is-field

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
aliases:
  - "Wedderburn's theorem (finite case)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - integral-domain
  - field
extends: []
related:
  - cancellation-law-integral-domains
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When is an integral domain automatically a field?"
  - "Are all finite integral domains fields?"
---

# Quick Definition

Every finite integral domain is a field. That is, in a finite integral domain, every nonzero element has a multiplicative inverse.

# Core Definition

"Every finite integral domain is a field" (Judson, Theorem 16.16, p. 208). The proof uses the fact that for $a \neq 0$ in a finite integral domain $D$, the map $\lambda_a(d) = ad$ on $D^* = D \setminus \{0\}$ is injective (by cancellation), hence surjective (since $D^*$ is finite), so $ad = 1$ for some $d$.

# Prerequisites

- **Integral domain** — The result concerns integral domains
- **Field** — The conclusion is that the domain is a field

# Key Properties

1. Finiteness + no zero divisors $\Rightarrow$ every nonzero element is invertible
2. The proof uses a counting argument: injective maps on finite sets are surjective
3. This fails for infinite integral domains (e.g., $\mathbb{Z}$ is not a field)

# Construction / Recognition

## To Apply:
1. Verify the ring is an integral domain
2. Verify the ring is finite
3. Conclude every nonzero element has an inverse, so it is a field

# Context & Application

This theorem explains why $\mathbb{Z}_p$ is always a field for prime $p$, and more generally why all finite integral domains are fields. It is a key result connecting ring theory to finite field theory.

# Examples

**Example 1** (p. 209): $\mathbb{Z}_p$ for prime $p$ is a finite integral domain, hence a field.

**Example 2**: $\mathbb{Z}$ is an infinite integral domain that is not a field, showing finiteness is essential.

# Relationships

## Builds Upon
- **Integral domain** — The hypothesis
- **Cancellation law** — Used in the proof (injectivity of left multiplication)

## Enables
- **Finite field theory** — Foundation for studying fields of order $p^n$

# Common Errors

- **Error**: Applying this theorem to infinite integral domains
  **Correction**: $\mathbb{Z}$ shows the theorem fails without finiteness

# Common Confusions

- **Confusion**: Confusing this with "every integral domain is a field"
  **Clarification**: Only *finite* integral domains are automatically fields

# Source Reference

Chapter 16: Rings, Section 16.2, Theorem 16.16, page 208.

# Verification Notes

- Definition source: Direct from Theorem 16.16
- Confidence: HIGH — explicit theorem with proof
- Cross-reference status: Verified
- Uncertainties: None
