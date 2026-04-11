---
concept: Discriminant
slug: discriminant
category: galois-theory
subcategory: galois-groups-of-polynomials
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Galois Theory"
chapter_number: 14
pdf_page: 610
section: "14.6 Galois Groups of Polynomials"
extraction_confidence: high
aliases: []
prerequisites:
  - galois-group
  - alternating-group
extends: []
related:
  - resolvent
  - galois-group-of-polynomial
contrasts_with: []
answers_questions:
  - "What is the discriminant of a polynomial?"
  - "How do I compute the Galois group of a polynomial?"
---

# Quick Definition
The discriminant of a polynomial $f(x)$ with roots $\alpha_1, \ldots, \alpha_n$ is $D = \prod_{i < j} (\alpha_i - \alpha_j)^2$. It determines whether the Galois group is contained in $A_n$: $\text{Gal}(f) \subseteq A_n$ iff $D$ is a perfect square in F.

# Core Definition
For a polynomial $f(x)$ with roots $\alpha_1, \ldots, \alpha_n$, define $\Delta = \prod_{i<j}(\alpha_i - \alpha_j)$. The discriminant is $D = \Delta^2 = \prod_{i<j}(\alpha_i - \alpha_j)^2 \in F$. The Galois group of f acts on $\Delta$ by $\sigma(\Delta) = \epsilon(\sigma)\Delta$ where $\epsilon$ is the sign character. Thus: $\text{Gal}(f) \subseteq A_n$ iff $\Delta \in F$ iff $D$ is a square in F (Dummit & Foote, pp. 610-614).

# Prerequisites
- **galois-group** — The discriminant helps determine the Galois group
- **alternating-group** — Discriminant detects containment in $A_n$

# Key Properties
1. $D \in F$ always (it is symmetric in the roots)
2. $\text{Gal}(f) \subseteq A_n$ iff $D$ is a square in F
3. For quadratic $x^2 + bx + c$: $D = b^2 - 4c$
4. For cubic $x^3 + px + q$: $D = -4p^3 - 27q^2$
5. $D = 0$ iff f has a repeated root

# Relationships
## Builds Upon
- **galois-group**, **alternating-group**

## Related
- **resolvent** — Another tool for computing Galois groups

# Source Reference
Chapter 14, Section 14.6, pp. 610-614.

# Verification Notes
- Confidence: HIGH — explicit definition with computability criteria
