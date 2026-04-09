---
# === CORE IDENTIFICATION ===
concept: Root Angles and Length Ratios
slug: root-angles-and-length-ratios

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
pdf_page: 92
section: "8.3. Pairs of roots and rank two root systems"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "allowed angles between roots"
  - "Theorem 8.9"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - abstract-root-system
  - root-system-axioms
extends: []
related:
  - rank-two-root-system-classification
  - dynkin-diagram
  - long-and-short-roots
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What angles can occur between two roots?"
  - "What length ratios are possible between roots?"
---

# Quick Definition
The integrality condition $n_{\alpha\beta}n_{\beta\alpha} = 4\cos^2\varphi \in \{0,1,2,3\}$ restricts the angle $\varphi$ between any two non-proportional roots to exactly seven possibilities, each with a determined length ratio.

# Core Definition
Let $\alpha, \beta \in R$ be non-proportional roots with $|\alpha| \geq |\beta|$ and angle $\varphi$ between them. Then $n_{\alpha\beta}n_{\beta\alpha} = 4\cos^2\varphi$ must be a non-negative integer at most 3. The complete list of possibilities is (Theorem 8.9, p. 93):

1. $\varphi = \pi/2$, $n_{\alpha\beta} = n_{\beta\alpha} = 0$
2. $\varphi = 2\pi/3$, $|\alpha| = |\beta|$, $n_{\alpha\beta} = n_{\beta\alpha} = -1$
3. $\varphi = \pi/3$, $|\alpha| = |\beta|$, $n_{\alpha\beta} = n_{\beta\alpha} = 1$
4. $\varphi = 3\pi/4$, $|\alpha| = \sqrt{2}|\beta|$, $n_{\alpha\beta} = -2$, $n_{\beta\alpha} = -1$
5. $\varphi = \pi/4$, $|\alpha| = \sqrt{2}|\beta|$, $n_{\alpha\beta} = 2$, $n_{\beta\alpha} = 1$
6. $\varphi = 5\pi/6$, $|\alpha| = \sqrt{3}|\beta|$, $n_{\alpha\beta} = 3$, $n_{\beta\alpha} = 1$
7. $\varphi = \pi/6$, $|\alpha| = \sqrt{3}|\beta|$, $n_{\alpha\beta} = -3$, $n_{\beta\alpha} = -1$

# Prerequisites
- **abstract-root-system** -- the integrality axiom R2 drives the constraint
- **root-system-axioms** -- the proof uses $n_{\alpha\beta} \in \mathbb{Z}$

# Key Properties
1. $n_{\alpha\beta}n_{\beta\alpha} = 4\cos^2\varphi \in \{0,1,2,3\}$
2. Possible length ratios: $1$, $\sqrt{2}$, $\sqrt{3}$ (when roots are not orthogonal)
3. If $|\alpha| = |\beta|$, then $n_{\alpha\beta} = n_{\beta\alpha}$
4. If $\cos\varphi \neq 0$, then $n_{\alpha\beta}/n_{\beta\alpha} = |\alpha|^2/|\beta|^2$
5. Each possibility is realized by some rank two root system

# Construction / Recognition
Given two roots $\alpha,\beta$:
1. Compute $n_{\alpha\beta} = 2(\alpha,\beta)/(\beta,\beta)$ and $n_{\beta\alpha} = 2(\alpha,\beta)/(\alpha,\alpha)$
2. Compute $n_{\alpha\beta}n_{\beta\alpha}$; this determines $\cos^2\varphi$
3. The signs of $n_{\alpha\beta}, n_{\beta\alpha}$ determine whether $\varphi$ is acute or obtuse

# Context & Application
This classification of pairs of roots is the key input to classifying rank two root systems, which in turn drives the full classification via Dynkin diagrams. The possible angles ($\pi/2$, $\pi/3$, $2\pi/3$, $\pi/4$, $3\pi/4$, $\pi/6$, $5\pi/6$) correspond to the edge multiplicities 0, 1, 2, 3 in Dynkin diagrams.

# Examples
**Example** (p. 93): The proof uses $n_{\alpha\beta} = 2\frac{|\alpha|}{|\beta|}\cos\varphi$, so $n_{\alpha\beta}n_{\beta\alpha} = 4\cos^2\varphi$. Since this must be a non-negative integer and $\cos^2\varphi \leq 1$ (with equality only for proportional roots), we get $n_{\alpha\beta}n_{\beta\alpha} \in \{0,1,2,3\}$.

# Relationships
## Builds Upon
- **root-system-axioms** -- the integrality constraint

## Enables
- **rank-two-root-system-classification** -- enumerates the four rank two types
- **dynkin-diagram** -- edge multiplicities correspond to these angles
- **cartan-matrix** -- entries are exactly the $n_{\alpha_i\alpha_j}$

## Related
- **long-and-short-roots** -- length ratios determine which roots are long/short

## Contrasts With
(none)

# Common Errors
- **Error**: Forgetting the convention $|\alpha| \geq |\beta|$ and listing redundant cases
  **Correction**: The convention determines which root is in the denominator and fixes the sign pattern

# Common Confusions
- **Confusion**: Thinking all seven angle values can occur between simple roots
  **Clarification**: For simple roots, $(\alpha_i,\alpha_j) \leq 0$ (Lemma 8.15), so only obtuse/right angles ($\pi/2$, $2\pi/3$, $3\pi/4$, $5\pi/6$) occur

# Source Reference
Chapter 8: Root Systems, Section 8.3, pages 92--94. Theorem 8.9.

# Verification Notes
- Definition source: Direct from Theorem 8.9
- Confidence rationale: HIGH -- complete explicit enumeration in source
- Uncertainties: None
- Cross-reference status: Verified
