---
concept: Least Common Multiple (in Rings)
slug: least-common-multiple-ring
category: ring-theory
subcategory: factorization
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Euclidean Domains, Principal Ideal Domains, and Unique Factorization Domains"
chapter_number: 8
pdf_page: 279
section: "8.1 Euclidean Domains"
extraction_confidence: high
aliases:
  - "l.c.m."
  - "LCM"
prerequisites:
  - integral-domain
  - gcd-in-ring
extends: []
related:
  - gcd-in-ring
  - euclidean-domain
contrasts_with: []
answers_questions:
  - "What is a least common multiple in a ring?"
---

# Quick Definition
A least common multiple of a and b is an element e such that $a \mid e$ and $b \mid e$, and if $a \mid e'$ and $b \mid e'$ then $e \mid e'$.

# Core Definition
A *least common multiple* of a and b is an element e of R such that (i) $a \mid e$ and $b \mid e$, and (ii) if $a \mid e'$ and $b \mid e'$ then $e \mid e'$ (Exercise 11, Dummit & Foote, p. 279).

# Prerequisites
- **Integral domain** — LCMs are defined in integral domains
- **GCD in ring** — Related concept

# Key Properties
1. In a Euclidean Domain (or PID or UFD), LCMs exist and are unique up to associates
2. In a Euclidean Domain: $\text{lcm}(a, b) = ab / \gcd(a, b)$ (Exercise 11(c))
3. The LCM generates the largest principal ideal contained in $(a) \cap (b)$ (Exercise 11(a))

# Source Reference
Chapter 8, Section 8.1, Exercise 11, page 279.

# Verification Notes
- Definition: From Exercise 11, p. 279
- Confidence: HIGH — explicit definition in exercises
