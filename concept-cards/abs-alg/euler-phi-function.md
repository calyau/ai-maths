---
concept: "Euler's Phi-Function"
slug: euler-phi-function
category: foundations
subcategory: number-theory
tier: foundational
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Preliminaries"
chapter_number: 0
pdf_page: 14
section: "0.2 Properties of the Integers"
extraction_confidence: high
aliases:
  - "Euler totient function"
  - "$\\varphi(n)$"
prerequisites:
  - greatest-common-divisor
extends: []
related:
  - congruence-mod-n
  - cyclic-group
contrasts_with: []
answers_questions:
  - "What is Euler's phi-function?"
  - "How many generators does a cyclic group of order n have?"
---

# Quick Definition
$\varphi(n)$ counts the positive integers $a \leq n$ with $(a, n) = 1$. It equals the number of generators of a cyclic group of order n and the order of $(\mathbb{Z}/n\mathbb{Z})^\times$.

# Core Definition
For $n \in \mathbb{Z}^+$, the *Euler $\varphi$-function* $\varphi(n)$ is the number of positive integers $a \leq n$ with $(a, n) = 1$. For primes p: $\varphi(p) = p-1$. More generally, $\varphi(p^a) = p^{a-1}(p-1)$. The function is multiplicative: $\varphi(ab) = \varphi(a)\varphi(b)$ when $(a,b) = 1$. General formula: if $n = p_1^{\alpha_1} \cdots p_s^{\alpha_s}$ then $\varphi(n) = \prod p_i^{\alpha_i - 1}(p_i - 1)$ (Dummit & Foote, pp. 6-7).

# Prerequisites
- **Greatest common divisor** — $\varphi$ counts relatively prime integers

# Key Properties
1. $\varphi(p) = p - 1$ for primes p
2. $\varphi(p^a) = p^{a-1}(p - 1)$
3. Multiplicative: $\varphi(ab) = \varphi(a)\varphi(b)$ when $(a,b) = 1$
4. $|(\mathbb{Z}/n\mathbb{Z})^\times| = \varphi(n)$ (Proposition 4)
5. Number of generators of $Z_n$ is $\varphi(n)$

# Context & Application
$\varphi(n)$ gives the order of the multiplicative group $(\mathbb{Z}/n\mathbb{Z})^\times$ and counts generators of cyclic groups of order n. Euler's Theorem: $a^{\varphi(n)} \equiv 1 \pmod{n}$ when $(a,n) = 1$.

# Examples
**Example 1** (p. 6): $\varphi(12) = \varphi(4)\varphi(3) = 2 \cdot 2 = 4$ (the integers 1, 5, 7, 11 are coprime to 12).

# Relationships
## Builds Upon
- **greatest-common-divisor**

## Related
- **cyclic-group** — $\varphi(n)$ generators for $Z_n$
- **congruence-mod-n** — $|(\mathbb{Z}/n\mathbb{Z})^\times| = \varphi(n)$

# Source Reference
Chapter 0, Section 0.2, pages 6-7.

# Verification Notes
- Definition source: direct from source pp. 6-7
- Confidence rationale: explicitly defined with formula
- Uncertainties: none
- Cross-reference status: verified
