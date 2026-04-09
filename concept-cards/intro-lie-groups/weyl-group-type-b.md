---
# === CORE IDENTIFICATION ===
concept: Weyl Group of Type B_n
slug: weyl-group-type-b

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
aliases:
  - "hyperoctahedral group"
  - "signed permutation group"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - root-system-type-b
  - weyl-group
extends: []
related:
  - weyl-group-type-c
contrasts_with:
  - weyl-group-type-a
  - weyl-group-type-d

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Weyl group of type B_n?"
---

# Quick Definition
The Weyl group of $B_n$ is $W = S_n \ltimes (\mathbb{Z}_2)^n$, the group of all permutations and sign changes of coordinates. It has order $2^n n!$.

# Core Definition
(Kirillov, p. 125): $W = S_n \ltimes (\mathbb{Z}_2)^n$, acting on $E$ by permutations and sign changes of coordinates. Simple reflections: $s_i = (i \;\; i+1)$ for $i = 1, \ldots, n-1$; $s_n: (\lambda_1, \ldots, \lambda_n) \mapsto (\lambda_1, \ldots, -\lambda_n)$.

# Prerequisites
- **Root system type B** -- reflections in roots generate $W$
- **Weyl group** -- general concept

# Key Properties
1. $|W| = 2^n n!$
2. Same as the Weyl group of type $C_n$
3. Includes all permutations and all sign changes (any number)
4. $s_n$ is the sign change of the last coordinate

# Relationships
## Related
- **Weyl group type C** -- same group $S_n \ltimes (\mathbb{Z}_2)^n$

## Contrasts With
- **Weyl group type A** -- only permutations, no sign changes
- **Weyl group type D** -- only even number of sign changes

# Source Reference
Appendix C, Section C.2, p. 125.

# Verification Notes
- Definition source: Direct from p. 125
- Confidence rationale: Explicit
- Uncertainties: None
- Cross-reference status: Verified
