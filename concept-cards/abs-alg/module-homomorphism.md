---
concept: Module Homomorphism
slug: module-homomorphism
category: module-theory
subcategory: basic-definitions
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Module Theory"
chapter_number: 10
pdf_page: 348
section: "10.2 Quotient Modules and Module Homomorphisms"
extraction_confidence: high
aliases:
  - "R-module homomorphism"
  - "R-linear map"
  - "module map"
prerequisites:
  - left-module
  - group-homomorphism
extends:
  - group-homomorphism
related:
  - module-isomorphism
  - linear-transformation
  - hom-functor
contrasts_with: []
answers_questions:
  - "What is a module homomorphism?"
---

# Quick Definition
An R-module homomorphism $\varphi: M \to N$ is a map of R-modules that preserves both the abelian group structure and the R-action, i.e., $\varphi(rm + m') = r\varphi(m) + \varphi(m')$ for all $r \in R$ and $m, m' \in M$.

# Core Definition
Let M and N be R-modules. An R-module homomorphism from M to N is a map $\varphi: M \to N$ such that $\varphi(rx + y) = r\varphi(x) + \varphi(y)$ for all $r \in R$ and $x, y \in M$. The set of all R-module homomorphisms from M to N is denoted $\text{Hom}_R(M, N)$. When R is commutative, $\text{Hom}_R(M, N)$ is itself an R-module (Dummit & Foote, p. 348).

# Prerequisites
- **left-module** — Homomorphisms are defined between modules
- **group-homomorphism** — A module homomorphism is in particular a group homomorphism

# Key Properties
1. The kernel of a module homomorphism is a submodule
2. The image of a module homomorphism is a submodule
3. $\text{Hom}_R(M, N)$ is an abelian group under pointwise addition
4. When R is commutative, $\text{Hom}_R(M, N)$ is an R-module
5. All isomorphism theorems for groups carry over to modules

# Construction / Recognition
1. Define a map $\varphi: M \to N$ between R-modules
2. Check $\varphi(x + y) = \varphi(x) + \varphi(y)$ for all $x, y \in M$
3. Check $\varphi(rx) = r\varphi(x)$ for all $r \in R$, $x \in M$

# Context & Application
Module homomorphisms are the structure-preserving maps in module theory. When R = F is a field, they are linear transformations. The functor $\text{Hom}_R$ plays a central role in homological algebra.

# Examples
**Example** (p. 349): The natural projection $\pi: M \to M/N$ mapping $m \mapsto m + N$ is an R-module homomorphism with kernel N.

# Relationships
## Builds Upon
- **left-module**, **group-homomorphism**

## Enables
- **exact-sequence** — Defined in terms of kernels and images of homomorphisms
- **projective-module** — Characterized by lifting properties of homomorphisms

## Related
- **linear-transformation** — Module homomorphism when R is a field

# Source Reference
Chapter 10, Section 10.2, pp. 348-350.

# Verification Notes
- Definition: from p. 348
- Confidence: HIGH — standard definition
