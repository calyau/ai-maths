---
concept: Jordan-Holder Theorem
slug: jordan-holder-theorem
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
aliases: []
prerequisites:
  - composition-series
  - simple-group
extends: []
related:
  - holder-program
contrasts_with: []
answers_questions:
  - "Are composition factors unique?"
  - "What is the Jordan-Holder Theorem?"
---

# Quick Definition
Every finite group has a composition series, and the composition factors (simple quotients) are unique up to permutation and isomorphism. This is the "unique factorization theorem" for groups.

# Core Definition
**Theorem 22 (Jordan-Holder):** Let $G \neq 1$ be a finite group. (1) G has a composition series. (2) If $1 = N_0 \trianglelefteq \cdots \trianglelefteq N_r = G$ and $1 = M_0 \trianglelefteq \cdots \trianglelefteq M_s = G$ are two composition series, then $r = s$ and there is a permutation $\pi$ such that $M_{\pi(i)}/M_{\pi(i)-1} \cong N_i/N_{i-1}$ for all i (Dummit & Foote, pp. 103-104).

# Prerequisites
- **Composition series**, **Simple group**

# Key Properties
1. Existence: every finite group has a composition series
2. Uniqueness: the multiset of composition factors is invariant
3. The series itself need not be unique (only the factors are)
4. Analogous to unique prime factorization for integers

# Context & Application
This theorem justifies the Holder Program's approach of classifying groups through their simple composition factors.

# Examples
**Example 1** (p. 103): $D_8$ has two distinct composition series, both with factors $Z_2, Z_2, Z_2$.

# Relationships
## Builds Upon
- **composition-series**, **simple-group**

## Related
- **holder-program** — motivated by Jordan-Holder

# Source Reference
Chapter 3, Section 3.4, pages 103-104, Theorem 22.

# Verification Notes
- Definition source: direct from source pp. 103-104
- Confidence rationale: major theorem, explicitly stated
- Uncertainties: none
- Cross-reference status: verified
