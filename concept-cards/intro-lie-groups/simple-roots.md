---
# === CORE IDENTIFICATION ===
concept: Simple Roots
slug: simple-roots

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
  - "$\\Pi$"
  - "system of simple roots"
  - "basis of simple roots"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - positive-roots
  - polarization
extends: []
related:
  - height-function
  - cartan-matrix
  - dynkin-diagram
  - simple-reflections
contrasts_with:
  - positive-roots

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes simple roots from positive roots?"
  - "How many simple roots are there?"
  - "What properties do simple roots have?"
---

# Quick Definition
A simple root is a positive root that cannot be written as a sum of two positive roots. The set of simple roots $\Pi = \{\alpha_1,\ldots,\alpha_r\}$ forms a basis of $E$, and every root is an integer combination of simple roots.

# Core Definition
A root $\alpha \in R_+$ is called simple if it cannot be written as a sum of two positive roots (Definition 8.12, p. 94). The set of simple roots is denoted $\Pi \subset R_+$.

**Theorem 8.16** (p. 95): The simple roots form a basis of $E$. Thus $|\Pi| = r = \operatorname{rank}(R)$.

**Corollary 8.18** (p. 95): Every $\alpha \in R$ can be uniquely written as $\alpha = \sum n_i\alpha_i$ with $n_i \in \mathbb{Z}$, where all $n_i \geq 0$ if $\alpha \in R_+$ and all $n_i \leq 0$ if $\alpha \in R_-$.

# Prerequisites
- **positive-roots** -- simple roots are a subset of positive roots
- **polarization** -- positive roots require a polarization

# Key Properties
1. $|\Pi| = r = \dim E = \operatorname{rank}(R)$ (Theorem 8.16)
2. $\Pi$ is a basis of $E$
3. For distinct simple roots $\alpha_i, \alpha_j$: $(\alpha_i,\alpha_j) \leq 0$ (Lemma 8.15, p. 95)
4. Every positive root is a sum of simple roots with non-negative integer coefficients (Lemma 8.13)
5. Simple roots are exactly the positive roots of height 1
6. $R$ can be recovered from $\Pi$: $R = W(\Pi)$ (Corollary 8.33)
7. Different polarizations give Weyl-conjugate sets $\Pi$: $\Pi' = w(\Pi)$ for some $w \in W$ (Corollary 8.29)

# Construction / Recognition
## To find simple roots from $R_+$
1. A positive root $\alpha$ is simple if and only if it cannot be written as $\alpha = \beta + \gamma$ with $\beta,\gamma \in R_+$
2. Equivalently, simple roots are the positive roots of height 1

## To recover $R$ from $\Pi$
1. Generate $W$ from simple reflections $s_{\alpha_i}$
2. Apply $W$ to $\Pi$: $R = W(\Pi)$ (Corollary 8.33)

# Context & Application
Simple roots are the minimal generating data for a root system. The Cartan matrix and Dynkin diagram encode only the relationships between simple roots, yet these determine the entire root system up to isomorphism. This makes simple roots the key to the classification.

# Examples
**Example 8.14** (p. 95): For $A_2$ with $t$ chosen appropriately, $\alpha_1$ and $\alpha_2$ are simple roots and $\alpha_1 + \alpha_2$ is the third positive root (not simple).

**Example 8.19** (p. 96): For $A_{n-1}$, the simple roots are $\alpha_i = e_i - e_{i+1}$ for $i = 1,\ldots,n-1$.

# Relationships
## Builds Upon
- **positive-roots** -- simple roots are the indecomposable positive roots

## Enables
- **cartan-matrix** -- defined from the inner products of simple roots
- **dynkin-diagram** -- encodes the simple root geometry
- **simple-reflections** -- the reflections $s_{\alpha_i}$, which generate $W$
- **height-function** -- measures decomposition into simple roots

## Related
- **weyl-group** -- $R = W(\Pi)$

## Contrasts With
- **positive-roots** -- simple roots are a proper subset of $R_+$ (except in rank 1)

# Common Errors
- **Error**: Attempting to decompose simple roots into sums of other roots
  **Correction**: Simple roots are by definition indecomposable in $R_+$

# Common Confusions
- **Confusion**: Thinking simple roots depend only on the root system (not on the polarization)
  **Clarification**: Simple roots depend on the choice of polarization, but different choices give $W$-conjugate results

# Source Reference
Chapter 8: Root Systems, Section 8.4, pages 94--96. Definition 8.12, Lemma 8.13, Lemma 8.15, Theorem 8.16, Corollary 8.18.

# Verification Notes
- Definition source: Direct from Definition 8.12
- Confidence rationale: HIGH -- explicit definition with detailed theorems
- Uncertainties: None
- Cross-reference status: Verified
