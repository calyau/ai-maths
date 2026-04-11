---
concept: Gaussian Integers
slug: gaussian-integers
category: ring-theory
subcategory: special-domains
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Euclidean Domains, Principal Ideal Domains, and Unique Factorization Domains"
chapter_number: 8
pdf_page: 270
section: "8.1 Euclidean Domains"
extraction_confidence: high
aliases:
  - "Z[i]"
prerequisites:
  - integral-domain
  - euclidean-domain
extends:
  - euclidean-domain
related:
  - quadratic-integer-ring
  - unique-factorization-domain
contrasts_with: []
answers_questions:
  - "What are the Gaussian integers?"
  - "Why is Z[i] a Euclidean Domain?"
  - "What are the irreducibles in Z[i]?"
---

# Quick Definition
The Gaussian integers $\mathbb{Z}[i] = \{a + bi \mid a, b \in \mathbb{Z}\}$ form a subring of $\mathbb{C}$, with norm $N(a+bi) = a^2 + b^2$. They are a Euclidean Domain.

# Core Definition
The ring $\mathbb{Z}[i]$ of Gaussian integers consists of all complex numbers $a + bi$ with $a, b \in \mathbb{Z}$. It is a Euclidean Domain with respect to the norm $N(a+bi) = a^2 + b^2$ (Dummit & Foote, pp. 228, 273).

# Prerequisites
- **Integral domain** — $\mathbb{Z}[i]$ is a subring of the field $\mathbb{C}$
- **Euclidean domain** — $\mathbb{Z}[i]$ is Euclidean with respect to the field norm

# Key Properties
1. Units: $\mathbb{Z}[i]^{\times} = \{\pm 1, \pm i\}$ (p. 228)
2. Euclidean with $N(a+bi) = a^2+b^2$ (p. 273)
3. Hence also a PID and a UFD
4. N is multiplicative: $N(\alpha\beta) = N(\alpha)N(\beta)$ (p. 206)
5. $\alpha$ is a unit iff $N(\alpha) = 1$

# Construction / Recognition
## Division Algorithm:
1. Given $\alpha, \beta \in \mathbb{Z}[i]$ with $\beta \neq 0$
2. Compute $\alpha/\beta = r + si$ in $\mathbb{Q}(i)$
3. Round r and s to nearest integers p, q
4. Then $\alpha = (p+qi)\beta + \gamma$ with $N(\gamma) \leq \frac{1}{2}N(\beta)$

# Context & Application
Gauss introduced these numbers around 1800 to study biquadratic reciprocity. Their study led to the classification of primes expressible as sums of two squares (Fermat's theorem).

# Examples
**Example 1** (p. 293): Irreducibles in $\mathbb{Z}[i]$ are: (a) $1+i$ (norm 2), (b) primes $p \equiv 3 \pmod{4}$ from $\mathbb{Z}$ (norm $p^2$), (c) $a \pm bi$ where $p = a^2+b^2$ for primes $p \equiv 1 \pmod{4}$ (norm p).

**Example 2** (p. 293): $2 = -i(1+i)^2$ in $\mathbb{Z}[i]$.

**Example 3** (p. 293): $5 = (2+i)(2-i)$ since $5 \equiv 1 \pmod{4}$.

# Relationships

## Builds Upon
- **euclidean-domain** — $\mathbb{Z}[i]$ is a Euclidean Domain

## Related
- **quadratic-integer-ring** — $\mathbb{Z}[i]$ is the case $D = -1$

# Common Errors
- **Error**: Forgetting that $1+i$ and $1-i$ are associates in $\mathbb{Z}[i]$
  **Correction**: $1-i = (-i)(1+i)$, so they differ by the unit $-i$

# Common Confusions
- **Confusion**: Thinking all primes in $\mathbb{Z}$ remain prime in $\mathbb{Z}[i]$
  **Clarification**: Primes $p \equiv 1 \pmod{4}$ split; primes $p \equiv 3 \pmod{4}$ remain prime; $2 = -i(1+i)^2$ ramifies

# Source Reference
Chapter 7, Section 7.1, page 228 (definition); Chapter 8, Section 8.1, page 273 (Euclidean property); Chapter 8, Section 8.3, Proposition 18, pages 293-294 (irreducibles).

# Verification Notes
- Definition: Direct from pp. 228, 273
- Irreducibles: Proposition 18, pp. 293-294
- Confidence: HIGH — extensively discussed example
