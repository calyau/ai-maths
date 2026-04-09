---
# === CORE IDENTIFICATION ===
concept: Reduced Expression
slug: reduced-expression

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
  - "reduced word"
  - "reduced decomposition"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - simple-reflections
  - weyl-length
extends: []
related:
  - longest-element
  - coxeter-relations
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a reduced expression for a Weyl group element?"
---

# Quick Definition
A reduced expression for $w \in W$ is a product $w = s_{i_1}\cdots s_{i_l}$ of simple reflections with minimal possible length $l = l(w)$. Reduced expressions are generally not unique.

# Core Definition
An expression $w = s_{i_1}\cdots s_{i_l}$ is called reduced if $l$ is minimal (Theorem 8.37, p. 101). By Theorem 8.37, $l = l(w)$, and in a reduced expression, the hyperplanes $L_{\beta_1},\ldots,L_{\beta_l}$ (where $\beta_k = s_{i_1}\cdots s_{i_{k-1}}(\alpha_{i_k})$) crossed in going from $C_+$ to $w(C_+)$ are all distinct.

# Prerequisites
- **simple-reflections** -- the building blocks of the expression
- **weyl-length** -- the minimal length being achieved

# Key Properties
1. Length of a reduced expression equals $l(w)$
2. In a reduced expression, all hyperplanes crossed are distinct (Theorem 8.37)
3. The set of positive roots made negative is $\{\beta_1,\ldots,\beta_l\}$ where $\beta_k = s_{i_1}\cdots s_{i_{k-1}}(\alpha_{i_k})$ (Exercise 8.6)
4. Reduced expressions are generally not unique (different sequences of simple reflections can give the same $w$)

# Construction / Recognition
An expression is reduced if and only if it has the minimal number of factors. One can check this by computing $l(w) = |\{\alpha \in R_+ \mid w(\alpha) \in R_-\}|$ and comparing.

# Context & Application
Reduced expressions provide a canonical way to decompose Weyl group elements. They appear in Bruhat decomposition, in the definition of Schubert cells, and in computing the action of $W$ on representations.

# Examples
**Example**: In $S_3 = W(A_2)$, the element $(132)$ can be written as $s_1 s_2$ (reduced, length 2) but also as $s_2 s_1 s_2 s_1$ (non-reduced, length 4).

# Relationships
## Builds Upon
- **simple-reflections**, **weyl-length**

## Enables
- Understanding Weyl group structure

## Related
- **coxeter-relations** -- relate different reduced expressions
- **longest-element** -- has the longest reduced expressions

## Contrasts With
(none)

# Common Errors
- **Error**: Assuming reduced expressions are unique
  **Correction**: They are generally not; different reduced expressions for the same $w$ are related by braid/Coxeter relations

# Common Confusions
(none)

# Source Reference
Chapter 8: Root Systems, Section 8.7, pages 101--102. Theorem 8.37, Exercise 8.6.

# Verification Notes
- Definition source: Direct from Theorem 8.37
- Confidence rationale: HIGH -- explicit definition
- Uncertainties: None
- Cross-reference status: Verified
