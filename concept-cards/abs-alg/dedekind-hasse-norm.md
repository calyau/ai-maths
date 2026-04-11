---
concept: Dedekind-Hasse Norm
slug: dedekind-hasse-norm
category: ring-theory
subcategory: special-domains
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Euclidean Domains, Principal Ideal Domains, and Unique Factorization Domains"
chapter_number: 8
pdf_page: 281
section: "8.2 Principal Ideal Domains (P.I.D.s)"
extraction_confidence: high
aliases: []
prerequisites:
  - integral-domain
  - principal-ideal-domain
extends: []
related:
  - euclidean-domain
  - principal-ideal-domain
contrasts_with:
  - euclidean-function
answers_questions:
  - "What is a Dedekind-Hasse norm?"
  - "How does a Dedekind-Hasse norm characterize PIDs?"
---

# Quick Definition
A Dedekind-Hasse norm on an integral domain R is a positive norm N such that for all nonzero $a, b \in R$, either $b \mid a$ or there exists a nonzero element in $(a, b)$ with norm strictly less than $N(b)$.

# Core Definition
N is a *Dedekind-Hasse norm* if N is a positive norm and for every nonzero $a, b \in R$, either $a \in (b)$ or there exist $s, t \in R$ with $0 < N(sa - tb) < N(b)$ (Dummit & Foote, p. 281).

# Prerequisites
- **Integral domain** — R must be an integral domain
- **Principal ideal domain** — R is a PID iff it has a Dedekind-Hasse norm

# Key Properties
1. R is a PID iff R has a Dedekind-Hasse norm (Proposition 9, p. 281)
2. The Euclidean condition is the special case $s = 1$ (p. 281)
3. Used to prove $\mathbb{Z}[(1+\sqrt{-19})/2]$ is a PID but not Euclidean (pp. 281-282)

# Context & Application
The Dedekind-Hasse norm provides a weaker alternative to the Euclidean condition that still forces all ideals to be principal.

# Source Reference
Chapter 8, Section 8.2, Definition on page 281, Proposition 9.

# Verification Notes
- Definition: Direct from p. 281
- Confidence: HIGH — explicit definition with characterization theorem
