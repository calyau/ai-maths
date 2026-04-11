---
concept: Nonzero Primes are Maximal in PIDs
slug: nonzero-prime-maximal-pid
category: ring-theory
subcategory: structure-theorems
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Euclidean Domains, Principal Ideal Domains, and Unique Factorization Domains"
chapter_number: 8
pdf_page: 283
section: "8.2 Principal Ideal Domains (P.I.D.s)"
extraction_confidence: high
aliases: []
prerequisites:
  - principal-ideal-domain
  - prime-ideal
  - maximal-ideal
extends: []
related:
  - prime-ideal
  - maximal-ideal
contrasts_with: []
answers_questions:
  - "Are prime ideals maximal in a PID?"
  - "What is the relationship between prime and maximal ideals in a PID?"
---

# Quick Definition
In a PID, every nonzero prime ideal is a maximal ideal.

# Core Definition
(Proposition 7) Every nonzero prime ideal in a Principal Ideal Domain is a maximal ideal. Proof: if $(p)$ is a nonzero prime and $(m) \supseteq (p)$, then $p = rm$ for some r. Since $(p)$ is prime, $r \in (p)$ or $m \in (p)$. If $m \in (p)$ then $(m) = (p)$; if $r \in (p)$ then $r = ps$ so $sm = 1$ and $(m) = R$ (Dummit & Foote, p. 283).

# Prerequisites
- **Principal ideal domain** — R is a PID
- **Prime ideal** — The ideal must be prime
- **Maximal ideal** — The conclusion is maximality

# Key Properties
1. In a PID: nonzero prime $\Leftrightarrow$ maximal
2. The zero ideal is prime (in any integral domain) but not maximal (unless R is a field)
3. This is stronger than the general result that maximal $\Rightarrow$ prime

# Source Reference
Chapter 8, Section 8.2, Proposition 7, page 283.

# Verification Notes
- Definition: Direct from Proposition 7, p. 283
- Confidence: HIGH — explicit proposition with proof
