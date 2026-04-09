---
# === CORE IDENTIFICATION ===
concept: Field of Fractions
slug: field-of-fractions

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
pdf_page: 239
section: "18.1 Fields of Fractions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "field of quotients"
  - "fraction field"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - integral-domain
extends: []
related:
  - field
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the field of fractions of an integral domain?"
  - "How does an integral domain embed into a field?"
---

# Quick Definition

The field of fractions $F_D$ of an integral domain $D$ is the smallest field containing $D$, constructed by forming equivalence classes of "fractions" $[a, b]$ with $a, b \in D$ and $b \neq 0$, analogous to constructing $\mathbb{Q}$ from $\mathbb{Z}$.

# Core Definition

Given an integral domain $D$, define $S = \{(a,b) : a, b \in D, b \neq 0\}$ with equivalence $(a,b) \sim (c,d)$ iff $ad = bc$. The field of fractions $F_D$ is the set of equivalence classes with $[a,b] + [c,d] = [ad+bc, bd]$ and $[a,b] \cdot [c,d] = [ac, bd]$ (Judson, Lemma 18.3, p. 240). The embedding $\phi : D \to F_D$ given by $\phi(a) = [a,1]$ is injective, and $F_D$ is unique up to isomorphism (Theorem 18.4, p. 241).

# Prerequisites

- **Integral domain** — The construction requires no zero divisors for the equivalence relation to work

# Key Properties

1. $F_D$ is a field (Lemma 18.3)
2. $D$ embeds in $F_D$ via $a \mapsto [a,1]$ (Theorem 18.4)
3. $F_D$ is the smallest field containing $D$ (unique up to isomorphism)
4. Characteristic $0$ fields contain $\mathbb{Q}$; characteristic $p$ fields contain $\mathbb{Z}_p$ (Corollaries 18.6, 18.7)

# Construction / Recognition

## To Construct:
1. Form pairs $(a,b)$ with $b \neq 0$
2. Define equivalence: $(a,b) \sim (c,d)$ iff $ad = bc$
3. Define addition and multiplication on equivalence classes
4. Verify field axioms

# Context & Application

The field of fractions construction generalizes the passage from $\mathbb{Z}$ to $\mathbb{Q}$. It shows that every integral domain "lives inside" a field. This is used to study factorization by passing to the field of fractions and back.

# Examples

**Example 1** (p. 239): The field of fractions of $\mathbb{Z}$ is $\mathbb{Q}$.

**Example 2** (p. 242): The field of fractions of $\mathbb{Q}[x]$ is $\mathbb{Q}(x)$, the field of rational expressions.

# Relationships

## Builds Upon
- **Integral domain** — The source domain

## Enables
- **Factorization theory** — Connects factorization in $D$ to factorization in $F_D[x]$

# Common Errors

- **Error**: Trying to construct the field of fractions for a ring with zero divisors
  **Correction**: The construction requires an integral domain; with zero divisors, the equivalence relation fails to be well-defined

# Common Confusions

- **Confusion**: Thinking the field of fractions adds new algebraic structure
  **Clarification**: $F_D$ simply "fills in the denominators"; $D$ embeds faithfully

# Source Reference

Chapter 18: Integral Domains, Section 18.1, pages 239-242. See Lemma 18.3 and Theorem 18.4.

# Verification Notes

- Definition source: Direct from pp. 239-241
- Confidence: HIGH — explicit construction with proof
- Cross-reference status: Verified
- Uncertainties: None
