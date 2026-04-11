---
concept: Straightedge and Compass Construction
slug: straightedge-compass-construction
category: field-theory
subcategory: constructions
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Field Theory"
chapter_number: 13
pdf_page: 531
section: "13.3 Classical Straightedge and Compass Constructions"
extraction_confidence: high
aliases:
  - "constructible number"
  - "compass and straightedge"
prerequisites:
  - field-extension
  - degree-of-extension
extends: []
related:
  - algebraic-extension
contrasts_with: []
answers_questions:
  - "What numbers are constructible by straightedge and compass?"
---

# Quick Definition
A real number $\alpha$ is constructible iff $[\mathbb{Q}(\alpha):\mathbb{Q}]$ is a power of 2. This settles the classical impossibility results: doubling the cube, trisecting angles, and squaring the circle are impossible.

# Core Definition
A real number is constructible (by straightedge and compass) iff it can be obtained from the rationals by a finite sequence of field extensions, each of degree 2. Thus $\alpha$ is constructible iff $\alpha$ lies in a field K with $[K:\mathbb{Q}] = 2^k$ for some k, which implies $[\mathbb{Q}(\alpha):\mathbb{Q}]$ divides $2^k$, hence is a power of 2. The constructible numbers form a subfield of $\mathbb{R}$ (Dummit & Foote, pp. 531-536).

# Prerequisites
- **field-extension** — Constructibility is characterized by degrees of extensions
- **degree-of-extension** — The degree must be a power of 2

# Key Properties
1. $\alpha$ constructible $\Rightarrow$ $[\mathbb{Q}(\alpha):\mathbb{Q}]$ is a power of 2
2. Doubling the cube requires $\sqrt[3]{2}$, with $[\mathbb{Q}(\sqrt[3]{2}):\mathbb{Q}] = 3$, impossible
3. Trisecting $60°$ requires a root of $8x^3 - 6x - 1$, degree 3, impossible
4. Squaring the circle requires $\sqrt{\pi}$, transcendental over $\mathbb{Q}$, impossible
5. Regular n-gon constructible iff $n = 2^a p_1 \cdots p_k$ where $p_i$ are distinct Fermat primes

# Context & Application
This is one of the most celebrated applications of field theory, resolving questions that were open for over 2000 years since ancient Greece.

# Relationships
## Builds Upon
- **field-extension**, **degree-of-extension**

# Source Reference
Chapter 13, Section 13.3, pp. 531-536.

# Verification Notes
- Confidence: HIGH — classic application of field theory
