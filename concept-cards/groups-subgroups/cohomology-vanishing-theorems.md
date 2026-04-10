---
# === CORE IDENTIFICATION ===
concept: Cohomology Vanishing Theorems
slug: cohomology-vanishing-theorems

# === CLASSIFICATION ===
category: galois-cohomology
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "The Structure of Reductive Groups: General Case"
chapter_number: 6
pdf_page: 393
section: "The main theorems on the cohomology of groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Hilbert's Theorem 90"
  - "Lang's theorem"
  - "Kneser's theorem"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - galois-cohomology-of-algebraic-groups
extends: []
related:
  - form-of-algebraic-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does Galois cohomology classify forms of algebraic groups?"
  - "What must I know before understanding Galois cohomology of algebraic groups?"
---

# Quick Definition

Key vanishing theorems for Galois cohomology include: $H^1(k, \mathrm{GL}_n) = 1$ (Hilbert 90), $H^1(k, G) = 1$ for connected $G$ over finite $k$ (Lang), and $H^1(k, G) = 1$ for simply connected semisimple $G$ over $p$-adic $k$ (Kneser). The Hasse principle relates local and global cohomology.

# Core Definition

The main theorems (Milne, pp. 388, 393):

- 1.6/1.11: $H^1(\Gamma, \mathrm{GL}_n(K)) = 1$ for all $n$ and all Galois $K/k$ (Hilbert 90 generalized)
- 1.7/1.12: $H^1(k, \mathrm{SL}_n) = 1$
- 1.8/1.13: $H^1(k, \mathrm{Sp}_n) = 1$
- 1.23: If $k$ is finite and $G$ is connected, then $H^1(k, G) = 1$ (Lang's theorem)
- 1.24: If $k$ is $p$-adic and $G$ is simply connected semisimple, then $H^1(k, G) = 1$ (Kneser)
- 1.25a: For $G$ simply connected over $\mathbb{Q}$: $H^1(\mathbb{Q}, G) \simeq H^1(\mathbb{R}, G)$
- 1.25b: For $G$ adjoint or orthogonal over $\mathbb{Q}$: $H^1(\mathbb{Q}, G) \hookrightarrow \prod_p H^1(\mathbb{Q}_p, G)$ (Hasse principle)

# Prerequisites

- **Galois cohomology of algebraic groups** — the framework for these results

# Key Properties

1. Over finite fields, all connected groups have trivial $H^1$
2. Over $p$-adic fields, simply connected semisimple groups have trivial $H^1$
3. Over $\mathbb{Q}$, simply connected semisimple groups satisfy the Hasse principle: global $H^1$ injects into the product of local $H^1$'s
4. The Hasse principle for orthogonal groups implies: two quadratic forms over $\mathbb{Q}$ are isomorphic iff they are isomorphic over all $\mathbb{Q}_p$ (including $\mathbb{R}$)
5. These results extend to finite extensions of $\mathbb{Q}$

# Construction / Recognition

## To Apply:
1. Identify the algebraic group $G$ and the field $k$
2. Check if a vanishing theorem applies (finite field, $p$-adic, simply connected, etc.)
3. Use exact sequences to reduce to known cases
4. For $\mathbb{Q}$: reduce to $H^1(\mathbb{R}, G)$ for simply connected groups

# Context & Application

These theorems are the computational backbone of the classification of forms. They reduce the problem of classifying algebraic groups over number fields to concrete questions about groups over $\mathbb{R}$ and $\mathbb{Q}_p$. The Hasse principle for quadratic forms is a deep result in number theory.

# Examples

**Example 1** (p. 393): The Hasse principle for quadratic forms: $(V, \phi) \cong (V', \phi')$ over $\mathbb{Q}$ iff $(V, \phi) \cong (V', \phi')$ over $\mathbb{Q}_p$ for all $p$ (including $p = \infty$).

**Example 2** (p. 388): $H^1(\Gamma, \mathrm{GL}_n(K)) = 1$ because there is only one $k$-vector space of dimension $n$ (up to isomorphism).

# Relationships

## Builds Upon
- **Galois cohomology of algebraic groups** — the framework

## Enables
- **Form of algebraic group** — vanishing results limit the number of forms

# Common Errors

- **Error**: Applying Kneser's theorem to non-simply connected groups
  **Correction**: $H^1(\mathbb{Q}_p, G) = 1$ requires $G$ to be simply connected

# Common Confusions

- **Confusion**: Thinking the Hasse principle holds for all algebraic groups
  **Clarification**: The Hasse principle is known for adjoint and orthogonal groups, and for simply connected groups it takes the form $H^1(\mathbb{Q}, G) \simeq H^1(\mathbb{R}, G)$, but it fails for general groups

# Source Reference

Chapter VI: The Structure of Reductive Groups: General Case, Sections 1a-1e. Propositions 1.6-1.8, Statements 1.23-1.25.

# Verification Notes

- Definition source: Explicit statements from pp. 388, 393
- Confidence: HIGH — clearly listed theorem statements
- Uncertainties: Proofs reference Kneser 1969, Platonov-Rapinchuk 1994
- Cross-reference status: Verified
