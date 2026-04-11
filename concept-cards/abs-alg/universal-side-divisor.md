---
concept: Universal Side Divisor
slug: universal-side-divisor
category: ring-theory
subcategory: special-domains
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Euclidean Domains, Principal Ideal Domains, and Unique Factorization Domains"
chapter_number: 8
pdf_page: 275
section: "8.1 Euclidean Domains"
extraction_confidence: high
aliases: []
prerequisites:
  - integral-domain
  - unit
extends: []
related:
  - euclidean-domain
contrasts_with: []
answers_questions:
  - "What is a universal side divisor?"
  - "How can one prove a ring is not Euclidean?"
---

# Quick Definition
A nonzero non-unit element u in an integral domain R is a universal side divisor if for every $x \in R$, $u$ divides $x - z$ for some $z$ that is 0 or a unit.

# Core Definition
An element $u \in R - \widetilde{R}$ (where $\widetilde{R} = R^{\times} \cup \{0\}$) is a *universal side divisor* if for every $x \in R$ there is some $z \in \widetilde{R}$ such that u divides $x - z$. Equivalently, every $x$ can be written $x = qu + z$ where z is 0 or a unit (Dummit & Foote, p. 275).

# Prerequisites
- **Integral domain** — R is an integral domain
- **Unit** — The definition involves units

# Key Properties
1. If R is Euclidean (and not a field), then R has universal side divisors (Proposition 5, p. 275)
2. Contrapositive: if R has no universal side divisors, R is not Euclidean
3. Used to prove $\mathbb{Z}[(1+\sqrt{-19})/2]$ is not Euclidean (pp. 275-276)

# Context & Application
Universal side divisors provide a criterion for showing a ring is NOT Euclidean (with respect to any norm), complementing the method of finding non-principal ideals.

# Source Reference
Chapter 8, Section 8.1, Definition on page 275, Proposition 5.

# Verification Notes
- Definition: Direct from p. 275
- Confidence: HIGH — explicit definition
