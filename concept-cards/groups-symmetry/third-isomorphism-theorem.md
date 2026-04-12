---
# === CORE IDENTIFICATION ===
concept: Third Isomorphism Theorem
slug: third-isomorphism-theorem

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
  - "correspondence theorem (partial)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - first-isomorphism-theorem
  - normal-subgroup
  - quotient-group
extends:
  - first-isomorphism-theorem
related:
  - second-isomorphism-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Third Isomorphism Theorem?"
  - "How do nested normal subgroups give isomorphisms?"
---

# Quick Definition

If $H \subseteq J$ are both normal subgroups of $G$, then $J/H$ is normal in $G/H$ and $(G/H)/(J/H) \cong G/J$.

# Core Definition

**(16.5) Third Isomorphism Theorem.** Let $H, J$ be normal subgroups of $G$ and suppose $H$ is contained in $J$. Then $J/H$ is a normal subgroup of $G/H$ and the quotient group $(G/H)/(J/H)$ is isomorphic to $G/J$ (Armstrong, Ch. 16, p. 96).

**Proof.** The function $\varphi: G/H \to G/J$ defined by $\varphi(xH) = xJ$ is a surjective homomorphism. Its kernel is $J/H$. Apply the First Isomorphism Theorem.

# Prerequisites

- **First isomorphism theorem** — Applied in the proof
- **Normal subgroup** — Both $H$ and $J$ must be normal
- **Quotient group** — Multiple quotients appear

# Key Properties

1. $J/H \triangleleft G/H$
2. $(G/H)/(J/H) \cong G/J$
3. Informally: "you can cancel the $H$'s"
4. The map $xH \mapsto xJ$ is the natural surjection

# Construction / Recognition

## To Apply:
1. Identify $H \subseteq J$ both normal in $G$
2. Form the quotients $G/H$, $G/J$, $J/H$
3. Conclude $(G/H)/(J/H) \cong G/J$

# Context & Application

The Third Isomorphism Theorem shows that taking successive quotients can be done in one step. It is particularly useful when analysing towers of normal subgroups (composition series).

# Examples

**Example 1**: If $G = \mathbb{Z}$, $H = 6\mathbb{Z}$, $J = 2\mathbb{Z}$: $(G/H)/(J/H) = (\mathbb{Z}/6\mathbb{Z})/(2\mathbb{Z}/6\mathbb{Z}) \cong \mathbb{Z}_6/\mathbb{Z}_3 \cong \mathbb{Z}_2 \cong \mathbb{Z}/2\mathbb{Z} = G/J$.

# Relationships

## Builds Upon
- **First isomorphism theorem** — Applied in the proof

## Related
- **Second isomorphism theorem** — The other generalisation

# Common Errors

- **Error**: Forgetting that $H$ must be contained in $J$
  **Correction**: The theorem requires $H \subseteq J$, not just both normal

# Common Confusions

- **Confusion**: Thinking $(G/H)/(J/H)$ is somehow "G/J/H" or involves three levels of quotienting
  **Clarification**: $(G/H)/(J/H)$ is a single quotient of the group $G/H$ by its normal subgroup $J/H$, and the theorem says this equals $G/J$.

# Source Reference

Chapter 16: Homomorphisms, Theorem (16.5), p. 96 (pdf).

# Verification Notes

- Definition source: Direct from Theorem (16.5)
- Confidence rationale: HIGH — explicit theorem with proof
- Uncertainties: None
