---
concept: Submodule
slug: submodule
category: module-theory
subcategory: basic-definitions
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Module Theory"
chapter_number: 10
pdf_page: 337
section: "10.1 Basic Definitions and Examples"
extraction_confidence: high
aliases:
  - "R-submodule"
prerequisites:
  - left-module
extends:
  - subgroup
related:
  - left-ideal
  - subspace
contrasts_with:
  - subspace
answers_questions:
  - "What is a submodule?"
  - "How do I verify a subset is a submodule?"
---

# Quick Definition
An R-submodule of an R-module M is a subgroup N of M that is closed under the action of ring elements, i.e., $rn \in N$ for all $r \in R$, $n \in N$.

# Core Definition
Let R be a ring and let M be an R-module. An R-submodule of M is a subgroup N of M which is closed under the action of ring elements, i.e., $rn \in N$ for all $r \in R$, $n \in N$. Submodules are subsets of M that are themselves modules under the restricted operations. When $R = F$ is a field, submodules are the same as subspaces. Every R-module M has the submodules M and 0 (the latter called the *trivial submodule*) (Dummit & Foote, p. 338).

# Prerequisites
- **left-module** — Submodules are subsets of modules that are themselves modules

# Key Properties
1. When R is a field, submodules are exactly subspaces
2. When R is viewed as a left module over itself, submodules are precisely the left ideals of R
3. Every module has at least two submodules: M and {0}
4. The submodule criterion: N is a submodule iff $N \neq \emptyset$ and $x + ry \in N$ for all $r \in R$ and $x, y \in N$

# Construction / Recognition
## To Verify (Submodule Criterion, Proposition 1):
1. Check that $N \neq \emptyset$ (or equivalently, $0 \in N$)
2. Check that $x + ry \in N$ for all $r \in R$ and all $x, y \in N$

# Context & Application
Submodules play the same role in module theory that normal subgroups play in group theory and ideals play in ring theory. They are the building blocks for constructing quotient modules and understanding module structure.

# Examples
**Example 1** (p. 338): If $R = F$ is a field and M is a vector space, the submodules are exactly the subspaces.
**Example 2** (p. 338): The left ideals of a ring R are precisely the submodules of R viewed as a left module over itself.

# Relationships
## Builds Upon
- **left-module** — Submodules live inside modules

## Enables
- **quotient-module** — Formed by dividing a module by a submodule
- **direct-sum-of-modules** — Internal direct sum of submodules

## Contrasts With
- **subspace** — A submodule when the ring is a field

# Common Errors
- **Error**: Forgetting to check closure under the ring action. **Correction**: A subgroup of M is a submodule only if it is also closed under multiplication by all ring elements.

# Common Confusions
- **Confusion**: Thinking submodules require a normal subgroup condition like in group theory. **Clarification**: Since modules are abelian groups, every subgroup is normal, so the condition is simply being a subgroup closed under the ring action.

# Source Reference
Chapter 10, Section 10.1, pp. 338-339. See Proposition 1 (Submodule Criterion) on p. 340.

# Verification Notes
- Definition: direct from p. 338
- Submodule criterion: Proposition 1, p. 340
- Confidence: HIGH — explicit definition
