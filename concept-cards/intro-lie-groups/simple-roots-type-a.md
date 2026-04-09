---
# === CORE IDENTIFICATION ===
concept: Simple Roots of Type A_n
slug: simple-roots-type-a

# === CLASSIFICATION ===
category: classification
subcategory: type-a
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Appendix C - Root Systems and Simple Lie Algebras"
chapter_number: null
pdf_page: 123
section: "C.1 A_n = sl(n+1,C)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - root-system-type-a
  - simple-roots
extends: []
related:
  - dynkin-diagram-type-a
  - cartan-matrix-type-a
  - positive-roots-type-a
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the simple roots of type A_n?"
---

# Quick Definition
The simple roots of $A_n$ are $\alpha_i = e_i - e_{i+1}$ for $i = 1, \ldots, n$. The positive roots are $R_+ = \{e_i - e_j \mid i < j\}$.

# Core Definition
(Kirillov, p. 123):

$$\Pi = \{\alpha_1, \ldots, \alpha_n\}, \quad \alpha_i = e_i - e_{i+1}$$

$$R_+ = \{e_i - e_j \mid i < j\}, \quad |R_+| = \frac{n(n+1)}{2}$$

# Prerequisites
- **Root system type A** -- the roots being organized
- **Simple roots** -- general theory

# Key Properties
1. There are $n$ simple roots (rank of $A_n$)
2. Any positive root $e_i - e_j$ ($i < j$) can be written as $\alpha_i + \alpha_{i+1} + \cdots + \alpha_{j-1}$
3. Adjacent simple roots have inner product $(\alpha_i, \alpha_{i+1}) = -1$
4. Non-adjacent simple roots are orthogonal: $(\alpha_i, \alpha_j) = 0$ for $|i - j| > 1$
5. All simple roots have equal length: $(\alpha_i, \alpha_i) = 2$

# Examples
**Example** (p. 123): For $A_2$: $\alpha_1 = e_1 - e_2$, $\alpha_2 = e_2 - e_3$. The third positive root is $\alpha_1 + \alpha_2 = e_1 - e_3$.

# Relationships
## Builds Upon
- **Root system type A** -- the simple roots are a basis for the root system

## Enables
- **Dynkin diagram type A** -- encoded by inner products of simple roots
- **Cartan matrix type A** -- entries computed from simple root pairings

# Source Reference
Appendix C, Section C.1, p. 123.

# Verification Notes
- Definition source: Direct from p. 123
- Confidence rationale: Explicit list
- Uncertainties: None
- Cross-reference status: Verified
