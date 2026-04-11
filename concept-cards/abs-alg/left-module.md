---
concept: Left Module
slug: left-module
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
  - "left R-module"
  - "R-module"
  - "module"
prerequisites:
  - ring
  - abelian-group
extends:
  - group-action
related:
  - right-module
  - vector-space
  - submodule
  - z-module
contrasts_with:
  - right-module
  - vector-space
answers_questions:
  - "What is a module?"
  - "How do modules generalize vector spaces?"
  - "What must I know before studying module theory?"
---

# Quick Definition
A left R-module is a set M that is an abelian group under addition together with an action of a ring R on M satisfying distributive and associative laws. Modules generalize vector spaces by allowing the scalars to come from an arbitrary ring rather than a field.

# Core Definition
Let R be a ring (not necessarily commutative nor with 1). A *left R-module* or a *left module over* R is a set M together with (1) a binary operation + on M under which M is an abelian group, and (2) an action of R on M (a map $R \times M \to M$) denoted by rm, satisfying: (a) $(r+s)m = rm + sm$, (b) $(rs)m = r(sm)$, and (c) $r(m+n) = rm + rn$ for all $r, s \in R$ and $m, n \in M$. If R has a 1, we impose the additional axiom (d) $1m = m$ for all $m \in M$ (Dummit & Foote, p. 337).

# Prerequisites
- **ring** — The scalars in a module come from a ring; ring axioms are essential
- **abelian-group** — The underlying additive structure of a module is an abelian group

# Key Properties
1. When R is a field F, the axioms for an R-module are precisely those for a vector space over F
2. Modules satisfying axiom (d) are called *unital* modules
3. The descriptor "left" indicates ring elements appear on the left of module elements
4. If R is commutative, every left R-module can be made into a right R-module by defining $mr = rm$
5. Every abelian group is a $\mathbb{Z}$-module in a unique way

# Construction / Recognition
## To Construct:
1. Start with an abelian group $(M, +)$
2. Define a map $R \times M \to M$ sending $(r, m) \mapsto rm$
3. Verify the four module axioms (a)-(d)

## To Recognize:
1. Check that M is an abelian group under addition
2. Check that R acts on M satisfying the distributive and associativity axioms
3. If R has identity, check that $1m = m$

# Context & Application
Modules are the "representation objects" for rings: they are algebraic objects on which rings act. Emmy Noether pioneered the use of modules, demonstrating the power and elegance of this structure. The structure of a ring R (particularly its ideals) is reflected by the structure of its modules and vice versa, analogous to how normal subgroups of a group are reflected by its permutation representations.

# Examples
**Example 1** (p. 337): Any ring R is a left R-module over itself, where the action is ring multiplication. The submodules of R (as a left module over itself) are precisely the left ideals of R.

**Example 2** (p. 338): If $R = F$ is a field, then every vector space over F is an F-module and vice versa. Affine n-space $F^n$ with componentwise operations is a vector space of dimension n.

**Example 3** (p. 338): $R^n$ with componentwise operations is the free module of rank n over R.

**Example 4** (p. 339): Every abelian group is a $\mathbb{Z}$-module in a unique way, with $na$ defined as the n-fold sum of a.

# Relationships
## Builds Upon
- **ring** — Provides the scalars for the module action
- **abelian-group** — Provides the additive structure of the module

## Enables
- **submodule** — Subsets of modules closed under the operations
- **module-homomorphism** — Structure-preserving maps between modules
- **free-module** — Modules with a basis
- **tensor-product** — Product construction for modules

## Related
- **group-action** — Module axioms are analogous to group action axioms
- **z-module** — Special case showing abelian groups are $\mathbb{Z}$-modules

## Contrasts With
- **vector-space** — A module over a field; has stronger properties (e.g., always has a basis)
- **right-module** — Ring elements act on the right instead of the left

# Common Errors
- **Error**: Assuming every module has a basis (like vector spaces). **Correction**: Only free modules have bases; for example, $\mathbb{Z}/2\mathbb{Z}$ is a $\mathbb{Z}$-module with no basis.
- **Error**: Assuming left modules are automatically right modules. **Correction**: This is only true when R is commutative.

# Common Confusions
- **Confusion**: Believing modules and vector spaces are essentially the same thing. **Clarification**: Vector spaces are modules over fields; general modules can have much more complex structure (torsion elements, no bases, etc.).
- **Confusion**: Thinking the "unital" condition $1m = m$ is always assumed. **Clarification**: This requires R to have a 1; however, in Dummit & Foote all modules are assumed unital.

# Source Reference
Chapter 10: Introduction to Module Theory, Section 10.1 "Basic Definitions and Examples," pages 337-349. See especially the definition on p. 337 and the examples of Z-modules and F[x]-modules.

# Verification Notes
- Definition: directly quoted from p. 337
- Key properties: synthesized from discussion pp. 337-340
- Confidence: HIGH — explicit definition with extensive examples
- Cross-references: all slugs verified against planned extractions
