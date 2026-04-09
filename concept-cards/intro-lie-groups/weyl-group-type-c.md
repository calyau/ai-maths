---
# === CORE IDENTIFICATION ===
concept: Weyl Group of Type C_n
slug: weyl-group-type-c

# === CLASSIFICATION ===
category: classification
subcategory: type-c
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Appendix C - Root Systems and Simple Lie Algebras"
chapter_number: null
pdf_page: 127
section: "C.3 C_n = sp(n,C)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - root-system-type-c
  - weyl-group
extends: []
related:
  - weyl-group-type-b
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Weyl group of type C_n?"
---

# Quick Definition
The Weyl group of $C_n$ is $W = S_n \ltimes (\mathbb{Z}_2)^n$, the same as for $B_n$: all permutations and sign changes of coordinates, with order $2^n n!$.

# Core Definition
(Kirillov, p. 127): $W = S_n \ltimes (\mathbb{Z}_2)^n$, acting on $E$ by permutations and sign changes. Simple reflections: $s_i = (i \;\; i+1)$ for $i = 1, \ldots, n-1$; $s_n: (\lambda_1, \ldots, \lambda_n) \mapsto (\lambda_1, \ldots, -\lambda_n)$.

# Prerequisites
- **Root system type C** -- generates the Weyl group
- **Weyl group** -- general concept

# Key Properties
1. Identical to the Weyl group of $B_n$: $|W| = 2^n n!$
2. Despite different root systems, $B_n$ and $C_n$ have the same Weyl group

# Relationships
## Related
- **Weyl group type B** -- same group

# Source Reference
Appendix C, Section C.3, p. 127.

# Verification Notes
- Definition source: Direct from p. 127
- Confidence rationale: Explicit
- Uncertainties: None
- Cross-reference status: Verified
