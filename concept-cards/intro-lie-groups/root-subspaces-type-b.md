---
# === CORE IDENTIFICATION ===
concept: Root Subspaces and Coroots of Type B_n
slug: root-subspaces-type-b

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
pdf_page: 124
section: "C.2 B_n = so(2n+1,C)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - root-system-type-b
  - coroot
extends: []
related:
  - cartan-subalgebra-type-b
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the root subspaces and coroots for type B_n?"
---

# Quick Definition
For type $B_n$, the root subspaces and coroots are explicitly given for each type of root. Notably, the coroot of the short root $e_i$ is $h_{e_i} = 2H_i$ (doubled because the root is short), where $H_i = E_{ii} - E_{i+n,i+n}$.

# Core Definition
(Kirillov, pp. 124-125): Using the alternative description with $H_i = E_{ii} - E_{i+n,i+n}$:
- $\alpha = e_i - e_j$: $\mathfrak{g}_\alpha = \mathbb{C}(E_{ij} - E_{j+n,i+n})$, $h_\alpha = H_i - H_j$
- $\alpha = e_i + e_j$: $\mathfrak{g}_\alpha = \mathbb{C}(E_{i,j+n} - E_{j,i+n})$, $h_\alpha = H_i + H_j$
- $\alpha = e_i$: $\mathfrak{g}_\alpha = \mathbb{C}(E_{i,2n+1} - E_{2n+1,n+i})$, $h_\alpha = 2H_i$
- (and similarly for negative roots)

# Prerequisites
- **Root system type B** -- the roots
- **Coroot** -- general concept

# Key Properties
1. Long root coroots: $h_{e_i \pm e_j} = H_i \pm H_j$
2. Short root coroots: $h_{e_i} = 2H_i$ (the factor of 2 compensates for the shorter root)
3. The doubling for short roots ensures $\langle e_i, h_{e_i} \rangle = 2$

# Source Reference
Appendix C, Section C.2, pp. 124-125.

# Verification Notes
- Definition source: Direct from pp. 124-125
- Confidence rationale: Fully explicit
- Uncertainties: None
- Cross-reference status: Verified
