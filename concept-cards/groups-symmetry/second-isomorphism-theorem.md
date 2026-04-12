---
# === CORE IDENTIFICATION ===
concept: Second Isomorphism Theorem
slug: second-isomorphism-theorem

# === CLASSIFICATION ===
category: homomorphisms
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Homomorphisms"
chapter_number: 16
pdf_page: 93
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "diamond isomorphism theorem"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - first-isomorphism-theorem
  - normal-subgroup
extends:
  - first-isomorphism-theorem
related:
  - third-isomorphism-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Second Isomorphism Theorem?"
  - "How do two subgroups interact to produce an isomorphism?"
---

# Quick Definition

If $H$ and $J$ are subgroups of $G$ with $J$ normal in $G$, then $HJ$ is a subgroup of $G$, $H \cap J$ is normal in $H$, and $HJ/J \cong H/(H \cap J)$.

# Core Definition

**(16.4) Second Isomorphism Theorem.** Suppose $H, J$ are subgroups of $G$ with $J$ normal in $G$. Then $HJ$ is a subgroup of $G$, $H \cap J$ is a normal subgroup of $H$, and the quotient groups $HJ/J$ and $H/(H \cap J)$ are isomorphic (Armstrong, Ch. 16, p. 95).

**Proof.** $HJ$ is a subgroup (using normality of $J$ for the key step $xyy_*^{-1}x_*^{-1} = (xx_*^{-1})(x_*yy_*^{-1}x_*^{-1}) \in HJ$). The homomorphism $\varphi: H \to HJ/J$, $\varphi(x) = xJ$ is surjective (if $g = xy \in HJ$ then $\varphi(x) = xJ = xyJ = gJ$). The kernel is $H \cap J$. Apply the First Isomorphism Theorem.

# Prerequisites

- **First isomorphism theorem** — The proof applies it
- **Normal subgroup** — $J$ must be normal in $G$

# Key Properties

1. $HJ$ is a subgroup of $G$ (requires $J \triangleleft G$)
2. $H \cap J \triangleleft H$
3. $HJ/J \cong H/(H \cap J)$
4. The isomorphism is induced by $x \mapsto xJ$

# Construction / Recognition

## To Apply:
1. Identify subgroups $H$ and $J$ of $G$ with $J \triangleleft G$
2. Form $HJ$ and $H \cap J$
3. Conclude $HJ/J \cong H/(H \cap J)$

# Context & Application

The Second Isomorphism Theorem is one of three fundamental isomorphism theorems that Armstrong derives from the First. It relates the intersection and product of two subgroups.

# Examples

The theorem is stated and proved but Armstrong does not give a worked example in the text. It is used implicitly in later developments.

# Relationships

## Builds Upon
- **First isomorphism theorem** — Applied in the proof

## Related
- **Third isomorphism theorem** — The other generalisation

# Common Errors

- **Error**: Forgetting the hypothesis that $J$ is normal in $G$
  **Correction**: Without normality of $J$, $HJ$ need not be a subgroup and $HJ/J$ is not defined

# Common Confusions

- **Confusion**: Thinking $H$ must also be normal
  **Clarification**: Only $J$ needs to be normal in $G$. $H$ can be any subgroup.

# Source Reference

Chapter 16: Homomorphisms, Theorem (16.4), pp. 95-96 (pdf).

# Verification Notes

- Definition source: Direct from Theorem (16.4)
- Confidence rationale: HIGH — explicit theorem with proof
- Uncertainties: None
