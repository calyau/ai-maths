---
concept: Free Module
slug: free-module
category: module-theory
subcategory: generation
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Module Theory"
chapter_number: 10
pdf_page: 356
section: "10.3 Generation of Modules, Direct Sums, and Free Modules"
extraction_confidence: high
aliases:
  - "free R-module"
prerequisites:
  - left-module
  - direct-sum-of-modules
extends: []
related:
  - projective-module
  - free-abelian-group
  - vector-space
  - rank-of-free-module
contrasts_with:
  - projective-module
answers_questions:
  - "What is a free module?"
  - "What distinguishes a free module from a projective module?"
  - "How do free modules relate to projective modules?"
---

# Quick Definition
An R-module F is free on a subset A if every nonzero element of F can be written uniquely as $r_1 a_1 + r_2 a_2 + \cdots + r_n a_n$ with nonzero $r_i \in R$ and distinct $a_i \in A$. The set A is called a basis of F.

# Core Definition
An R-module F is said to be *free* on the subset A of F if for every nonzero element x of F, there exist unique nonzero elements $r_1, \ldots, r_n$ of R and unique $a_1, \ldots, a_n$ in A such that $x = r_1 a_1 + \cdots + r_n a_n$. The set A is called a *basis* or *set of free generators* for F. If R is commutative, the cardinality of A is called the *rank* of F (Dummit & Foote, p. 356).

# Prerequisites
- **left-module** — Free modules are a special type of module
- **direct-sum-of-modules** — Free modules of finite rank are isomorphic to $R^n$

# Key Properties
1. **Universal property** (Theorem 6): For any R-module M and any map of sets $\varphi: A \to M$, there is a unique R-module homomorphism $\Phi: F(A) \to M$ extending $\varphi$
2. When $A = \{a_1, \ldots, a_n\}$, the free module $F(A) = Ra_1 \oplus \cdots \oplus Ra_n \cong R^n$
3. Over a commutative ring, two free modules of finite rank are isomorphic iff they have the same rank
4. When $R = \mathbb{Z}$, free modules are free abelian groups
5. Over a field, every module is free (i.e., every vector space has a basis)

# Construction / Recognition
## To Construct:
1. Choose a set A
2. Form the collection of all functions $f: A \to R$ with $f(a) = 0$ for all but finitely many $a \in A$
3. Define addition and R-action pointwise

## To Recognize:
1. Check that M has a basis (a set of elements with unique representation property)
2. Equivalently, check that M is isomorphic to a direct sum of copies of R

# Context & Application
Free modules are the module-theoretic analogue of free groups and polynomial rings. They play a central role: every module is a quotient of a free module, and the universal property allows defining homomorphisms by specifying values on a basis.

# Examples
**Example 1** (p. 356): $R^n$ is the free R-module of rank n.
**Example 2** (p. 359): When $R = \mathbb{Z}$, the free module of rank n is $\mathbb{Z}^n$, the free abelian group of rank n.
**Example 3** (p. 356): $\mathbb{Z}/2\mathbb{Z} \oplus \mathbb{Z}/2\mathbb{Z}$ is NOT a free $\mathbb{Z}$-module, because elements do not have unique representations in terms of ring elements.

# Relationships
## Builds Upon
- **left-module**, **direct-sum-of-modules**

## Enables
- **projective-module** — Every free module is projective; projective = direct summand of free
- **tensor-product** — Free modules tensor simply: $S \otimes_R R^n \cong S^n$

## Related
- **vector-space** — Free modules over a field
- **free-abelian-group** — Free $\mathbb{Z}$-modules

## Contrasts With
- **projective-module** — Projective modules are direct summands of free modules, but need not be free

# Common Errors
- **Error**: Confusing the uniqueness in direct sums with uniqueness in free modules. **Correction**: In a direct sum, uniqueness is on module elements; in a free module, uniqueness is on both ring elements and module elements.

# Common Confusions
- **Confusion**: Thinking every projective module is free. **Clarification**: Over a PID (like $\mathbb{Z}$), finitely generated projective modules are free, but this fails for general rings.

# Source Reference
Chapter 10, Section 10.3, pp. 356-360. See especially Theorem 6 (universal property) and Corollary 7.

# Verification Notes
- Definition: direct from p. 356
- Universal property: Theorem 6, p. 357
- Confidence: HIGH — explicit definition with universal property
