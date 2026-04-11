---
concept: Torsion Module
slug: torsion-module
category: module-theory
subcategory: modules-over-pids
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Modules over Principal Ideal Domains"
chapter_number: 12
pdf_page: 456
section: "12.1 The Basic Theory"
extraction_confidence: high
aliases:
  - "torsion submodule"
  - "torsion element"
prerequisites:
  - left-module
extends: []
related:
  - torsion-free-module
  - annihilator
  - structure-theorem-modules-over-pids
contrasts_with:
  - torsion-free-module
  - free-module
answers_questions:
  - "What is a torsion module?"
  - "What is a torsion element?"
---

# Quick Definition
An element m of an R-module M (R an integral domain) is a torsion element if $rm = 0$ for some nonzero $r \in R$. The torsion submodule $\text{Tor}(M)$ is the set of all torsion elements. M is a torsion module if $\text{Tor}(M) = M$.

# Core Definition
If R is an integral domain and M is an R-module, $\text{Tor}(M) = \{x \in M \mid rx = 0 \text{ for some nonzero } r \in R\}$ is a submodule called the torsion submodule. M is torsion if $\text{Tor}(M) = M$ and torsion-free if $\text{Tor}(M) = 0$. Every finite abelian group is a torsion $\mathbb{Z}$-module. The annihilator of a submodule N is $\text{Ann}(N) = \{r \in R \mid rn = 0 \text{ for all } n \in N\}$ (Dummit & Foote, pp. 459-460).

# Prerequisites
- **left-module** — Torsion is a property of modules over integral domains

# Key Properties
1. $\text{Tor}(M)$ is a submodule of M
2. $M/\text{Tor}(M)$ is torsion-free
3. A free module over an integral domain is torsion-free
4. Over a PID, a finitely generated torsion-free module is free
5. A finite dimensional vector space over F, viewed as an F[x]-module, is always a torsion module

# Relationships
## Builds Upon
- **left-module**

## Enables
- **structure-theorem-modules-over-pids** — Decomposes torsion part into cyclic modules

## Contrasts With
- **torsion-free-module** — No nonzero torsion elements
- **free-module** — Free modules are torsion-free

# Source Reference
Chapter 12, Section 12.1, pp. 459-460.

# Verification Notes
- Confidence: HIGH — explicit definitions
