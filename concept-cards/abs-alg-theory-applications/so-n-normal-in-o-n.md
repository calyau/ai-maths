---
concept: SO(n) is Normal in O(n)
slug: so-n-normal-in-o-n
category: matrix-groups
subcategory: classical-matrix-groups
tier: intermediate
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Matrix Groups and Symmetry"
chapter_number: 12
pdf_page: 169
section: "Exercises"
extraction_confidence: high
aliases: []
prerequisites:
  - special-orthogonal-group
  - orthogonal-group
  - normal-subgroup
  - determinant-as-homomorphism
extends: []
related:
  - kernel-of-homomorphism
contrasts_with: []
answers_questions:
  - "Why is SO(n) normal in O(n)?"
---

# Quick Definition

$SO(n)$ is a normal subgroup of $O(n)$ because it is the kernel of the determinant restricted to $O(n)$: $\det|_{O(n)}: O(n) \to \{-1, 1\}$. The quotient $O(n)/SO(n) \cong \mathbb{Z}_2$.

# Core Definition

**Exercise 12.4.10**: "Prove that $SO(n)$ is a normal subgroup of $O(n)$" (Judson, p. 169). Since $SO(n) = \ker(\det|_{O(n)})$ and the kernel of any homomorphism is normal, $SO(n) \trianglelefteq O(n)$.

# Prerequisites

- **Special orthogonal group** — $SO(n)$
- **Orthogonal group** — $O(n)$
- **Normal subgroup** — $SO(n) \trianglelefteq O(n)$
- **Determinant as homomorphism** — $\det$ restricted to $O(n)$

# Key Properties

1. $SO(n) = \ker(\det|_{O(n)})$
2. $SO(n) \trianglelefteq O(n)$
3. $O(n)/SO(n) \cong \mathbb{Z}_2$
4. $[O(n):SO(n)] = 2$ (index 2 subgroup)

# Relationships

## Related
- **Kernel of homomorphism** — $SO(n)$ is a kernel, hence normal

# Source Reference

Chapter 12: Matrix Groups and Symmetry, Exercise 12.4.10, p. 169.

# Verification Notes

- Definition source: Exercise 12.4.10
- Confidence: HIGH
