---
# === CORE IDENTIFICATION ===
concept: Transitive Weyl Action on Chambers
slug: transitive-weyl-action-on-chambers

# === CLASSIFICATION ===
category: root-systems
subcategory: weyl-group
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Root Systems"
chapter_number: 8
pdf_page: 99
section: "8.6. Weyl chambers"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Theorem 8.25"
  - "simply transitive Weyl action"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - weyl-group
  - weyl-chamber
extends: []
related:
  - simple-reflections
  - weyl-length
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the Weyl group act on Weyl chambers?"
  - "Is the Weyl group action on chambers free?"
---

# Quick Definition
The Weyl group acts simply transitively on the set of Weyl chambers: for any two chambers $C, C'$ there exists a unique $w \in W$ with $C' = w(C)$. In particular, the number of chambers equals $|W|$.

# Core Definition
**Theorem 8.25** (p. 99): The Weyl group acts transitively on the set of Weyl chambers.

**Corollary 8.38** (p. 102): The action is simply transitive (if $w(C_+) = C_+$ then $w = \mathrm{id}$, since $l(w) = 0$).

# Prerequisites
- **weyl-group** -- the group acting
- **weyl-chamber** -- the objects being acted upon

# Key Properties
1. Transitivity: every chamber is $w(C_+)$ for some $w$ (Theorem 8.25)
2. Simple transitivity: the $w$ is unique (Corollary 8.38)
3. Number of Weyl chambers $= |W|$
4. The proof uses that any two chambers can be connected by adjacent chambers (Lemma 8.26) and adjacent chambers are related by reflections (Lemma 8.27)

# Construction / Recognition
Given chambers $C, C'$: connect them by a chain of adjacent chambers $C = C_0, C_1, \ldots, C_l = C'$. Then $C' = s_{\beta_l}\cdots s_{\beta_1}(C)$ where $L_{\beta_k}$ separates $C_{k-1}$ from $C_k$ (equation 8.18, p. 99).

# Context & Application
This theorem is foundational: it implies that different polarizations give $W$-conjugate simple root systems (Corollary 8.29), which ensures the classification of root systems is independent of the choice of polarization.

# Examples
**Example**: For $A_2$, $|W| = |S_3| = 6$, and there are exactly 6 Weyl chambers, one for each permutation.

# Relationships
## Builds Upon
- **weyl-group**, **weyl-chamber**

## Enables
- The classification being independent of polarization (Corollary 8.29)
- **weyl-length** -- well-defined because the chamber $w(C_+)$ uniquely determines $w$

## Related
- **simple-reflections** -- generate the connecting elements

## Contrasts With
(none)

# Common Errors
(none)

# Common Confusions
(none)

# Source Reference
Chapter 8: Root Systems, Section 8.6, pages 99--100. Theorem 8.25, Lemmas 8.26--8.27, Corollary 8.38.

# Verification Notes
- Definition source: Direct from Theorem 8.25 and Corollary 8.38
- Confidence rationale: HIGH -- explicit theorems
- Uncertainties: None
- Cross-reference status: Verified
