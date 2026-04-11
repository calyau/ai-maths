---
concept: Quadratic Integer Ring
slug: quadratic-integer-ring
category: ring-theory
subcategory: ring-constructions
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Rings"
chapter_number: 7
pdf_page: 229
section: "7.1 Basic Definitions and Examples"
extraction_confidence: high
aliases:
  - "ring of integers in a quadratic field"
prerequisites:
  - integral-domain
  - subring
extends:
  - integral-domain
related:
  - gaussian-integers
  - field-of-fractions
  - euclidean-domain
contrasts_with: []
answers_questions:
  - "What is a quadratic integer ring?"
  - "What is the ring of integers in a quadratic field?"
---

# Quick Definition
For squarefree integer D, the quadratic integer ring $\mathcal{O} = \mathbb{Z}[\omega]$ is the ring of integers in the quadratic field $\mathbb{Q}(\sqrt{D})$, where $\omega = \sqrt{D}$ if $D \equiv 2, 3 \pmod{4}$ and $\omega = \frac{1+\sqrt{D}}{2}$ if $D \equiv 1 \pmod{4}$.

# Core Definition
Let D be a squarefree integer. Define the quadratic integer ring $\mathcal{O} = \mathbb{Z}[\omega] = \{a + b\omega \mid a, b \in \mathbb{Z}\}$ where $\omega = \sqrt{D}$ if $D \equiv 2, 3 \pmod{4}$ and $\omega = \frac{1+\sqrt{D}}{2}$ if $D \equiv 1 \pmod{4}$. This is the *ring of integers* in $\mathbb{Q}(\sqrt{D})$ (Dummit & Foote, pp. 229-230).

# Prerequisites
- **Integral domain** — Quadratic integer rings are integral domains
- **Subring** — They are subrings of $\mathbb{Q}(\sqrt{D})$

# Key Properties
1. The field norm $N(a+b\omega) = a^2 - Db^2$ (or $a^2+ab+\frac{1-D}{4}b^2$ when $D \equiv 1 \pmod{4}$) is multiplicative
2. $\alpha$ is a unit iff $N(\alpha) = \pm 1$ (p. 231)
3. The field of fractions is $\mathbb{Q}(\sqrt{D})$ (p. 264)
4. $D = -1$ gives the Gaussian integers $\mathbb{Z}[i]$
5. For $D < 0$: units are $\{\pm 1\}$ (except $D = -1$ and $D = -3$)
6. For $D > 0$: the unit group is always infinite

# Examples
**Example 1** (p. 228): $D = -1$: $\mathbb{Z}[i]$, the Gaussian integers. Euclidean, PID, UFD.

**Example 2** (p. 275): $D = -5$: $\mathbb{Z}[\sqrt{-5}]$ is NOT a UFD ($6 = 2 \cdot 3 = (1+\sqrt{-5})(1-\sqrt{-5})$).

**Example 3** (pp. 280-281): $D = -19$: $\mathbb{Z}[(1+\sqrt{-19})/2]$ is a PID but NOT Euclidean.

# Relationships

## Builds Upon
- **integral-domain** — Every quadratic integer ring is an integral domain

## Related
- **gaussian-integers** — The special case $D = -1$
- **euclidean-domain** — Some quadratic integer rings are Euclidean ($D = -1, -2, -3, -7, -11$)

# Source Reference
Chapter 7, Section 7.1, "Quadratic Integer Rings" example, pages 229-232.

# Verification Notes
- Definition: Direct from pp. 229-230
- Confidence: HIGH — extensive discussion with many examples
