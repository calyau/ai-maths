---
# === CORE IDENTIFICATION ===
concept: Content of a Polynomial
slug: content-of-polynomial

# === CLASSIFICATION ===
category: domain-theory
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Integral Domains"
chapter_number: 18
pdf_page: 247
section: "18.2 Factorization in Integral Domains"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - unique-factorization-domain
  - polynomial-ring
extends: []
related:
  - primitive-polynomial
  - gausss-lemma-ufd
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the content of a polynomial?"
---

# Quick Definition

The content of a polynomial $p(x) = a_nx^n + \cdots + a_0 \in D[x]$ over a UFD $D$ is the greatest common divisor of its coefficients $a_0, \ldots, a_n$.

# Core Definition

"Let $D$ be a unique factorization domain and suppose that $p(x) = a_nx^n + \cdots + a_1x + a_0$ in $D[x]$. Then the content of $p(x)$ is the greatest common divisor of $a_0, \ldots, a_n$" (Judson, p. 247).

# Prerequisites

- **UFD** — Content is defined over UFDs where GCDs exist
- **Polynomial ring** — Content is a property of polynomials

# Key Properties

1. Content is the GCD of all coefficients
2. $p(x)$ is primitive iff its content is $1$
3. Content of a product equals product of contents (Lemma 18.25)
4. Every polynomial $p(x)$ can be written as $c \cdot p_1(x)$ where $c$ is the content and $p_1(x)$ is primitive

# Construction / Recognition

## To Compute:
1. List all coefficients of $p(x)$
2. Compute their GCD

# Context & Application

Content separates a polynomial into its "scalar part" (content) and "polynomial part" (primitive polynomial). This decomposition is essential for Gauss's Lemma and for proving $D[x]$ is a UFD when $D$ is.

# Examples

**Example 1** (p. 247): $p(x) = 5x^4 - 3x^3 + x - 4 \in \mathbb{Z}[x]$ has content $1$ (primitive).

**Example 2** (p. 247): $q(x) = 4x^2 - 6x + 8 \in \mathbb{Z}[x]$ has content $2$.

# Relationships

## Enables
- **Primitive polynomial** — Content $= 1$
- **Gauss's Lemma (UFD version)** — Product of primitives is primitive

# Common Errors

- **Error**: Computing content using only some coefficients
  **Correction**: Must take the GCD of *all* coefficients, including zero terms

# Common Confusions

- **Confusion**: Confusing content with leading coefficient
  **Clarification**: Content is the GCD of all coefficients; leading coefficient is just the highest-degree term's coefficient

# Source Reference

Chapter 18: Integral Domains, Section 18.2, page 247.

# Verification Notes

- Definition source: Direct from p. 247
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
