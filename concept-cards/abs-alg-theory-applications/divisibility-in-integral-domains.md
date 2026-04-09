---
# === CORE IDENTIFICATION ===
concept: Divisibility in Integral Domains
slug: divisibility-in-integral-domains

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
extends: []
related:
  - associates-in-integral-domains
  - principal-ideal
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What does divisibility mean in an integral domain?"
  - "How does divisibility relate to ideals?"
---

# Quick Definition

In a commutative ring $R$ with identity, $a$ divides $b$ (written $a | b$) if there exists $c \in R$ such that $b = ac$. Divisibility is intimately connected to ideal containment.

# Core Definition

"Let $R$ be a commutative ring with identity, and let $a$ and $b$ be elements in $R$. We say that $a$ divides $b$, and write $a | b$, if there exists an element $c \in R$ such that $b = ac$" (Judson, p. 242). The key connection: $a | b$ iff $\langle b \rangle \subset \langle a \rangle$ (Lemma 18.11).

# Prerequisites

- **Integral domain** — Divisibility is studied in integral domains

# Key Properties

1. $a | b$ iff $b = ac$ for some $c \in R$
2. $a | b$ iff $\langle b \rangle \subset \langle a \rangle$ (Lemma 18.11)
3. $a$ and $b$ are associates iff $\langle a \rangle = \langle b \rangle$ (Lemma 18.11)
4. $a$ is a unit iff $\langle a \rangle = D$ (Lemma 18.11)
5. Divisibility is reflexive and transitive

# Construction / Recognition

## To Verify $a | b$:
1. Check if $b/a$ exists in $R$ (i.e., find $c$ with $b = ac$)
2. Or check if $b \in \langle a \rangle$

# Context & Application

Divisibility theory in integral domains generalizes the divisibility of integers. The connection between divisibility and ideal containment (Lemma 18.11) is one of the most important bridges between element-wise and ideal-theoretic reasoning.

# Examples

**Example 1**: In $\mathbb{Z}$, $3 | 12$ since $12 = 3 \cdot 4$, and $\langle 12 \rangle = 12\mathbb{Z} \subset 3\mathbb{Z} = \langle 3 \rangle$.

**Example 2**: In $\mathbb{Z}[i]$, $(1+i) | 2$ since $2 = (1+i)(1-i)$.

# Relationships

## Enables
- **Associates** — $a$ and $b$ are associates iff each divides the other
- **Irreducible/prime elements** — Defined via divisibility

## Related
- **Principal ideal** — $a | b \Leftrightarrow \langle b \rangle \subset \langle a \rangle$

# Common Errors

- **Error**: Assuming $a | b$ and $b | a$ implies $a = b$
  **Correction**: It implies $a$ and $b$ are associates (differ by a unit)

# Common Confusions

- **Confusion**: Confusing the direction of ideal containment with divisibility
  **Clarification**: $a | b$ means $\langle b \rangle \subset \langle a \rangle$ (bigger divisor = smaller ideal)

# Source Reference

Chapter 18: Integral Domains, Section 18.2, page 242. See Lemma 18.11.

# Verification Notes

- Definition source: Direct from p. 242
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
