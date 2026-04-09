---
# === CORE IDENTIFICATION ===
concept: Root Addition Lemma
slug: root-addition-lemma

# === CLASSIFICATION ===
category: root-systems
subcategory: abstract-root-systems
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Root Systems"
chapter_number: 8
pdf_page: 94
section: "8.3. Pairs of roots and rank two root systems"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Lemma 8.11"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - abstract-root-system
  - rank-two-root-system-classification
extends: []
related:
  - simple-roots
  - positive-roots
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When is the sum of two roots also a root?"
---

# Quick Definition
If $\alpha,\beta \in R$ are roots with $(\alpha,\beta) < 0$ and $\alpha \neq c\beta$, then $\alpha + \beta \in R$. This provides a sufficient condition for root addition.

# Core Definition
Lemma 8.11 (p. 94): Let $\alpha,\beta \in R$ be two roots such that $(\alpha,\beta) < 0$ and $\alpha \neq c\beta$. Then $\alpha + \beta \in R$.

The proof reduces to checking each rank two root system directly (Theorem 8.10).

# Prerequisites
- **abstract-root-system** -- the setting for the lemma
- **rank-two-root-system-classification** -- the proof is case-by-case over rank two types

# Key Properties
1. The condition $(\alpha,\beta) < 0$ means the angle between $\alpha$ and $\beta$ is obtuse
2. The condition $\alpha \neq c\beta$ excludes proportional roots
3. This lemma is used in proving properties of simple roots (Lemma 8.15)

# Construction / Recognition
To apply the lemma: check that $(\alpha,\beta) < 0$ and $\alpha,\beta$ are not proportional; then conclude $\alpha+\beta \in R$.

# Context & Application
This lemma is a key technical tool used repeatedly in the theory. It is used in the proof that simple roots have non-positive inner products (Lemma 8.15) and in the proof that the Lie algebra can be recovered from generators (Lemma 8.53).

# Examples
**Example**: In $A_2$ with positive roots $\alpha_1, \alpha_2, \alpha_1+\alpha_2$: since $(\alpha_1,\alpha_2) < 0$ (angle $2\pi/3$), the lemma guarantees $\alpha_1 + \alpha_2 \in R$.

# Relationships
## Builds Upon
- **rank-two-root-system-classification** -- proof is by checking each case

## Enables
- **simple-roots** -- used in proving Lemma 8.15 ($(\alpha_i,\alpha_j) \leq 0$ for simple roots)

## Related
- **positive-roots**

## Contrasts With
(none)

# Common Errors
- **Error**: Omitting the condition $\alpha \neq c\beta$
  **Correction**: Without this condition, $\alpha = -\beta$ gives $\alpha+\beta = 0 \notin R$

# Common Confusions
- **Confusion**: Thinking $(\alpha,\beta) < 0$ is necessary for $\alpha+\beta \in R$
  **Clarification**: The lemma gives a sufficient condition only; $\alpha+\beta$ can be a root even when $(\alpha,\beta) \geq 0$

# Source Reference
Chapter 8: Root Systems, Section 8.3, page 94. Lemma 8.11.

# Verification Notes
- Definition source: Direct from Lemma 8.11
- Confidence rationale: HIGH -- explicit lemma statement
- Uncertainties: None
- Cross-reference status: Verified
