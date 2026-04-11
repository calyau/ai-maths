---
concept: Galois Group of a Polynomial
slug: galois-group-of-polynomial
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
aliases:
  - "Galois group of f(x)"
prerequisites:
  - galois-group
  - splitting-field
  - symmetric-group
extends: []
related:
  - discriminant
  - resolvent
  - computation-of-galois-groups
contrasts_with: []
answers_questions:
  - "How do I compute the Galois group of a polynomial?"
---

# Quick Definition
The Galois group of a separable polynomial $f(x) \in F[x]$ is $\text{Gal}(K/F)$ where K is the splitting field of f over F. It embeds as a transitive subgroup of $S_n$ (n = deg f) via its action on the roots.

# Core Definition
For a separable polynomial $f(x)$ of degree n over F with splitting field K, the Galois group $\text{Gal}(f) = \text{Gal}(K/F)$ acts on the n roots of f and embeds as a transitive subgroup of $S_n$. Key tools for computation: (1) $|\text{Gal}(f)| = [K:F]$ divides $n!$; (2) $\text{Gal}(f) \subseteq A_n$ iff the discriminant D is a square in F; (3) resolvents and reduction mod p can determine the group (Dummit & Foote, pp. 610-624).

# Prerequisites
- **galois-group** — Defined for the splitting field
- **splitting-field** — The Galois group acts on roots
- **symmetric-group** — $\text{Gal}(f) \leq S_n$

# Key Properties
1. $\text{Gal}(f)$ is a transitive subgroup of $S_n$
2. If f is irreducible, $n \mid |\text{Gal}(f)|$
3. For irreducible cubic: $\text{Gal}(f) = S_3$ if $D$ not a square, $A_3$ if $D$ is a square
4. For irreducible quartic: determined by discriminant and resolvent cubic
5. Reduction mod p: if f mod p has cycle type $\sigma$ in $\mathbb{F}_p$, then $\text{Gal}(f)$ contains an element of that cycle type

# Context & Application
Computing Galois groups is one of the central computational problems of algebra. The techniques combine field theory (degrees), group theory (transitive subgroups of $S_n$), and number theory (reduction mod p).

# Examples
**Example** (p. 614): $f(x) = x^3 - 2$ over $\mathbb{Q}$: discriminant $D = -108$, not a square, so $\text{Gal}(f) = S_3$.

# Relationships
## Builds Upon
- **galois-group**, **splitting-field**, **symmetric-group**

## Related
- **discriminant** — Determines containment in $A_n$

# Source Reference
Chapter 14, Section 14.6, pp. 610-624; Section 14.8, pp. 637-645.

# Verification Notes
- Confidence: HIGH — extensive development with computational techniques
