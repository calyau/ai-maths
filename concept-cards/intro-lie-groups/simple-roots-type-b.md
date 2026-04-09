---
# === CORE IDENTIFICATION ===
concept: Simple Roots of Type B_n
slug: simple-roots-type-b

# === CLASSIFICATION ===
category: classification
subcategory: type-b
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Appendix C - Root Systems and Simple Lie Algebras"
chapter_number: null
pdf_page: 125
section: "C.2 B_n = so(2n+1,C)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - root-system-type-b
  - simple-roots
extends: []
related:
  - dynkin-diagram-type-b
  - cartan-matrix-type-b
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the simple roots of type B_n?"
---

# Quick Definition
The simple roots of $B_n$ are $\alpha_i = e_i - e_{i+1}$ for $i = 1, \ldots, n-1$ and $\alpha_n = e_n$. The last simple root $\alpha_n$ is a short root.

# Core Definition
(Kirillov, p. 125):

$$\Pi = \{\alpha_1, \ldots, \alpha_n\}, \quad \alpha_1 = e_1 - e_2, \ldots, \alpha_{n-1} = e_{n-1} - e_n, \quad \alpha_n = e_n$$

# Prerequisites
- **Root system type B** -- the roots being organized
- **Simple roots** -- general concept

# Key Properties
1. $\alpha_1, \ldots, \alpha_{n-1}$ are long roots ($(\alpha_i, \alpha_i) = 2$)
2. $\alpha_n = e_n$ is a short root ($(\alpha_n, \alpha_n) = 1$)
3. $(\alpha_{n-1}, \alpha_n) = -1$, giving a double bond in the Dynkin diagram
4. The short root is at the end of the diagram

# Examples
**Example** (p. 125): For $B_2$: $\alpha_1 = e_1 - e_2$ (long), $\alpha_2 = e_2$ (short).

# Relationships
## Builds Upon
- **Root system type B** -- simple roots are a subset of roots

## Enables
- **Dynkin diagram type B** -- has a double bond at the last node
- **Cartan matrix type B** -- computed from these roots

# Source Reference
Appendix C, Section C.2, p. 125.

# Verification Notes
- Definition source: Direct from p. 125
- Confidence rationale: Explicit list
- Uncertainties: None
- Cross-reference status: Verified
