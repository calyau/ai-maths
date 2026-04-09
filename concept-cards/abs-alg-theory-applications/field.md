---
# === CORE IDENTIFICATION ===
concept: Field
slug: field

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
pdf_page: 205
section: "16.2 Integral Domains and Fields"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - commutative-ring
  - division-ring
extends:
  - integral-domain
  - division-ring
related:
  - maximal-ideal
  - characteristic-of-ring
contrasts_with:
  - integral-domain
  - ring

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a field?"
  - "What distinguishes a ring from a field?"
  - "What distinguishes an integral domain from a field?"
  - "How do maximal ideals relate to fields?"
---

# Quick Definition

A field is a commutative division ring: a commutative ring with identity in which every nonzero element has a multiplicative inverse.

# Core Definition

"A commutative division ring is called a field" (Judson, p. 205). Equivalently, a field is a commutative ring $F$ with identity $1 \neq 0$ such that for every nonzero $a \in F$, there exists $a^{-1} \in F$ with $aa^{-1} = 1$. The relationship $R/M$ is a field if and only if $M$ is a maximal ideal (Theorem 16.35).

# Prerequisites

- **Commutative ring** — A field has commutative multiplication
- **Division ring** — Every nonzero element must have a multiplicative inverse

# Key Properties

1. $(F, +)$ is an abelian group
2. $(F \setminus \{0\}, \cdot)$ is an abelian group
3. Every field is an integral domain
4. A field has exactly two ideals: $\{0\}$ and $F$ itself
5. Characteristic is $0$ or prime (Theorem 16.19)
6. $R/M$ is a field iff $M$ is a maximal ideal (Theorem 16.35)

# Construction / Recognition

## To Verify:
1. Confirm $F$ is a commutative ring with identity $1 \neq 0$
2. Show every nonzero element has a multiplicative inverse

## To Recognize:
1. $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$ are fields
2. $\mathbb{Z}_p$ for prime $p$ is a field
3. $\mathbb{Z}_n$ for composite $n$ is not a field

# Context & Application

Fields are the most well-behaved ring structures. They are the setting for linear algebra (vector spaces over fields) and polynomial theory (the division algorithm requires a field of coefficients). The classification of fields is a central topic in Galois theory.

# Examples

**Example 1** (p. 205): $\mathbb{Q}$, $\mathbb{R}$, and $\mathbb{C}$ are all fields under ordinary addition and multiplication.

**Example 2** (p. 209): $\mathbb{Z}_p$ is a field for every prime $p$, with characteristic $p$.

**Example 3** (p. 208): $\mathbb{Q}(\sqrt{2}) = \{a + b\sqrt{2} : a, b \in \mathbb{Q}\}$ is a field, with inverse $(a + b\sqrt{2})^{-1} = \frac{a}{a^2 - 2b^2} - \frac{b}{a^2 - 2b^2}\sqrt{2}$.

# Relationships

## Builds Upon
- **Integral domain** — Every field is an integral domain; finite integral domains are fields
- **Division ring** — A field is a commutative division ring

## Enables
- **Polynomial ring over a field** — $F[x]$ has the division algorithm when $F$ is a field
- **Vector space** — Vector spaces are defined over fields
- **Field of fractions** — Every integral domain embeds in a field

## Contrasts With
- **Integral domain** — $\mathbb{Z}$ is an integral domain but not a field ($2$ has no inverse)
- **Ring** — A ring need not have inverses or commutativity of multiplication

# Common Errors

- **Error**: Assuming $\mathbb{Z}$ is a field because it is an integral domain
  **Correction**: $\mathbb{Z}$ lacks multiplicative inverses for most elements (only $\pm 1$ are units)

# Common Confusions

- **Confusion**: Believing every integral domain is a field
  **Clarification**: Only finite integral domains are automatically fields (Wedderburn's theorem, Theorem 16.16); infinite integral domains like $\mathbb{Z}$ are not fields

# Source Reference

Chapter 16: Rings, Section 16.1 (definition, p. 205) and Section 16.2 (pp. 207-209). See Theorem 16.16 and Theorem 16.35.

# Verification Notes

- Definition source: Direct quote from p. 205
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
