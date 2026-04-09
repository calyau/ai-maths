---
# === CORE IDENTIFICATION ===
concept: Associates in Integral Domains
slug: associates-in-integral-domains

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
pdf_page: 242
section: "18.2 Factorization in Integral Domains"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - integral-domain
  - unit-in-ring
extends: []
related:
  - irreducible-element
  - unique-factorization-domain
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are associates in an integral domain?"
  - "When are two elements considered the same up to units?"
---

# Quick Definition

Two elements $a$ and $b$ in an integral domain $D$ are associates if $a = ub$ for some unit $u \in D$. Associates generate the same principal ideal: $\langle a \rangle = \langle b \rangle$.

# Core Definition

"Two elements $a$ and $b$ in $R$ are said to be associates if there exists a unit $u$ in $R$ such that $a = ub$" (Judson, p. 242). Associates are equivalent from the perspective of divisibility: $a$ and $b$ are associates iff $\langle a \rangle = \langle b \rangle$ (Lemma 18.11).

# Prerequisites

- **Integral domain** — Associates are studied in integral domains
- **Unit in ring** — Associates differ by a unit factor

# Key Properties

1. $a$ and $b$ are associates iff $a = ub$ for some unit $u$
2. $a$ and $b$ are associates iff $\langle a \rangle = \langle b \rangle$ (Lemma 18.11)
3. Being associates is an equivalence relation
4. In $\mathbb{Z}$, $a$ and $b$ are associates iff $a = \pm b$

# Construction / Recognition

## To Verify:
1. Check if $a/b$ (or $b/a$) is a unit in $D$
2. Equivalently, check if $\langle a \rangle = \langle b \rangle$

# Context & Application

Associates play the role of "equal up to sign" in more general domains. In unique factorization, elements factor uniquely up to order and replacement by associates.

# Examples

**Example 1**: In $\mathbb{Z}$, $3$ and $-3$ are associates (unit $u = -1$).

**Example 2**: In $\mathbb{Z}[i]$, $1+i$ and $i(1+i) = i + i^2 = -1+i$ are associates.

# Relationships

## Enables
- **Unique factorization** — Factorizations are unique up to associates

## Related
- **Unit in ring** — Associates differ by a unit factor
- **Principal ideal** — Associates generate the same ideal

# Common Errors

- **Error**: Assuming associates must be equal
  **Correction**: Associates differ by a unit factor; in $\mathbb{Z}$, $5$ and $-5$ are associates but not equal

# Common Confusions

- **Confusion**: Confusing "associate" with "related"
  **Clarification**: "Associate" is a precise term: $a = ub$ for a unit $u$

# Source Reference

Chapter 18: Integral Domains, Section 18.2, page 242. See Lemma 18.11.

# Verification Notes

- Definition source: Direct from p. 242
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
