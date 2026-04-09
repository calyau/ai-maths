---
# === CORE IDENTIFICATION ===
concept: Positive Roots
slug: positive-roots

# === CLASSIFICATION ===
category: root-systems
subcategory: simple-positive-roots
tier: foundational

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Root Systems"
chapter_number: 8
pdf_page: 94
section: "8.4. Positive roots and simple roots"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "$R_+$"
  - "positive root system"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - abstract-root-system
  - polarization
extends: []
related:
  - simple-roots
  - height-function
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are positive roots?"
  - "What distinguishes simple roots from positive roots?"
---

# Quick Definition
The positive roots $R_+$ are the roots on one side of a hyperplane determined by a regular element $t$: $R_+ = \{\alpha \in R \mid (\alpha,t) > 0\}$. Every positive root is a sum of simple roots with non-negative integer coefficients.

# Core Definition
Given a polarization determined by a regular element $t$, the positive roots are $R_+ = \{\alpha \in R \mid (\alpha,t) > 0\}$ (equation 8.6, p. 94). The negative roots are $R_- = -R_+$, and $R = R_+ \sqcup R_-$.

By Corollary 8.18 (p. 95), every $\alpha \in R_+$ can be uniquely written as $\alpha = \sum_{i=1}^r n_i\alpha_i$ with $n_i \in \mathbb{Z}_{\geq 0}$, where $\{\alpha_1,\ldots,\alpha_r\} = \Pi$ are the simple roots.

# Prerequisites
- **abstract-root-system** -- the root system being decomposed
- **polarization** -- determines which roots are positive

# Key Properties
1. $R_- = -R_+$
2. $|R_+| = |R|/2$
3. Every positive root is a non-negative integer combination of simple roots (Corollary 8.18)
4. Every positive root can be written as a sum of simple roots (Lemma 8.13)
5. The simple root $\alpha_i$ has $s_i(\alpha_i) = -\alpha_i \in R_-$, and $s_i$ permutes $R_+ \setminus \{\alpha_i\}$ (Example 8.35)

# Construction / Recognition
1. Choose a regular element $t$ (or equivalently a Weyl chamber)
2. $R_+ = \{\alpha \in R \mid (\alpha,t) > 0\}$
3. Alternatively, given simple roots, $R_+$ consists of all roots with non-negative coefficients in the simple root basis

# Context & Application
Positive roots provide the first reduction in describing a root system. The corresponding root subspaces $\mathfrak{g}_\alpha$ for $\alpha \in R_+$ span the nilpotent subalgebra $\mathfrak{n}_+$ in the triangular decomposition $\mathfrak{g} = \mathfrak{n}_- \oplus \mathfrak{h} \oplus \mathfrak{n}_+$.

# Examples
**Example 8.19** (p. 96): For $A_{n-1}$, $R_+ = \{e_i - e_j \mid i < j\}$. These correspond to the strictly upper-triangular matrix entries in $\mathfrak{sl}(n,\mathbb{C})$.

**Example 8.14** (p. 95): For $A_2$, there are three positive roots: $\alpha_1$, $\alpha_2$, and $\alpha_1 + \alpha_2$.

# Relationships
## Builds Upon
- **polarization** -- determines $R_+$

## Enables
- **simple-roots** -- the indecomposable elements of $R_+$
- **height-function** -- sums the simple root coefficients

## Related
- **weyl-chamber** -- in bijection with polarizations

## Contrasts With
(none)

# Common Errors
- **Error**: Thinking the positive roots are intrinsic to $R$ (no choice needed)
  **Correction**: Positive roots depend on the choice of polarization (i.e., Weyl chamber)

# Common Confusions
- **Confusion**: Thinking every positive root is a simple root
  **Clarification**: Simple roots are the positive roots that cannot be decomposed as sums of two positive roots; most positive roots are not simple

# Source Reference
Chapter 8: Root Systems, Section 8.4, pages 94--96. Equation (8.6), Lemma 8.13, Corollary 8.18.

# Verification Notes
- Definition source: Direct from equation (8.6)
- Confidence rationale: HIGH -- explicit definition
- Uncertainties: None
- Cross-reference status: Verified
