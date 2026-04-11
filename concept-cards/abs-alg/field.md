---
concept: Field
slug: field
category: ring-theory
subcategory: basic-definitions
tier: foundational
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Rings"
chapter_number: 7
pdf_page: 223
section: "7.1 Basic Definitions and Examples"
extraction_confidence: high
aliases: []
prerequisites:
  - commutative-ring
  - ring-with-identity
  - unit
extends:
  - division-ring
  - integral-domain
related:
  - field-of-fractions
  - maximal-ideal
  - polynomial-ring-over-field
contrasts_with:
  - ring
  - integral-domain
  - division-ring
answers_questions:
  - "What is a field?"
  - "What distinguishes a ring from a field?"
  - "What distinguishes a field from an integral domain?"
---

# Quick Definition
A field is a commutative ring with identity $1 \neq 0$ in which every nonzero element has a multiplicative inverse.

# Core Definition
A commutative division ring is called a *field*. Equivalently, a field is a commutative ring F with identity $1 \neq 0$ in which every nonzero element is a unit, i.e., $F^{\times} = F - \{0\}$ (Dummit & Foote, p. 224).

# Prerequisites
- **Commutative ring** — A field is commutative
- **Ring with identity** — A field has a multiplicative identity
- **Unit** — Every nonzero element must be a unit

# Key Properties
1. Every nonzero element has a multiplicative inverse
2. Contains no zero divisors
3. The only ideals are 0 and F (Proposition 9(2), p. 253)
4. Any nonzero ring homomorphism from a field is injective (Corollary 10, p. 254)
5. $\mathbb{Z}/n\mathbb{Z}$ is a field if and only if n is prime (p. 228)
6. Any finite integral domain is a field (Corollary 3, p. 229)

# Construction / Recognition
## To Recognize:
1. Verify R is a commutative ring with $1 \neq 0$
2. Check that every nonzero element has a multiplicative inverse

## To Construct:
1. Take a commutative ring R with identity and quotient by a maximal ideal M: R/M is a field (Proposition 12, p. 256)
2. Take the field of fractions of an integral domain (Theorem 15, p. 260)

# Context & Application
Fields are one of the most important examples of rings. They are the basic coefficient rings for linear algebra and are the setting for Galois theory (Part IV). The ideal structure of fields is trivial, so the study of fields focuses on embeddings and automorphisms (p. 254).

# Examples
**Example 1** (p. 224): $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$ are fields.

**Example 2** (p. 228): $\mathbb{Z}/p\mathbb{Z}$ is a field for every prime p.

**Example 3** (p. 228): The quadratic field $\mathbb{Q}(\sqrt{D})$ for squarefree $D$ is a field.

# Relationships

## Builds Upon
- **division-ring** — A field is a commutative division ring
- **integral-domain** — Every field is an integral domain; a finite integral domain is a field

## Enables
- **polynomial-ring-over-field** — $F[x]$ is a Euclidean Domain
- **field-of-fractions** — Every integral domain has a field of fractions

## Contrasts With
- **ring** — A ring need not have multiplicative inverses
- **integral-domain** — An integral domain need not have multiplicative inverses
- **division-ring** — A division ring need not be commutative

# Common Errors
- **Error**: Assuming $\mathbb{Z}/n\mathbb{Z}$ is always a field
  **Correction**: $\mathbb{Z}/n\mathbb{Z}$ is a field only when n is prime

# Common Confusions
- **Confusion**: Thinking a field is just a ring with no zero divisors
  **Clarification**: An integral domain has no zero divisors but need not be a field (e.g., $\mathbb{Z}$)

# Source Reference
Chapter 7, Section 7.1, Definition on page 224. See Proposition 9(2) on page 253 and Corollary 3 on page 229.

# Verification Notes
- Definition: Direct from p. 224
- Key properties: Proposition 9 (p. 253), Corollary 3 (p. 229), Corollary 10 (p. 254)
- Confidence: HIGH — explicit definition with many examples
