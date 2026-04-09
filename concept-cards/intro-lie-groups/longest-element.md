---
# === CORE IDENTIFICATION ===
concept: Longest Element of Weyl Group
slug: longest-element

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
pdf_page: 102
section: "8.7. Simple reflections"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "$w_0$"
  - "longest Weyl group element"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - weyl-group
  - weyl-length
  - positive-weyl-chamber
extends: []
related:
  - reduced-expression
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the longest element of the Weyl group?"
  - "What is $l(w_0)$?"
---

# Quick Definition
The longest element $w_0 \in W$ is the unique element sending the positive Weyl chamber to the negative Weyl chamber: $w_0(C_+) = C_- = -C_+$. Its length is $l(w_0) = |R_+|$, and it is the unique element of maximal length.

# Core Definition
Lemma 8.39 (p. 102): Let $C_- = -C_+$ be the negative Weyl chamber and $w_0 \in W$ the unique element with $w_0(C_+) = C_-$. Then $l(w_0) = |R_+|$ and for any $w \neq w_0$, $l(w) < l(w_0)$.

# Prerequisites
- **weyl-group** -- $w_0$ is an element of $W$
- **weyl-length** -- $w_0$ maximizes the length function
- **positive-weyl-chamber** -- $w_0$ maps $C_+$ to $-C_+$

# Key Properties
1. $w_0(C_+) = -C_+$ (sends positive chamber to negative)
2. $w_0(R_+) = R_-$ (sends all positive roots to negative)
3. $l(w_0) = |R_+|$
4. $w_0$ is unique (by simple transitivity of $W$ on chambers)
5. $w_0^2 = \mathrm{id}$ (since $w_0$ maps $C_-$ back to $C_+$)

# Construction / Recognition
$w_0$ is the unique element with $w_0(\alpha) \in R_-$ for every $\alpha \in R_+$.

# Context & Application
The longest element plays a role in duality: it often relates a representation to its dual. For instance, the highest weight of the dual of an irreducible representation with highest weight $\lambda$ is $-w_0(\lambda)$.

# Examples
**Exercise 8.7** (p. 109): For $A_{n-1}$ with $W = S_n$, the longest element is $w_0 = (n\; n{-}1\; \ldots\; 1)$, i.e., the permutation reversing the order. Its length is $l(w_0) = \binom{n}{2} = |R_+|$.

# Relationships
## Builds Upon
- **weyl-length** -- $w_0$ maximizes it

## Enables
- Duality in representation theory

## Related
- **reduced-expression** -- $w_0$ has the longest reduced expressions

## Contrasts With
(none)

# Common Errors
- **Error**: Thinking $w_0 = -\mathrm{id}$ always
  **Correction**: $w_0 = -\mathrm{id}$ on $E$ only for certain root systems (e.g., $B_n$, $C_n$, $D_{2n}$, $G_2$); for $A_n$ ($n \geq 2$), $w_0 \neq -\mathrm{id}$

# Common Confusions
(none)

# Source Reference
Chapter 8: Root Systems, Section 8.7, page 102. Lemma 8.39, Exercise 8.7.

# Verification Notes
- Definition source: Direct from Lemma 8.39
- Confidence rationale: HIGH -- explicit lemma
- Uncertainties: None
- Cross-reference status: Verified
