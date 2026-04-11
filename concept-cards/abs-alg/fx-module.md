---
concept: F[x]-Module
slug: fx-module
category: module-theory
subcategory: basic-definitions
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Module Theory"
chapter_number: 10
pdf_page: 340
section: "10.1 Basic Definitions and Examples"
extraction_confidence: high
aliases:
  - "polynomial module"
  - "module over polynomial ring"
prerequisites:
  - left-module
  - vector-space
  - linear-transformation
  - polynomial-ring
extends:
  - left-module
related:
  - rational-canonical-form
  - jordan-canonical-form
  - t-stable-subspace
contrasts_with: []
answers_questions:
  - "How are F[x]-modules related to linear transformations?"
  - "What must I know before understanding canonical forms?"
---

# Quick Definition
An F[x]-module is a vector space V over a field F together with a linear transformation $T: V \to V$, where the indeterminate x acts as T. F[x]-modules provide the framework for canonical forms of matrices.

# Core Definition
Let F be a field, let V be a vector space over F, and let $T: V \to V$ be a linear transformation. Make V into an F[x]-module by defining the action of a polynomial $p(x) = a_n x^n + \cdots + a_1 x + a_0$ on $v \in V$ by $p(x)v = a_n T^n(v) + \cdots + a_1 T(v) + a_0 v$. This gives a bijection between F[x]-modules and pairs (V, T) of a vector space with a linear transformation. The F[x]-submodules of V are precisely the T-stable subspaces (Dummit & Foote, pp. 340-342).

# Prerequisites
- **left-module** — F[x]-modules are a special case
- **vector-space** — The underlying structure
- **linear-transformation** — Specifies the action of x
- **polynomial-ring** — F[x] is the ring of scalars

# Key Properties
1. There is a bijection: {F[x]-modules} $\leftrightarrow$ {pairs (V, T) where V is a vector space over F and T: V $\to$ V is linear}
2. The element x acts on V as the linear transformation T
3. F[x]-submodules are precisely the T-stable (T-invariant) subspaces
4. The F[x]-module structure depends on the choice of T
5. Since F[x] is a PID, finitely generated F[x]-modules have nice structure (canonical forms)

# Construction / Recognition
## To Construct:
1. Start with a vector space V over F
2. Choose a linear transformation $T: V \to V$
3. Define the action of x on V as T, extend to all of F[x] by linearity

## To Recognize:
1. An F[x]-module is an F-vector space with a distinguished linear endomorphism

# Context & Application
F[x]-modules form the basis for the theory of rational canonical form and Jordan canonical form in Chapter 12. The relatively simple ideal structure of F[x] (as a PID) forces F[x]-module structure to be correspondingly uncomplicated, providing matrix representations for linear transformations.

# Examples
**Example 1** (p. 341): If T = 0, then $p(x)v = a_0 v$, so the F[x]-module structure reduces to the F-module structure.

**Example 2** (p. 341): If T is the shift operator on $F^n$ given by $T(x_1, \ldots, x_n) = (x_2, \ldots, x_n, 0)$, the subspaces $U_k = \{(x_1, \ldots, x_k, 0, \ldots, 0)\}$ are T-stable, hence F[x]-submodules.

# Relationships
## Builds Upon
- **left-module**, **vector-space**, **polynomial-ring**

## Enables
- **rational-canonical-form** — Classification of F[x]-modules gives rational canonical form
- **jordan-canonical-form** — Further decomposition over algebraically closed fields

## Related
- **t-stable-subspace** — The submodules of an F[x]-module

# Common Confusions
- **Confusion**: Thinking the F[x]-module structure on V is unique. **Clarification**: Different choices of T give different F[x]-module structures on the same vector space V.

# Source Reference
Chapter 10, Section 10.1, pp. 340-343.

# Verification Notes
- Definition: direct from pp. 340-341
- Bijection: explicitly stated on p. 342
- Confidence: HIGH — detailed development with examples
