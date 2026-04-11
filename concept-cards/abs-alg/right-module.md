---
concept: Right Module
slug: right-module
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
  - "right R-module"
prerequisites:
  - ring
  - abelian-group
extends: []
related:
  - left-module
  - bimodule
contrasts_with:
  - left-module
answers_questions:
  - "What is a right module?"
  - "When are left and right modules the same?"
---

# Quick Definition
A right R-module is an abelian group M with an action of R on the right, satisfying axioms analogous to those for left modules but with ring elements written on the right.

# Core Definition
A right R-module can be defined analogously to a left R-module, with ring elements appearing on the right. If R is commutative and M is a left R-module, then M can be made into a right R-module by defining $mr = rm$. If R is not commutative, the associativity axiom will not hold in general with this definition (Dummit & Foote, p. 337).

# Prerequisites
- **ring** — Provides the scalars
- **abelian-group** — The underlying additive structure

# Key Properties
1. For commutative rings, left and right module structures coincide
2. For noncommutative rings, a left module need not be a right module
3. Unless stated otherwise, "module" means "left module" in the text

# Construction / Recognition
1. Start with an abelian group M
2. Define a right action $M \times R \to M$
3. Verify: $m(r+s) = mr + ms$, $m(rs) = (mr)s$, $(m+n)r = mr + nr$, $m \cdot 1 = m$

# Context & Application
Right modules appear naturally in tensor product constructions, where one needs a right R-module and a left R-module to form $M \otimes_R N$.

# Examples
**Example** (p. 337): Any ring R is a right module over itself under right multiplication. The submodules are the right ideals.

# Relationships
## Builds Upon
- **ring**, **abelian-group**

## Related
- **left-module**, **bimodule**

## Contrasts With
- **left-module** — Ring elements act on different sides

# Common Confusions
- **Confusion**: Assuming left and right modules are always interchangeable. **Clarification**: They coincide only when R is commutative.

# Source Reference
Chapter 10, Section 10.1, p. 337.

# Verification Notes
- Definition: adapted from p. 337
- Confidence: HIGH — explicit definition
