---
# === CORE IDENTIFICATION ===
concept: Classification of Bilinear Forms by Cohomology
slug: classifying-bilinear-forms

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
pdf_page: 386
section: "Classifying bilinear forms"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - noncommutative-galois-cohomology
  - one-cocycle
  - semilinear-action
extends: []
related:
  - form-of-algebraic-group
  - galois-cohomology-of-algebraic-groups
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does Galois cohomology classify forms of algebraic groups?"
---

# Quick Definition

Bilinear forms over $k$ that become isomorphic to a given form $(V_0, \phi_0)$ over a Galois extension $K$ are classified by the cohomology set $H^1(\Gamma, \mathcal{A}(K))$, where $\mathcal{A}(K)$ is the automorphism group of $(V_0, \phi_0)_K$.

# Core Definition

Theorem 1.5 (Milne, p. 386): Let $(V_0, \phi_0)$ be a $k$-vector space with bilinear form, $K/k$ a finite Galois extension with group $\Gamma$, and $\mathcal{A}(K)$ the automorphism group of $(V_0, \phi_0)_K$. "The cohomology set $H^1(\Gamma, \mathcal{A}(K))$ classifies the isomorphism classes of pairs $(V, \phi)$ over $k$ that become isomorphic to $(V_0, \phi_0)$ over $K$."

# Prerequisites

- **Noncommutative Galois cohomology** — the classifying set $H^1$
- **1-cocycle** — the transition data
- **Semilinear action** — used in the proof via Galois descent

# Key Properties

1. The bijection is given by $(V, \phi) \mapsto \text{class of } (f^{-1} \circ \sigma f)$ for any isomorphism $f: (V_0, \phi_0)_K \to (V, \phi)_K$
2. Surjectivity is proved by twisting: a cocycle defines a new semilinear action, whose fixed space gives a new form
3. For $\phi_0 = 0$ (no form), this gives $H^1(\Gamma, \mathrm{GL}_n(K))$, which is trivial (Proposition 1.6)
4. For alternating forms, $H^1(\Gamma, \mathrm{Sp}(K)) = 1$ (all alternating forms of the same rank are isomorphic)
5. For symmetric forms, $H^1(\Gamma, \mathrm{O}(K))$ can be very large

# Construction / Recognition

## To Classify Forms:
1. Fix a reference form $(V_0, \phi_0)$ over $k$
2. For each form $(V, \phi)$ isomorphic to $(V_0, \phi_0)$ over $K$, choose $f: (V_0, \phi_0)_K \xrightarrow{\sim} (V, \phi)_K$
3. Compute the cocycle $a_\sigma = f^{-1} \circ \sigma f \in \mathcal{A}(K)$
4. The class of $(a_\sigma)$ in $H^1(\Gamma, \mathcal{A}(K))$ is independent of the choice of $f$

# Context & Application

This theorem is the prototype for the classification of algebraic objects by Galois cohomology. The same technique generalizes to classify forms of algebraic groups (Theorem 1.10), algebras, and other algebraic structures.

# Examples

**Example 1** (p. 388): $H^1(\Gamma, \mathrm{GL}_n(K)) = 1$ because all $k$-vector spaces of dimension $n$ are isomorphic.

**Example 2** (p. 388): $H^1(\Gamma, \mathrm{Sp}(K)) = 1$ because all nondegenerate alternating forms of the same dimension are isomorphic.

**Example 3** (p. 388): $H^1(\Gamma, \mathrm{O}(K))$ classifies quadratic spaces over $k$ of a given dimension; this can be a very large set (Remark 1.9).

# Relationships

## Builds Upon
- **Noncommutative Galois cohomology** — the classification uses $H^1$
- **Semilinear action** — used in the proof (Galois descent)

## Enables
- **Form of algebraic group** — the same technique classifies forms of groups (Theorem 1.10)
- **Galois cohomology of algebraic groups** — the bilinear form case motivates the general theory

# Common Errors

- **Error**: Forgetting that the automorphism group $\mathcal{A}(K)$ is the group of form-preserving automorphisms, not all automorphisms
  **Correction**: $\mathcal{A}(K) = \{\alpha \in \mathrm{GL}(V_{0K}) \mid \phi_{0K}(\alpha x, \alpha y) = \phi_{0K}(x,y)\}$

# Common Confusions

- **Confusion**: Thinking $H^1 = 1$ means there is only one bilinear form
  **Clarification**: $H^1(\Gamma, \mathcal{A}(K)) = 1$ means there is only one form *that becomes isomorphic to $(V_0, \phi_0)$ over $K$*. Different forms may exist that are not isomorphic even over $K$.

# Source Reference

Chapter VI: The Structure of Reductive Groups: General Case, Section 1b, pages 385-388. Theorem 1.5, Propositions 1.6-1.8, Remark 1.9.

# Verification Notes

- Definition source: Theorem 1.5 directly from p. 386
- Confidence: HIGH — explicit theorem with full proof
- Uncertainties: None
- Cross-reference status: Verified
