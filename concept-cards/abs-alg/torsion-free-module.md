---
concept: Torsion-Free Module
slug: torsion-free-module
category: module-theory
subcategory: modules-over-pids
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Modules over Principal Ideal Domains"
chapter_number: 12
pdf_page: 460
section: "12.1 The Basic Theory"
extraction_confidence: high
aliases:
  - "torsion free"
prerequisites:
  - torsion-module
extends: []
related:
  - free-module
  - flat-module
contrasts_with:
  - torsion-module
answers_questions:
  - "What is a torsion-free module?"
---

# Quick Definition
An R-module M (R an integral domain) is torsion-free if $\text{Tor}(M) = 0$, i.e., $rm = 0$ with $r \neq 0$ implies $m = 0$. Over a PID, finitely generated torsion-free modules are free. Over a PID, torsion-free = flat.

# Core Definition
An R-module M over an integral domain R is torsion-free if $\text{Tor}(M) = \{x \in M \mid rx = 0 \text{ for some nonzero } r \in R\} = 0$. Over a PID: (1) every submodule of a free module is free, (2) finitely generated torsion-free modules are free, (3) torsion-free = flat (Dummit & Foote, pp. 460, 469-471).

# Prerequisites
- **torsion-module** — Torsion-free means no torsion elements

# Key Properties
1. Free modules are torsion-free
2. Over a PID: torsion-free + finitely generated $\Rightarrow$ free
3. Over a PID: torsion-free $\iff$ flat
4. $M/\text{Tor}(M)$ is always torsion-free

# Relationships
## Contrasts With
- **torsion-module** — Torsion-free means the opposite

## Related
- **free-module** — Over PIDs, f.g. torsion-free = free
- **flat-module** — Over PIDs, flat = torsion-free

# Source Reference
Chapter 12, Section 12.1, pp. 460-471.

# Verification Notes
- Confidence: HIGH — standard definition
