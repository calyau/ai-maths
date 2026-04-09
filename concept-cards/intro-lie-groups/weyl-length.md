---
# === CORE IDENTIFICATION ===
concept: Weyl Length
slug: weyl-length

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
pdf_page: 101
section: "8.7. Simple reflections"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "$l(w)$"
  - "length of a Weyl group element"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - weyl-group
  - simple-reflections
  - positive-roots
extends: []
related:
  - reduced-expression
  - longest-element
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the length of a Weyl group element?"
  - "How is length related to reduced expressions?"
---

# Quick Definition
The length $l(w)$ of a Weyl group element $w$ is the number of root hyperplanes separating $C_+$ from $w(C_+)$, equivalently $l(w) = |\{\alpha \in R_+ \mid w(\alpha) \in R_-\}|$. It equals the minimal number of simple reflections needed to express $w$.

# Core Definition
For $w \in W$, the length is defined by (Definition 8.34, equation 8.20, p. 101):

$$l(w) = \text{number of root hyperplanes separating } C_+ \text{ and } w(C_+) = |\{\alpha \in R_+ \mid w(\alpha) \in R_-\}|$$

By Theorem 8.37 (p. 101): $l(w)$ equals the minimal number of simple reflections in any expression $w = s_{i_1}\cdots s_{i_l}$.

# Prerequisites
- **weyl-group** -- the group on which length is defined
- **simple-reflections** -- the generators with respect to which length is measured
- **positive-roots** -- needed for the set $\{\alpha \in R_+ \mid w(\alpha) \in R_-\}$

# Key Properties
1. $l(\mathrm{id}) = 0$
2. $l(s_i) = 1$ for each simple reflection (Example 8.35)
3. $l(w)$ = minimal length of an expression $w = s_{i_1}\cdots s_{i_l}$ (Theorem 8.37)
4. $l(w)$ depends on the choice of polarization
5. $l(w) = |\{\alpha \in R_+ \mid w(\alpha) \in R_-\}|$ (inversions)

# Construction / Recognition
## To compute $l(w)$
1. Count the positive roots sent to negative roots: $l(w) = |\{\alpha \in R_+ \mid w(\alpha) \in R_-\}|$
2. Alternatively, find the shortest expression $w = s_{i_1}\cdots s_{i_l}$

# Context & Application
Length is the key combinatorial invariant of Weyl group elements. It appears in the Weyl character formula (through the sign $(-1)^{l(w)}$), in the Bruhat order, and in Kazhdan-Lusztig theory.

# Examples
**Example 8.35** (p. 101): $l(s_i) = 1$ because $s_i$ sends exactly one positive root ($\alpha_i$) to a negative root ($-\alpha_i$) and permutes the rest.

# Relationships
## Builds Upon
- **simple-reflections** -- generators with length 1

## Enables
- **reduced-expression** -- a product of simple reflections achieving the minimum length
- **longest-element** -- the element of maximum length

## Related
- **positive-weyl-chamber** -- $l(w)$ measures distance from $C_+$ to $w(C_+)$

## Contrasts With
(none)

# Common Errors
- **Error**: Thinking $l(w)$ is the length of any expression, not just the minimal one
  **Correction**: $l(w)$ is defined as the minimum; non-reduced expressions are longer

# Common Confusions
- **Confusion**: Confusing Weyl length with root height
  **Clarification**: Length is defined on $W$; height is defined on roots. They are different concepts.

# Source Reference
Chapter 8: Root Systems, Section 8.7, pages 101--102. Definition 8.34, Example 8.35, Theorem 8.37.

# Verification Notes
- Definition source: Direct from Definition 8.34
- Confidence rationale: HIGH -- explicit definition
- Uncertainties: None
- Cross-reference status: Verified
