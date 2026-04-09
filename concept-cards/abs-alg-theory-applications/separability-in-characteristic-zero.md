---
concept: Separability in Characteristic Zero
slug: separability-in-characteristic-zero
category: galois-theory
subcategory: field-automorphisms
tier: advanced
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Galois Theory"
chapter_number: 23
pdf_page: 307
section: "23.1 Field Automorphisms"
extraction_confidence: high
aliases: []
prerequisites:
  - separable-polynomial
  - characteristic-of-a-field
extends: []
related:
  - separable-extension
  - galois-extension
contrasts_with: []
answers_questions:
  - "Are all extensions of characteristic 0 fields separable?"
  - "When can inseparable extensions occur?"
---

# Quick Definition

Every irreducible polynomial over a field of characteristic 0 is separable. Inseparable polynomials can only occur over fields of positive characteristic, and only when $f(x) = g(x^p)$.

# Core Definition

**Proposition 23.12.** Let $f(x)$ be an irreducible polynomial over $F$. If the characteristic of $F$ is 0, then $f(x)$ is separable. If the characteristic of $F$ is $p$ and $f(x) \neq g(x^p)$ for some $g(x) \in F[x]$, then $f(x)$ is also separable (Judson, p. 310).

# Prerequisites

- **Separable polynomial** — The concept being characterized
- **Characteristic of a field** — Determines whether inseparability can occur

# Key Properties

1. In characteristic 0: all irreducible polynomials are separable
2. In characteristic $p$: inseparability only occurs for polynomials of the form $g(x^p)$
3. Over finite fields, all extensions are separable (combining with the structure of finite fields)
4. This means Galois theory "works automatically" in characteristic 0

# Context & Application

This result is reassuring for the study of Galois theory over $\mathbb{Q}$ and its extensions: separability is never an issue. One only needs to worry about separability in positive characteristic, and even then, only for special polynomials.

# Examples

**Example 1**: Over $\mathbb{Q}$, every irreducible polynomial is automatically separable, so every finite normal extension is Galois.

**Example 2**: Over $\mathbb{Z}_p(t)$, the polynomial $x^p - t$ is irreducible but inseparable (Exercise 23.5.13).

# Relationships

## Builds Upon
- **Separable polynomial** — Characterizes when polynomials are separable

## Related
- **Separable extension** — All extensions of char 0 fields are separable
- **Galois extension** — In char 0, normal implies Galois

# Source Reference

Chapter 23: Galois Theory, Section 23.1, page 310. Proposition 23.12.

# Verification Notes

- Definition source: Direct from Proposition 23.12, p. 310
- Confidence: HIGH — explicit proposition
- Cross-reference status: Verified
- Uncertainties: None
