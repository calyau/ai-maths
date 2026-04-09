---
# === CORE IDENTIFICATION ===
concept: Root Subspaces and Coroots of Type C_n
slug: root-subspaces-type-c

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
pdf_page: 126
section: "C.3 C_n = sp(n,C)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - root-system-type-c
  - coroot
extends: []
related:
  - cartan-subalgebra-type-c
contrasts_with:
  - root-subspaces-type-b

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the root subspaces and coroots for type C_n?"
---

# Quick Definition
For type $C_n$, the root subspaces and coroots differ from $B_n$ in the long roots: the coroot of $2e_i$ (a long root) is $h_{2e_i} = H_i$, while for the short roots $e_i \pm e_j$, the coroots match those of $B_n$.

# Core Definition
(Kirillov, pp. 126-127): With $H_i = E_{ii} - E_{i+n,i+n}$:
- $\alpha = e_i - e_j$: $\mathfrak{g}_\alpha = \mathbb{C}(E_{ij} - E_{j+n,i+n})$, $h_\alpha = H_i - H_j$
- $\alpha = e_i + e_j$: $\mathfrak{g}_\alpha = \mathbb{C}(E_{i,j+n} + E_{j,i+n})$, $h_\alpha = H_i + H_j$
- $\alpha = 2e_i$: $\mathfrak{g}_\alpha = \mathbb{C}E_{i,i+n}$, $h_\alpha = H_i$
- (and similarly for negative roots)

# Prerequisites
- **Root system type C** -- the roots
- **Coroot** -- general concept

# Key Properties
1. Long root coroots: $h_{2e_i} = H_i$ (no factor of 2, since the root is long)
2. Short root coroots: $h_{e_i \pm e_j} = H_i \pm H_j$
3. Note the sign difference from $B_n$: for $e_i + e_j$, $C_n$ has $E_{i,j+n} + E_{j,i+n}$ (plus sign) vs. $B_n$'s $E_{i,j+n} - E_{j,i+n}$ (minus sign)

# Relationships
## Contrasts With
- **Root subspaces type B** -- different signs and coroot scalings reflect the different bilinear forms

# Source Reference
Appendix C, Section C.3, pp. 126-127.

# Verification Notes
- Definition source: Direct from pp. 126-127
- Confidence rationale: Fully explicit
- Uncertainties: None
- Cross-reference status: Verified
