---
# === CORE IDENTIFICATION ===
concept: Extension of Groups
slug: extension-of-groups

# === CLASSIFICATION ===
category: automorphisms-extensions
subcategory: extensions
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Automorphisms and Extensions"
chapter_number: 3
pdf_page: 49
section: "Extensions of groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - short exact sequence of groups
  - group extension

# === TYPED RELATIONSHIPS ===
prerequisites:
  - normal-subgroup
  - quotient-group
  - homomorphism
extends: []
related:
  - semidirect-product
  - split-extension
  - central-extension
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an extension of groups?"
---

# Quick Definition

An extension of $Q$ by $N$ is a short exact sequence $1 \to N \xrightarrow{\iota} G \xrightarrow{\pi} Q \to 1$, meaning $\iota$ is injective, $\pi$ is surjective, and $\ker(\pi) = \operatorname{im}(\iota)$.

# Core Definition

"A sequence $1 \to N \xrightarrow{\iota} G \xrightarrow{\pi} Q \to 1$ is exact if $\iota$ is injective, $\pi$ is surjective, and $\operatorname{Ker}(\pi) = \operatorname{Im}(\iota)$. ... An exact sequence (16) is also called an extension of $Q$ by $N$" (Milne, p. 49).

# Prerequisites

- **Normal subgroup** — $\iota(N)$ is a normal subgroup of $G$
- **Quotient group** — $Q \simeq G/\iota(N)$
- **Homomorphism** — $\iota$ and $\pi$ are group homomorphisms

# Key Properties

1. $\iota(N) \trianglelefteq G$ and $G/\iota(N) \simeq Q$
2. Two extensions are isomorphic if there is a commutative diagram with identity on $N$ and $Q$
3. Every extension induces a homomorphism $\theta: Q \to \operatorname{Out}(N)$
4. $\operatorname{Ext}^1(Q,N)_\theta$ classifies extensions with a given $\theta$
5. A semidirect product $N \rtimes_\theta Q$ gives an extension $1 \to N \to N \rtimes_\theta Q \to Q \to 1$

# Context & Application

Extensions are the framework for understanding how groups are built from simpler pieces. The Holder program seeks to classify all finite groups by (A) classifying simple groups and (B) classifying all extensions.

# Examples

**Example 1** (p. 50): $1 \to C_p \to C_{p^2} \to C_p \to 1$ is a non-split extension.

**Example 2** (p. 50): $1 \to Z(Q) \to Q \to Q/Z(Q) \to 1$ for the quaternion group does not split.

# Relationships

## Enables
- **split-extension** — Special case: extensions isomorphic to semidirect products
- **central-extension** — Special case: $\iota(N) \subset Z(G)$

## Related
- **semidirect-product** — Every semidirect product defines an extension

# Common Errors

- **Error**: Assuming all extensions split
  **Correction**: $1 \to C_p \to C_{p^2} \to C_p \to 1$ does not split

# Common Confusions

- **Confusion**: The terminology "extension of $Q$ by $N$" vs "extension of $N$ by $Q$"
  **Clarification**: Milne (following Bourbaki) calls $1 \to N \to G \to Q \to 1$ an extension of $Q$ by $N$; some authors reverse this convention

# Source Reference

Chapter 3: Automorphisms and Extensions, "Extensions of groups", equation (16), page 49.

# Verification Notes

- Definition source: Direct from p. 49
- Confidence: HIGH — explicit definition
- Uncertainties: None
