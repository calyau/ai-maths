---
concept: Field Norm
slug: field-norm
category: ring-theory
subcategory: ring-constructions
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Rings"
chapter_number: 7
pdf_page: 230
section: "7.1 Basic Definitions and Examples"
extraction_confidence: high
aliases:
  - "norm of a quadratic integer"
prerequisites:
  - quadratic-integer-ring
extends: []
related:
  - gaussian-integers
  - euclidean-function
contrasts_with: []
answers_questions:
  - "What is the field norm of a quadratic integer?"
  - "How does the norm characterize units?"
---

# Quick Definition
The field norm $N: \mathbb{Q}(\sqrt{D}) \to \mathbb{Q}$ is $N(a + b\sqrt{D}) = a^2 - Db^2$. It is multiplicative and characterizes units: $\alpha$ is a unit in $\mathcal{O}$ iff $N(\alpha) = \pm 1$.

# Core Definition
Define the *field norm* $N: \mathbb{Q}(\sqrt{D}) \to \mathbb{Q}$ by $N(a + b\sqrt{D}) = (a + b\sqrt{D})(a - b\sqrt{D}) = a^2 - Db^2$. The norm is multiplicative: $N(\alpha\beta) = N(\alpha)N(\beta)$. On the ring of integers $\mathcal{O}$, N takes integer values. An element $\alpha \in \mathcal{O}$ is a unit iff $N(\alpha) = \pm 1$ (Dummit & Foote, pp. 230-231).

# Prerequisites
- **Quadratic integer ring** — The norm is defined on quadratic fields

# Key Properties
1. $N$ is multiplicative: $N(\alpha\beta) = N(\alpha)N(\beta)$
2. $N(\alpha) \neq 0$ if $\alpha \neq 0$
3. $\alpha$ is a unit iff $N(\alpha) = \pm 1$
4. If $|N(\alpha)|$ is prime, then $\alpha$ is irreducible
5. For $D = -1$: $N(a + bi) = a^2 + b^2$ (always positive)

# Examples
**Example 1** (p. 231): In $\mathbb{Z}[i]$: $N(a+bi) = a^2 + b^2$, units have $a^2 + b^2 = 1$, giving $\{\pm 1, \pm i\}$.

**Example 2** (p. 231): In $\mathbb{Z}[\sqrt{2}]$: $N(1+\sqrt{2}) = 1 - 2 = -1$, so $1 + \sqrt{2}$ is a unit.

# Relationships

## Related
- **gaussian-integers** — $N(a+bi) = a^2 + b^2$
- **euclidean-function** — The field norm serves as the Euclidean function for some $\mathcal{O}$

# Source Reference
Chapter 7, Section 7.1, pages 230-231.

# Verification Notes
- Definition: Direct from pp. 230-231
- Confidence: HIGH — explicit definition with proofs
