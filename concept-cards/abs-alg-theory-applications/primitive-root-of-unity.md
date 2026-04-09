---
# === CORE IDENTIFICATION ===
concept: Primitive Root of Unity
slug: primitive-root-of-unity

# === CLASSIFICATION ===
category: cyclic-groups
subcategory: complex-numbers
tier: intermediate

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Cyclic Groups"
chapter_number: 4
pdf_page: 66
section: "The Circle Group and the Roots of Unity"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - primitive nth root of unity

# === TYPED RELATIONSHIPS ===
prerequisites:
  - roots-of-unity
  - generator
extends: []
related:
  - relatively-prime
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a cyclic group?"
---

# Quick Definition

A primitive $n$th root of unity is a generator of the cyclic group of $n$th roots of unity. Equivalently, $\omega^k$ is primitive if and only if $\gcd(k, n) = 1$.

# Core Definition

"A generator for the group of the $n$th roots of unity is called a primitive $n$th root of unity" (Judson, p. 66).

# Prerequisites

- **Roots of unity** — Primitive roots generate the group of all roots
- **Generator** — A primitive root is a generator

# Key Properties

1. $\omega = \operatorname{cis}(2\pi/n)$ is always a primitive $n$th root
2. $\omega^k$ is primitive iff $\gcd(k, n) = 1$
3. There are $\phi(n)$ primitive $n$th roots of unity
4. The primitive roots generate the full group of $n$th roots

# Examples

**Example 1** (p. 66): The primitive 8th roots of unity are $\omega, \omega^3, \omega^5, \omega^7$ where $\omega = \frac{\sqrt{2}}{2} + \frac{\sqrt{2}}{2}i$ (those with $\gcd(k, 8) = 1$).

# Relationships

## Builds Upon
- **roots-of-unity** — Primitive roots generate all roots
- **generator** — Is a generator of the roots of unity group

## Related
- **relatively-prime** — $\omega^k$ is primitive iff $\gcd(k, n) = 1$

# Source Reference

Chapter 4: Cyclic Groups, Section 4.2, page 66.

# Verification Notes

- Definition source: Direct from p. 66
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
