---
concept: "Holder Program"
slug: holder-program
category: group-theory
subcategory: structure-theory
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Quotient Groups and Homomorphisms"
chapter_number: 3
pdf_page: 73
section: "3.4 Composition Series and the Holder Program"
extraction_confidence: high
aliases:
  - "Hoelder Program"
prerequisites:
  - composition-series
  - simple-group
extends: []
related:
  - jordan-holder-theorem
  - solvable-group
contrasts_with: []
answers_questions:
  - "What is the Holder program?"
  - "How does one classify finite groups?"
---

# Quick Definition
The Holder Program is a two-part strategy to classify all finite groups: (1) classify all finite simple groups (completed 1980), and (2) find all ways of "putting simple groups together" (the extension problem, still open).

# Core Definition
The *Holder Program* consists of two parts: (1) Classify all finite simple groups. This was completed in 1980 by over 100 mathematicians, yielding 18 infinite families and 26 sporadic groups. (2) Find all ways of assembling groups from simple composition factors (the *extension problem*). This remains extremely difficult; the number of groups of order $2^n$ grows exponentially (Dummit & Foote, pp. 104-107).

# Prerequisites
- **Composition series** — factorization into simple pieces
- **Simple group** — the "atoms" of group theory

# Key Properties
1. Part (1) is complete: the Classification of Finite Simple Groups
2. Part (2) is open and extremely difficult
3. Non-isomorphic groups can have identical composition factors
4. The Feit-Thompson Theorem (255 pages) is a cornerstone: groups of odd order are solvable

# Context & Application
The Holder Program provides the overarching motivation for much of finite group theory. Understanding the extension problem drives the study of group cohomology, semidirect products, and other construction techniques.

# Examples
**Example 1** (p. 106): If $A = B = Z_2$, there are exactly two groups G with $N \cong Z_2$, $G/N \cong Z_2$: namely $Z_4$ and $V_4$.

# Relationships
## Builds Upon
- **composition-series**, **simple-group**

## Related
- **jordan-holder-theorem** — uniqueness of composition factors
- **solvable-group** — groups whose composition factors are all prime-order cyclic

# Source Reference
Chapter 3, Section 3.4, pages 104-107.

# Verification Notes
- Definition source: direct from source pp. 104-105
- Confidence rationale: explicitly stated
- Uncertainties: none
- Cross-reference status: verified
